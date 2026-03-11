#!/usr/bin/env python3
import numpy as np
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan
from ackermann_msgs.msg import AckermannDriveStamped
from rcl_interfaces.msg import SetParametersResult

class SafetyStop(Node):

    def __init__(self):
        super().__init__("safety_stop")
        # Declare parameters to make them available for use
        # DO NOT MODIFY THIS!
        self.declare_parameter("scan_topic", "/scan")
        self.declare_parameter("safety_topic", '/vesc/input/safety')
        self.declare_parameter("position_topic", '/vesc/low_level/ackermann_cmd')
        self.declare_parameter("side", 1)
        self.declare_parameter("velocity", 1.0)
        self.declare_parameter("desired_distance", 1.0)

        # Fetch constants from the ROS parameter server
        # DO NOT MODIFY THIS! This is necessary for the tests to be able to test varying parameters!
        self.SCAN_TOPIC = self.get_parameter('scan_topic').get_parameter_value().string_value
        self.SAFETY_TOPIC = self.get_parameter('safety_topic').get_parameter_value().string_value
        self.POSITION_TOPIC = self.get_parameter('position_topic').get_parameter_value().string_value
        self.SIDE = self.get_parameter('side').get_parameter_value().integer_value
        self.VELOCITY = self.get_parameter('velocity').get_parameter_value().double_value
        self.DESIRED_DISTANCE = self.get_parameter('desired_distance').get_parameter_value().double_value

        # This activates the parameters_callback function so that the tests are able
        # to change the parameters during testing.
        # DO NOT MODIFY THIS!
        self.add_on_set_parameters_callback(self.parameters_callback)

        # TODO: Initialize your publishers and subscribers here
        self.stop_publisher = self.create_publisher(AckermannDriveStamped, self.SAFETY_TOPIC, 10)
        self.scan_subscriber = self.create_subscription(LaserScan, self.SCAN_TOPIC, self.listener_callback, 10)
        self.car_pose_subscriber = self.create_subscription(AckermannDriveStamped, self.POSITION_TOPIC, self.car_listen, 10)

        # TODO: Write your callback functions here
        self.speed = self.VELOCITY

    def forcestop(self, received_scan):
        ranges = np.array(received_scan.ranges)
        valid_distances_mask = (ranges > received_scan.range_min) & (ranges < received_scan.range_max)

        all_angles = np.linspace(received_scan.angle_min, received_scan.angle_max, len(ranges))

        # angles from +- 45 to 115
        if self.SIDE == 1:
            wall_distances_mask = valid_distances_mask & (all_angles > (np.pi/4.0)) & (all_angles < (115.0 * (np.pi / 180.0)))
        else:
            wall_distances_mask = valid_distances_mask & (all_angles < -(np.pi/4.0)) & (all_angles > -(115.0 * (np.pi / 180.0)))

        wall_distances = ranges[wall_distances_mask]

        if min(wall_distances) < 0.25:
            return True

        front_mask = valid_distances_mask & (all_angles > -0.55) & (all_angles < 0.55)
        front_ranges = ranges[front_mask]

        if len(front_ranges) > 0:
            front_dist = np.min(front_ranges)

            # faster we go the further away we start feeling the corner
            safe_dist = 0.4

            if front_dist < safe_dist or front_dist < self.speed * 0.3:
                return True

        return False

    def listener_callback(self, received):

        stop = self.forcestop(received)

        new_instruction = AckermannDriveStamped()

        new_instruction.header.stamp = self.get_clock().now().to_msg()
        new_instruction.header.frame_id = 'base_link'
        if stop:
            new_instruction.drive.speed = 0.0
            self.stop_publisher.publish(new_instruction)

    def car_listen(self, car_position):
        if car_position:
            self.speed = car_position.drive.speed

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
    wall_follower = SafetyStop()
    rclpy.spin(wall_follower)
    wall_follower.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
