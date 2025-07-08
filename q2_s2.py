#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class Signal2(Node):
    def __init__(self):
        super().__init__('signal2')
        self.subscriber_ = self.create_subscription(String,'/s1',self.listener_callback,10)
        self.publisher_ = self.create_publisher(String, '/s2', 10)

    def listener_callback(self, msg):
        if msg.data == 'red':
            colour = 'green'
        else:
            colour ='red'
        response = String()
        response.data = colour
        self.publisher_.publish(response)
        self.get_logger().info(f'S2: Received "{msg.data}", Published "{response.data}"')

def main(args=None):
    rclpy.init(args=args)
    node = Signal2()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
