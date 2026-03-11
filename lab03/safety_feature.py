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

        # --- Base Parameters ---
        self.declare_parameter("scan_topic", "/scan")
        self.declare_parameter("safety_topic", '/vesc/input/safety')
        self.declare_parameter("position_topic", '/vesc/low_level/ackermann_cmd')
        self.declare_parameter("side", 1)
        self.declare_parameter("velocity", 1.0)

        # --- Tunable Safety Parameters (extracted from hardcoded values) ---
        self.declare_parameter("side_angle_min", np.pi / 4.0)
        self.declare_parameter("side_angle_max", 115.0 * (np.pi / 180.0))
        self.declare_parameter("min_wall_dist", 0.25)
        self.declare_parameter("front_angle", 0.55)
        self.declare_parameter("safe_front_dist", 0.4)
        self.declare_parameter("speed_multiplier", 0.3)

        # Fetch constants from the ROS parameter server
        self.SCAN_TOPIC = self.get_parameter('scan_topic').get_parameter_value().string_value
        self.SAFETY_TOPIC = self.get_parameter('safety_topic').get_parameter_value().string_value
        self.POSITION_TOPIC = self.get_parameter('position_topic').get_parameter_value().string_value
        self.SIDE = self.get_parameter('side').get_parameter_value().integer_value
        self.VELOCITY = self.get_parameter('velocity').get_parameter_value().double_value

        # Fetch tunable constants
        self.SIDE_ANGLE_MIN = self.get_parameter('side_angle_min').get_parameter_value().double_value
        self.SIDE_ANGLE_MAX = self.get_parameter('side_angle_max').get_parameter_value().double_value
        self.MIN_WALL_DIST = self.get_parameter('min_wall_dist').get_parameter_value().double_value
        self.FRONT_ANGLE = self.get_parameter('front_angle').get_parameter_value().double_value
        self.SAFE_FRONT_DIST = self.get_parameter('safe_front_dist').get_parameter_value().double_value
        self.SPEED_MULTIPLIER = self.get_parameter('speed_multiplier').get_parameter_value().double_value

        # Activates the parameters_callback function
        self.add_on_set_parameters_callback(self.parameters_callback)

        # Initialize publishers and subscribers
        self.stop_publisher = self.create_publisher(AckermannDriveStamped, self.SAFETY_TOPIC, 10)
        self.scan_subscriber = self.create_subscription(LaserScan, self.SCAN_TOPIC, self.listener_callback, 10)
        self.car_pose_subscriber = self.create_subscription(AckermannDriveStamped, self.POSITION_TOPIC, self.car_listen, 10)

        self.speed = self.VELOCITY

    def forcestop(self, received_scan):
        ranges = np.array(received_scan.ranges)
        valid_distances_mask = (ranges > received_scan.range_min) & (ranges < received_scan.range_max)

        all_angles = np.linspace(received_scan.angle_min, received_scan.angle_max, len(ranges))

        # Apply parameterized angle ranges for side wall detection
        if self.SIDE == 1:
            wall_distances_mask = valid_distances_mask & (all_angles > self.SIDE_ANGLE_MIN) & (all_angles < self.SIDE_ANGLE_MAX)
        else:
            wall_distances_mask = valid_distances_mask & (all_angles < -self.SIDE_ANGLE_MIN) & (all_angles > -self.SIDE_ANGLE_MAX)

        wall_distances = ranges[wall_distances_mask]

        # Check against tunable minimum wall distance
        if len(wall_distances) > 0 and min(wall_distances) < self.MIN_WALL_DIST:
            return True

        # Apply parameterized front mask angles
        front_mask = valid_distances_mask & (all_angles > -self.FRONT_ANGLE) & (all_angles < self.FRONT_ANGLE)
        front_ranges = ranges[front_mask]

        if len(front_ranges) > 0:
            front_dist = np.min(front_ranges)

            # Check against tunable safe distances and dynamic speed calculations
            if front_dist < self.SAFE_FRONT_DIST or front_dist < (self.speed * self.SPEED_MULTIPLIER):
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
        Dynamically updates parameters when modified via 'ros2 param set'.
        """
        for param in params:
            if param.name == 'side':
                self.SIDE = param.value
                self.get_logger().info(f"Updated side to {self.SIDE}")
            elif param.name == 'velocity':
                self.VELOCITY = param.value
                self.speed = self.VELOCITY # Sync fallback speed
                self.get_logger().info(f"Updated velocity to {self.VELOCITY}")
            elif param.name == 'side_angle_min':
                self.SIDE_ANGLE_MIN = param.value
                self.get_logger().info(f"Updated side_angle_min to {self.SIDE_ANGLE_MIN}")
            elif param.name == 'side_angle_max':
                self.SIDE_ANGLE_MAX = param.value
                self.get_logger().info(f"Updated side_angle_max to {self.SIDE_ANGLE_MAX}")
            elif param.name == 'min_wall_dist':
                self.MIN_WALL_DIST = param.value
                self.get_logger().info(f"Updated min_wall_dist to {self.MIN_WALL_DIST}")
            elif param.name == 'front_angle':
                self.FRONT_ANGLE = param.value
                self.get_logger().info(f"Updated front_angle to {self.FRONT_ANGLE}")
            elif param.name == 'safe_front_dist':
                self.SAFE_FRONT_DIST = param.value
                self.get_logger().info(f"Updated safe_front_dist to {self.SAFE_FRONT_DIST}")
            elif param.name == 'speed_multiplier':
                self.SPEED_MULTIPLIER = param.value
                self.get_logger().info(f"Updated speed_multiplier to {self.SPEED_MULTIPLIER}")

        return SetParametersResult(successful=True)


def main():
    rclpy.init()
    safety_stop = SafetyStop()
    rclpy.spin(safety_stop)
    safety_stop.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
