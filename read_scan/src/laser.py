#!/usr/bin/env python
import rospy
from sensor_msgs.msg import LaserScan

def readScan(msg):
	rang = msg.ranges
	incre = msg.angle_increment
	print(rang)

rospy.init_node('laser')
scan_sub = rospy.Subscriber('scan',LaserScan,readScan)
rospy.spin()
