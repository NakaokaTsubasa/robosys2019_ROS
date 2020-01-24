#!/usr/bin/env python

import rospy
from std_msgs.msg import String
import os

def Lchika(message):
    if message.data == "u":
        os.system("echo u > /dev/myled0")
    elif message.data == "n":
        os.system("echo n > /dev/myled0")
    elif message.data == 'k':
        os.system("echo k > /dev/myled0")
    elif message.data == 'o':
        os.system("echo o > /dev/myled0")
    elif message.data == '1':
        os.system("echo 1 > /dev/myled0")
    else:
        os.system("echo 0 > /dev/myled0")

if __name__ == '__main__':
    rospy.init_node('flash_LED')
    rospy.Subscriber('keyboard', String, Lchika)
    rospy.spin()
    os.system("echo 0 > /dev/myled0")
