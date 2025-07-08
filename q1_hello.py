#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class Talker(Node):
    def __init__(self):
        super().__init__('talker')
        self.publisher_ = self.create_publisher(String, '/new', 10) #creating publihser to publish the message on topic /new 
         
        timer_period = 1.0 / 15  # 15 times per second so it will be 15 hz
        self.timer = self.create_timer(timer_period, self.timer_callback) #calling timer_callback func 15 times per sec
        self.msg = String()
        self.msg.data = "Hello World !"

    def timer_callback(self):
        self.publisher_.publish(self.msg)
        self.get_logger().info("Publishing") #logger just to inform it is publishing

    

def main(args=None):
    rclpy.init(args=args)
    node = Talker()
    rclpy.spin(node)   #running the node again and again 
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
