#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class listener(Node):
    def __init__(self):
        super().__init__('listener')
        self.suscriber = self.create_subscription(String ,'/new',self.listener_callback ,10)# creating suscriber
        
    def listener_callback(self, msg):
        self.get_logger().info(f'Received: "{msg.data}"') 


def main(args=None):
    rclpy.init(args=args)
    node = listener()
    rclpy.spin(node)   #running the node again and again 
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()