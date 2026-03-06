#!/usr/bin/env python3
import numpy as np
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan
from ackermann_msgs.msg import AckermannDriveStamped
from rcl_interfaces.msg import SetParametersResult

class WallFollower(Node):

    def __init__(self):
        super().__init__("wall_follower")
        # Declare parameters to make them available for use
        # DO NOT MODIFY THIS!
        self.declare_parameter("scan_topic", "/scan")
        self.declare_parameter("drive_topic", "/vesc/high_level/input/nav_0")
        self.declare_parameter("side", 1)
        self.declare_parameter("velocity", 1.0)
        self.declare_parameter("desired_distance", 1.0)

        # Fetch constants from the ROS parameter server
        # DO NOT MODIFY THIS! This is necessary for the tests to be able to test varying parameters!
        self.SCAN_TOPIC = self.get_parameter('scan_topic').get_parameter_value().string_value
        self.DRIVE_TOPIC = self.get_parameter('drive_topic').get_parameter_value().string_value
        self.SIDE = self.get_parameter('side').get_parameter_value().integer_value
        self.VELOCITY = self.get_parameter('velocity').get_parameter_value().double_value
        self.DESIRED_DISTANCE = self.get_parameter('desired_distance').get_parameter_value().double_value

        # This activates the parameters_callback function so that the tests are able
        # to change the parameters during testing.
        self.add_on_set_parameters_callback(self.parameters_callback)

        #publisher and subscriber
        self.steer_publisher = self.create_publisher(AckermannDriveStamped, self.DRIVE_TOPIC, 10)
        self.scan_subscriber = self.create_subscription(LaserScan, self.SCAN_TOPIC, self.listener_callback, 10)

        # TODO: Write your callback functions here
        #setting PD constants
        self.kp = 4.0
        self.kd = 4.0

    def slice_scan(self, received_scan):
        """
        Function to read LaserScan range and angle data.
        Masks are applied to slice all data to get the desired data for wall following.
        Inputs are the scan data and output is the desired steer angle change.
        """
        ranges = np.array(received_scan.ranges) #get all laserscan ranges
        valid_distances_mask = (ranges > received_scan.range_min) & (ranges < received_scan.range_max) #slice ranges into allowable ranges based on range_min & range_max

        all_angles = np.linspace(received_scan.angle_min, received_scan.angle_max, len(ranges)) #get all laserscan angles

        # angles from +- 45 to 115
        #get valid masking for ranges and angles
        if self.SIDE == 1:
            wall_distances_mask = valid_distances_mask & (all_angles > (np.pi/3.0)) & (all_angles < (115.0 * (np.pi / 180.0)))
        else:
            wall_distances_mask = valid_distances_mask & (all_angles < -(np.pi/3.0)) & (all_angles > -(115.0 * (np.pi / 180.0)))

        #get sliced ranges and angles by applying mask to ranges and angles
        wall_distances = ranges[wall_distances_mask]
        needed_angles = all_angles[wall_distances_mask]

        #convert from rotated to cartesian frame
        all_x = wall_distances * np.cos(needed_angles)
        all_y = wall_distances * np.sin(needed_angles)

        #get median of y data to make the line based on earlier points for estimating the line (get rid of extraneous points/outliers)
        median_y = np.median(all_y)
        tolerance = 0.4 #arbitrary tolerance value
        good_range_mask = np.abs(all_y - median_y) < tolerance #new mask to account for earlier points to make a more accurate lines
        #prevents car location confusion, prevents guessing

        #apply new max to get acceptable x and y values
        good_x = all_x[good_range_mask]
        good_y = all_y[good_range_mask]

        #for external corners: if you only collected two - points then do a full turn into the corner
        if len(good_x) < 2:
            return float(0.34 * self.SIDE)

        x_spread = np.ptp(good_x) #how far the x values are from each other, make the car go straight because the wall is a straight line
        if x_spread < 0.1:
            # vertical line, bad for plotting
            return 0.0

        #get a linear regression fit of the sliced data
        m, c = np.polyfit(good_x, good_y, 1)

        x_offset = self.VELOCITY * 0.5 #want to look a bit further than just the exact distance of wall to wheel -> mainly for corners to estimate where the car would be
        y_at_x_offset = (m * x_offset) + c #wall distances

        #apply third mask as an emergency front mask, helped to dampen oscillations
        front_mask = valid_distances_mask & (all_angles > -0.2) & (all_angles < 0.2)
        front_ranges = ranges[front_mask] #apply new mask, approaching a wall need to turn

        front_detection_error = 0.0
        if len(front_ranges) > 0:
            front_dist = np.min(front_ranges) #get the minimum front distance

            # faster we go the further away we start feeling the corner
            safe_dist = self.DESIRED_DISTANCE * self.VELOCITY

            if front_dist < safe_dist: #need to account for the closer front wall
                front_detection_error = (safe_dist - front_dist) * 2.0 #we are too close to the front wall, increase the error manually -> increase turning factor

        error = self.DESIRED_DISTANCE - abs(y_at_x_offset) + front_detection_error #calculate the wall distance error

        # derivative for PD controller
        if not hasattr(self, 'prev_error'):
            self.prev_error = 0.0

        derivative = error - self.prev_error #calculate the derivative numerator for PD controller
        self.prev_error = error

        #calculate the steer angle -> PD control
        steer_angle_change = ((error * self.kp) + (derivative * self.kd)) * -self.SIDE  #account for wall following side

        #cut out extraneous values
        steer_angle_change = np.clip(steer_angle_change, -0.34, 0.34)

        return steer_angle_change

    def listener_callback(self, received):
        """
        Callback function for Ackermann Message that is published.
        Inputs are received data and output is a AK Message with speed and a steering angle.
        """
        new_steer_angle = self.slice_scan(received)

        new_instruction = AckermannDriveStamped()

        new_instruction.header.stamp = self.get_clock().now().to_msg()
        new_instruction.header.frame_id = 'base_link'
        new_instruction.drive.speed = self.VELOCITY
        new_instruction.drive.steering_angle = new_steer_angle

        self.steer_publisher.publish(new_instruction)

    def parameters_callback(self, params):
        """
        DO NOT MODIFY THIS CALLBACK FUNCTION!

        This is used by the test cases to modify the parameters during testing.
        It's called whenever a parameter is set via 'ros2 param set'.
        """
        for param in params:
            if param.name == 'side':
                self.SIDE = param.value
                self.get_logger().info(f"Updated side to {self.SIDE}")
            elif param.name == 'velocity':
                self.VELOCITY = param.value
                self.get_logger().info(f"Updated velocity to {self.VELOCITY}")
            elif param.name == 'desired_distance':
                self.DESIRED_DISTANCE = param.value
                self.get_logger().info(f"Updated desired_distance to {self.DESIRED_DISTANCE}")
        return SetParametersResult(successful=True)


def main():
    rclpy.init()
    wall_follower = WallFollower()
    rclpy.spin(wall_follower)
    wall_follower.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
