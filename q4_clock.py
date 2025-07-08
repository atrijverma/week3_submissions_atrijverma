#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import Int64, String

class ClockPublisher(Node):
    def __init__(self):
        super().__init__('clock_publisher')

        # Publishers
        self.second_pub = self.create_publisher(Int64, '/second', 10)
        self.minute_pub = self.create_publisher(Int64, '/minute', 10)
        self.hour_pub = self.create_publisher(Int64, '/hour', 10)
        self.clock_pub = self.create_publisher(String, '/clock', 10)

        self.seconds = 0
        self.minutes = 0
        self.hours = 0
        self.timer = self.create_timer(1.0, self.timer_callback)

    def timer_callback(self):
        # Publish individual values
        self.publish_time_components

        # Publish formatted clock
        clock_msg = String()
        clock_msg.data = f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}"
        self.clock_pub.publish(clock_msg)
        self.get_logger().info(f"Clock: {clock_msg.data}")

        # Increment seconds
        self.seconds += 1
        if self.seconds >= 60:
            self.seconds = 0
            self.minutes += 1
            if self.minutes >= 60:
                self.minutes = 0
                self.hours += 1

    def publish_time_components(self):
        sec = Int64()
        sec.data = self.seconds
        self.second_pub.publish(sec)
        min = Int64()
        min.data = self.minutes
        self.minute_pub.publish(min)
        hour = Int64()
        hour.data = self.hours
        self.hour_pub.publish(hour)

def main(args=None):
    rclpy.init(args=args)
    node = ClockPublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
