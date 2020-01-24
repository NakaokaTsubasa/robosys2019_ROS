#!/usr/bin/env python

import sys, tty, select, termios
import rospy
from std_msgs.msg import String

if __name__ == '__main__':
    rospy.init_node("keyboard_driver")
    key_pub = rospy.Publisher('keyboard', String, queue_size=1)
    rate = rospy.Rate(100)
    old_attr = termios.tcgetattr(sys.stdin)
    tty.setcbreak(sys.stdin.fileno())
    
    while not rospy.is_shutdown():
        if select.select([sys.stdin], [], [], 0)[0] == [sys.stdin]:
            key_pub.publish(sys.stdin.read(1))
        rate.sleep()
    
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_attr)
