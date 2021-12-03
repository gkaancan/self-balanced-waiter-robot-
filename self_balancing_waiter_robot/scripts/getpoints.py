#!/usr/bin/python3
# -*- coding: utf-8 -*-
import rospy
from nav_msgs.msg import Odometry
from tf.transformations import euler_from_quaternion
from geometry_msgs.msg import Point, Twist
import math
from std_msgs.msg import Float32
from sensor_msgs.msg import LaserScan
import numpy as np
import pandas as pd


theta = 0.0

class points:
    x= 0.0
    y= 0.0

robot = points()
obstacles_list_x = []
obstacles_list_y = []     
    
laser = np.empty([720])
resolution = 1
regions = {
            "0":0   #0
           ,"15":0  #60
           ,"30":0  #120
           ,"45":0  #180
           ,"60":0  #240
           ,"75":0  #300
           ,"90":0  #360
           ,"105":0 #420
           ,"120":0 #480
           ,"135":0 #540
           ,"150":0 #600
           ,"165":0 #660
           ,"180":0 #719   
}
regions_basic = {
    "0":0,
    "180":0
}
def stop():
    global obstacles_list_x,obstacles_list_y
    
    point_array = np.array([obstacles_list_x,obstacles_list_y])
    
    np.savetxt("/home/kaan/points_cloud.txt",point_array)
    
    print("\npoints_cloud.txt dosyasi olusturuldu")

def get_regions(regionslist,info):
    i = 0
    for x in regionslist:
        try:
            regionslist[x]=min(info[i],10)
        except:
            regionslist[x]=min(info[i-1],10)    
        i = i + 60

def get_regions_basic(regionlist,info):
    regionlist[0] = min(info[0],10)
    regionlist[1] = min(info[719],10)


def callback_odom (msg):
    global robot
    global theta

    robot.x = msg.pose.pose.position.x
    robot.y = msg.pose.pose.position.y

    orientation_q = msg.pose.pose.orientation
    orientation_list = [orientation_q.x, orientation_q.y, orientation_q.z, orientation_q.w]
    (roll, pitch, theta) = euler_from_quaternion (orientation_list)

def callback_laser(msg):
    global laser
    laser =np.array(msg.ranges)


def get_angle(region):
    return int(region)


def find_obstacles_points(angle,robot,distance):
    global obstacles_list_x,obstacles_list_y,theta,resolution
    y = round(math.sin(angle+theta-degree_to_radian(90))*distance+robot.y,resolution)
    x = round(math.sin(angle+theta)*distance+robot.x,resolution)

    if obstacles_list_x.count(x) == 0 or obstacles_list_y.count(y) == 0:
        obstacles_list_x.append(x)
        obstacles_list_y.append(y)
        print("y:",y)
        print("x:",x)
        #print("x: {}   y:{} \n angle: {} theta:{} \n distance: {}".format(x,y,radian_to_degree(angle),theta,distance))
        #print("x: {}   y:{} \n angle: {} theta:{} \n distance: {}".format(math.sin(angle+theta)*distance,math.cos(angle+theta+degree_to_radian(180))*distance,radian_to_degree(angle),radian_to_degree(theta),distance))
        
def degree_to_radian(degree):
    return degree*math.pi/180.0
def radian_to_degree(radian):
    return radian*180.0/math.pi    



rospy.init_node("get_points")
r = rospy.Rate(250)

#-------------------------------------subscribers-----------------------------------
sub_odom = rospy.Subscriber("/odom",Odometry,callback_odom)
sub_laser = rospy.Subscriber('/lidar/laser/scan', LaserScan,callback_laser)
#-------------------------------------subscribers-----------------------------------
rospy.on_shutdown(stop)

while not rospy.is_shutdown():

    get_regions_basic(regions_basic,laser)
    for x in regions_basic:
        if regions_basic[x] < 10 and regions_basic[x] > 0.1:
            find_obstacles_points(degree_to_radian(get_angle(x)),robot,regions_basic[x])

    #get_regions(regions,laser)
    #for x in regions:
        #if regions[x] < 10 and regions[x] > 0.1:
            #find_obstacles_points(degree_to_radian(get_angle(x)),robot,regions[x])
            
       


    