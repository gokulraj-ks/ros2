import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class ros2_sub(Node):
    def __init__(self):
        super().__init__('ros2_sub')
        self.sub=self.create_subscription(Twist,"cmd_vel",self.vel_cb,10)

    def vel_cb(self,msg):
        print(msg.linear.x)

        
def main():
    rclpy.init(args=None)
    ros2_class=ros2_sub()
    rclpy.spin(ros2_class)

main()