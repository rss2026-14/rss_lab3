#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from ackermann_msgs.msg import AckermannDriveStamped
from rcl_interfaces.msg import SetParametersResult

class ForwardDrive(Node):

    def __init__(self):
        super().__init__("forward_drive")

        # Declare parameters to make them available for use
        # DO NOT MODIFY THIS!
        self.declare_parameter("drive_topic", "/vesc/high_level/input/nav_0")
        self.declare_parameter("velocity", 1.0)
        self.declare_parameter("steering_angle", 0.0)

        self.DRIVE_TOPIC = self.get_parameter('drive_topic').get_parameter_value().string_value
        self.VELOCITY = self.get_parameter('velocity').get_parameter_value().double_value
        self.STEERING_ANGLE = self.get_parameter('steering_angle').get_parameter_value().double_value

        self.add_on_set_parameters_callback(self.parameters_callback)

        # Publisher for the Ackermann drive commands
        self.steer_publisher = self.create_publisher(AckermannDriveStamped, self.DRIVE_TOPIC, 10)

        timer_period = 1.0 / 20.0 # (20 Hz)
        self.timer = self.create_timer(timer_period, self.timer_callback)

    def timer_callback(self):
        """
        Callback function executed by the timer.
        Continuously outputs an Ackermann Message with the designated speed and steering angle.
        """
        new_instruction = AckermannDriveStamped()

        new_instruction.header.stamp = self.get_clock().now().to_msg()
        new_instruction.header.frame_id = 'base_link'

        # Apply the parameters for speed and steering angle
        new_instruction.drive.speed = float(self.VELOCITY)
        new_instruction.drive.steering_angle = float(self.STEERING_ANGLE)

        self.steer_publisher.publish(new_instruction)

    def parameters_callback(self, params):
        """
        DO NOT MODIFY THIS CALLBACK FUNCTION!

        This is used by the test cases to modify the parameters during testing.
        It's called whenever a parameter is set via 'ros2 param set'.
        """
        for param in params:
            if param.name == 'velocity':
                self.VELOCITY = param.value
                self.get_logger().info(f"Updated velocity to {self.VELOCITY}")
            elif param.name == 'steering_angle':
                self.STEERING_ANGLE = param.value
                self.get_logger().info(f"Updated steering_angle to {self.STEERING_ANGLE}")
            elif param.name == 'drive_topic':
                self.DRIVE_TOPIC = param.value
                self.get_logger().info(f"Updated drive_topic to {self.DRIVE_TOPIC}")

        return SetParametersResult(successful=True)


def main():
    rclpy.init()
    forward_drive = ForwardDrive()
    rclpy.spin(forward_drive)
    forward_drive.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
