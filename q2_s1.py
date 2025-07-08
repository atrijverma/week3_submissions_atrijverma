#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class Signal1(Node):
    def __init__(self):
        super().__init__('signal1')
        self.publisher_ = self.create_publisher(String, '/s1', 10)
        self.state = 'green'
        self.timer = self.create_timer(10.0, self.timer_callback)
        self.publish_state()

    def publish_state(self):
        msg = String()
        msg.data = self.state
        self.publisher_.publish(msg)
        self.get_logger().info(f'S1: Published "{msg.data}"')

    def timer_callback(self):
        # Toggle state between green and red every 10 seconds
        self.state = 'red' if self.state == 'green' else 'green'
        self.publish_state()

def main(args=None):
    rclpy.init(args=args)
    node = Signal1()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
