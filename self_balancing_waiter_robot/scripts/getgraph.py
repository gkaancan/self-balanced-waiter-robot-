#!/usr/bin/python3
# -*- coding: utf-8 -*-
import rospy
from nav_msgs.msg import Odometry
import time
from geometry_msgs.msg import Twist
import math
from std_msgs.msg import Float32
from sensor_msgs.msg import LaserScan
import numpy as np

vel = []
times = []
errors = []
i = 0
def callback_Twist(data):
    global vel,times,i
    vel.append(data.linear.x)
    times.append(i)
    print(i)
    i = i + 1/250
def durdur():
    global errors,times
    nar = np.array([vel,times])
    np.savetxt("/home/kaan/points_cloud.txt",nar)
    print("dosya olusturuldu")
def callback_error(data):
    global i
    errors.append(data.data)
    #i = i + 1/250

rospy.Subscriber("/cmd_vel",Twist,callback_Twist)
rospy.Subscriber("/error",Float32,callback_error)

rospy.init_node("get_graph")
rospy.on_shutdown(durdur)
r = rospy.Rate(250)

while not rospy.is_shutdown():
    r.sleep()

