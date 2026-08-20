import rclpy
from rclpy.node import Node

import serial
import struct

from geometry_msgs.msg import Twist

class BridgeNode(Node):

    def __init__(self):
        super().__init__("bridge_node")
        self.subscription = self.create_subscription(Twist, 'topic', self.message_cb, 10)
        self.ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
        self.wheel_separation = 0.13  # meters
        self.max_speed = 1.11824123 # meters per second

    def message_cb(self, msg):
        left_pwm, right_pwm = self.diff_drive_kinematics(msg.linear.x, msg.angular.z)
        self.get_logger().info(f"Sent Left PWM: {left_pwm} and Right PWM: {right_pwm}")

        packet = struct.pack('Bbb', 0xFF, left_pwm, right_pwm)
        self.ser.write(packet)

    def diff_drive_kinematics(self, linear_vel, angular_vel):
        self.get_logger().info(f"Linear Velocity: {linear_vel}, Angular Velocity: {angular_vel}")
        left_vel = linear_vel - angular_vel * (self.wheel_separation / 2)
        right_vel = linear_vel + angular_vel * (self.wheel_separation / 2)

        left_pwm = max(-100, min(100, int((left_vel / self.max_speed) * 100)))
        right_pwm = max(-100, min(100, int((right_vel / self.max_speed) * 100)))
        return left_pwm, right_pwm



def main(args=None):
    rclpy.init()
    bridge = BridgeNode()
    rclpy.spin(bridge)
    bridge.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main();