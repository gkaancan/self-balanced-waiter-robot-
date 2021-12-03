#!/usr/bin/python3
# -*- coding: utf-8 -*-

import rospy
from nav_msgs.msg import Odometry
from tf.transformations import euler_from_quaternion
from geometry_msgs.msg import Point, Twist
import math
from std_msgs.msg import Float32
from sensor_msgs.msg import LaserScan
import time

engel=False
spin=True
regions={}
x = 0.0
y = 0.0
theta = 0.0
control=True
goal = Point ()
goal.x = 0
goal.y = 0
vel=0
ang=0
reach = False


def donus_yonu(hedef):
    if hedef != 0:
        return 1
    else:
        return -1    

def newOdom (msg):
    global x   
    global y
    global theta

    x = msg.pose.pose.position.x
    y = msg.pose.pose.position.y

    orientation_q = msg.pose.pose.orientation
    orientation_list = [orientation_q.x, orientation_q.y, orientation_q.z, orientation_q.w]
    (roll, pitch, theta) = euler_from_quaternion (orientation_list)

def clbk_laser(msg):
    global regions
    regions = {
        'right':  min(min(msg.ranges[0:143]), 10),
        'fright': min(min(msg.ranges[144:287]), 10),
        'front':  min(min(msg.ranges[288:431]), 10),
        'fleft':  min(min(msg.ranges[432:575]), 10),
        'left':   min(min(msg.ranges[576:719]), 10),
    }

def masaya_git(masa):
    global goal
    if masa==1:
        goal.x = 6.20
        goal.y = -4
    elif masa==2:
        goal.x = 1.45
        goal.y = -6.84
    elif masa==3:
        goal.x = -8
        goal.y = -6.68
    elif masa==4:
        goal.x = -14.47
        goal.y = -4.04
    elif masa==0:
        goal.x = 0.16
        goal.y = 9.16
    else:
        print("Yanlıs masa numarası girildi!!")    

def masaya_git(x,y):
    global goal
    goal.x = x
    goal.y = y
    main()
    
#rospy.init_node("speed_controller")


pub_linear = rospy.Publisher("/Desired_position",Float32,queue_size=10)
pub_angular = rospy.Publisher("/rotate",Float32,queue_size=10)  
sub = rospy.Subscriber('/odom', Odometry, newOdom)
sub = rospy.Subscriber('/lidar/laser/scan', LaserScan, clbk_laser)

#r = rospy.Rate(250)


#masa=int(input("Masa numarası giriniz mutfağa gitmek için 0 giriniz: "))
#masaya_git(masa)

engeldenkac=True

def main():

    global engeldenkac,engel,spin,goal,theta,regions,x,y,vel,ang,control,r,reach
    inc_x = goal.x - x
    inc_y = goal.y - y
    tol=math.sqrt((inc_x)**2+(inc_y)**2)
    angle_to_goal = math.atan2 (inc_y, inc_x)
    
    
    if abs(angle_to_goal - theta) > 0.05 and spin:
        
        vel = 0.0
        ang = -1
        pub_linear.publish(vel)
        pub_angular.publish(ang)
        #print(angle_to_goal,theta)

    else:
        ang = 0
        #pub_linear.publish(vel)
        pub_angular.publish(ang)
        if tol>2.5:
            
            if regions['front'] > 1.25 and engel==False:
                vel=0.5
                pub_linear.publish(vel)
                #pub_angular.publish(ang)
                #print("Tolerans = ",tol)
                #print("(x={:.3f},y={:.3f})".format(x,y))

            else:
                spin=False
                engel=True
                print("Engel Tespit Edildi Engeli Kaldırınız!!")
                
                if engeldenkac:
                    vel=0
                    pub_linear.publish(vel)
                    while regions['front']<1.25:
                        ang=1
                        pub_angular.publish(ang)
                        print("while içinde kaldım yardım")
                    ang=0
                    pub_angular.publish(ang)
                    engeldenkac=False
                elif regions['left'] < 1 or regions['fleft']< 1:
                    vel=0.5
                    pub_linear.publish(vel)
                    if regions['front']<1.25:
                        engeldenkac=True
                else:
                    spin=True
                    engel=False
                    engeldenkac=True
        else:
            vel=0
            pub_linear.publish(vel)
            ang=0
            pub_angular.publish(ang)
            reach = True
            
    pub_linear.publish(vel)
    pub_angular.publish(ang)
    #r.sleep()