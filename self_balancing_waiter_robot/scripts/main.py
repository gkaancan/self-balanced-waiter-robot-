#!/usr/bin/python3
# -*- coding: utf-8 -*-

import rospy
from nav_msgs.msg import Odometry
from tf.transformations import euler_from_quaternion, quaternion_from_euler
from geometry_msgs.msg import Twist
import math
from std_msgs.msg import Float32




roll = pitch = yaw = 0.0
target = 0 
target_rad = math.pi*target/180
kp = 4.34
ki = 0.144
kd = 25.26
error = 0.0
error_dif = 0.0
prev_error = 0.0
target_speed = 0.0
error_sum = 0.0
rotate = 0.0


def callback_Kp(data):
    global kp
    kp=data.data
    print("YENI Kp: ",kp)

def callback_Ki(data):
    global ki
    ki=data.data
    print("YENI Ki: ",ki)

def callback_Kd(data):
    global kd
    kd=data.data
    print("YENI Kd: ",kd)

def callback_target(data):
    global target
    target = data.data    
    print ("target = ", target)

def durdur():
    print("Robot durduruldu.")
    pub.publish(Twist())
    
def callback_rotate(msg):
    global rotate 
    rotate = msg.data   


sub_Kp = rospy.Subscriber("/Kp",Float32,callback_Kp)
sub_Ki = rospy.Subscriber("/Ki",Float32,callback_Ki)
sub_Kd = rospy.Subscriber("/Kd",Float32,callback_Kd)
sub_Target = rospy.Subscriber("/Desired_position",Float32,callback_target)
sub_rotate = rospy.Subscriber("/rotate",Float32,callback_rotate) 


    

def get_rotation (msg):
    global roll, pitch, yaw
    
    orientation_q = msg.pose.pose.orientation
    
    orientation_list = [orientation_q.x, orientation_q.y, orientation_q.z, orientation_q.w]
    (roll, pitch, yaw) = euler_from_quaternion (orientation_list)


rospy.init_node('self_balancing')

sub = rospy.Subscriber ('/odom', Odometry, get_rotation)
pub = rospy.Publisher("/cmd_vel",Twist,queue_size=10)



r = rospy.Rate(250)
command = Twist()

rospy.on_shutdown(durdur)

while not rospy.is_shutdown():

    error =   pitch - math.pi*target/180 
    error_sum += error
    error_dif = error - prev_error
    prev_error = error
       	    
    if abs(error) < 50*math.pi/180:
        target_speed = kp*error + ki*error_sum + kd*error_dif
         
        error_sum +=target_speed*0.015      
    
    
    command.linear.x = target_speed
    command.angular.z = rotate
    
    if abs(error) > 50*math.pi/180:
        error_sum = 0
        error_dif = 0
        prev_error = 0 
        command.linear.x = 0
        target = 0


    pub.publish(command)
    
    r.sleep()
