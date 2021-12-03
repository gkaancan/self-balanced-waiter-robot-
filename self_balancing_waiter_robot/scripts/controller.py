#!/usr/bin/python3
# -*- coding: utf-8 -*-

from numpy.core.function_base import linspace
from numpy.lib.function_base import angle
import rospy
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Twist, Point
from tf.transformations import euler_from_quaternion
from math import atan2,pi,cos,sin,sqrt
import numpy as np

x1 = 0.0
y1 = 0.0
theta1 = 0.0
velocity_1 = 1.0
speed = Twist()
def stop(): # kodu durdurma 
    velocity_pub_1.publish(Twist())
    
    print("All robots have been stopped")


def get_position_1 (data):
    global x1
    global y1
    global theta1
    x1 = data.pose.pose.position.x
    y1 = data.pose.pose.position.y

    orientation_q = data.pose.pose.orientation
    orientation_list = [orientation_q.x, orientation_q.y, orientation_q.z, orientation_q.w]
    (roll, pitch, theta1) = euler_from_quaternion (orientation_list)

rospy.Subscriber("/robot1/odom",Odometry,get_position_1)
velocity_pub_1 = rospy.Publisher("/robot1/cmd_vel",Twist,queue_size=10)

def go_to_point(goal_x,goal_y):
    global speed
    global x1,y1,theta1
 
    #print("x:{}\n , y:{}\n , theta:{}\n , velocity:{}\n , rotate={}\n".format(x,y,theta,velocity,rotate))
    inc_x = goal_x - x1
    inc_y = goal_y - y1
    #print("x:{}\n , y:{}\n , theta:{}\n , velocity:{}\n , rotate={}\n".format(x,y,theta,velocity,rotate))
    angle_to_goal = atan2 (inc_y,inc_x)

    #print("angle to goal:",angle_to_goal)

    
    if abs(inc_x) > 0.05 and abs(inc_y) > 0.05:
        if abs(angle_to_goal - theta1) > 0.1:
            speed.linear.x = 0
            speed.angular.z = -1
            print("donuyor")
            
        #elif angle_to_goal - theta < -0.1:
            #speed.linear.x = 0
            #speed.angular.z = 1
               
        else:
            #print("açıyı buldu da mı buraya giriyor")
            speed.linear.x = 1.0
            speed.angular.z = 0.0
            print("ilerliyor")
    else:
        
        speed = Twist()
    print(speed)
    speed.linear.x = 0
    speed.angular.z = 1    
    velocity_pub_1.publish(speed)                  
rospy.init_node("controller")
r = rospy.Rate(250)

rospy.on_shutdown(stop)

goal_x = 10.00
goal_y = 10.00

k_linear = 0.05
k_angular = -1


while not rospy.is_shutdown():
    
    inc_x = goal_x - x1
    inc_y = goal_y - y1
    angle_to_goal = atan2 (inc_y,inc_x)
    distance = abs(sqrt(inc_x**2+inc_y**2))
    #if theta1 < 0:
        #theta1 = theta1 + pi
    #if angle_to_goal < 0:
        #angle_to_goal = angle_to_goal + pi    
    print("theta: ",theta1)
    print("goal:",angle_to_goal)
    if distance > 0.1:
        speed.linear.x = distance * k_linear
        speed.angular.z = (angle_to_goal-theta1)*k_angular
        velocity_pub_1.publish(speed)
    else:
        velocity_pub_1.publish(Twist())    
    r.sleep()
