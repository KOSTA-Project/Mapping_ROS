#!/usr/bin/env python
import rospy
import math
import  matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from sensor_msgs.msg import LaserScan

def graph(ranges, inc):
	x=[]
	y=[]
	angle=0
	for d in ranges:
		x.append(d*math.cos(angle))
		y.append(d*math.sin(angle))
		angle+=inc
	sc.set_data(x,y)
	return line,


def readScan(msg):
	f=open('s1.txt','a+')
	f2=open('s2.txt','w')
	angle=0
	rang=msg.ranges
	incre = msg.angle_increment
	print(incre)
	# ani=FuncAnimation(fig, graph, fargs=(rang, incre))
	f.write(str(rang))
	f2.write(str(incre))
	f2.close()
	f.close()



rospy.init_node('laser')


scan_sub = rospy.Subscriber('scan',LaserScan,readScan)

#ani = FuncAnimation(fig, graph, fargs=rang, incre)

#print(scan_sub)
#plt.show()

rospy.spin()
