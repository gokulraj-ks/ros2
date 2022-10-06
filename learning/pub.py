import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class ros2(Node):
    def __init__(self):
        super().__init__('pub')
        self.pub=self.create_publisher(String,"string_pub",10)
        timer_period=0.5
        self.timer=self.create_timer(timer_period,self.timer_callbk)
        self.i=0
    
    def timer_callbk(self):
        msg=String()
        msg.data="hello"
        self.pub.publish(msg)
        
def main():
    rclpy.init(args=None)
    ros2_class=ros2()
    rclpy.spin(ros2_class)

main()