#!/usr/bin/python3
# -*- coding: utf-8 -*-
 
import rospy
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Twist
from std_msgs.msg import Float32
from tf.transformations import euler_from_quaternion, quaternion_from_euler
import math


velocity = 0.0 
angular = 0.0
target_x = 10.0
target_y= 0.0
control_x = False 
control_y = False
i = 5

x,y=0.0,0.0
roll,pitch,yaw = 0.0,0.0,0.0

def callback(data):
    global x,y,roll,pitch,yaw
    x=data.pose.pose.position.x
    y=data.pose.pose.position.y
    orientation_q = data.pose.pose.orientation
    orientation_list = [orientation_q.x, orientation_q.y, orientation_q.z, orientation_q.w]
    (roll, pitch, yaw) = euler_from_quaternion (orientation_list)

def durdur():
    pub_linear.publish(0)
    pub_angular.publish(0)
    print("Robot durduruldu.")  

def reach_x(dif_x,y,yaw):
    global velocity,angular
    global control_x
    print(str(dif_x)+"  "+ str(yaw*180/math.pi))
    if dif_x > 0:
        
        if abs(round(yaw*180/math.pi)) != 0:
            if yaw*180/math.pi < 0:
                angular = -0.2
            elif yaw*180/math.pi> 0:
                angular = +0.2 
            velocity = 0
        else:       
            if dif_x < 0.5:
                velocity = 0
                angular = 0
                #control_x = True
            else:    
                velocity = 0.4
                angular = 0
            
                
    elif dif_x < 0:
        if abs(round(yaw*180/math.pi)) != 0:
            if yaw*180/math.pi < 0:
                angular = 0.2
            elif yaw*180/math.pi > 0:
                angular = -0.2    
            velocity = 0
        else: 
            
            if dif_x > -0.5:
                velocity = 0
                angular = 0.0
                #control_x = True
            else:    
                velocity = -0.4
                angular = 0.0
                    







 
rospy.init_node('hedefe_git')
pub_linear = rospy.Publisher("/Desired_position",Float32,queue_size=10)
pub_angular = rospy.Publisher("/donus",Float32,queue_size=10) 
odom_sub = rospy.Subscriber('/odom', Odometry, callback)
rate = rospy.Rate(250)
rospy.on_shutdown(durdur)
while not rospy.is_shutdown():
    dif_x, dif_y = target_x - x , target_y - y  # x ve y bizim anlık konumumuz
    if abs(dif_x) > 0:
        reach_x(dif_x,y,yaw)
    pub_linear.publish(velocity)
    pub_angular.publish(angular)

          



