#!/usr/bin/python3
# -*- coding: utf-8 -*-

import rospy
from std_msgs.msg import Float32
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist

def clbk_laser(msg):
    regions = {
        'right':  min(min(msg.ranges[0:143]), 10),
        'fright': min(min(msg.ranges[144:287]), 10),
        'front':  min(min(msg.ranges[288:431]), 10),
        'fleft':  min(min(msg.ranges[432:575]), 10),
        'left':   min(min(msg.ranges[576:719]), 10),
    }
    
    take_action(regions)
    
def take_action(regions):
    linear_x = 0
    angular_z = 0
    
    state_description = ''
    
    if regions['front'] > 1:
        linear_x = 0.4

        if (0.5< regions['right']) < 0.1 and regions['left']>0.5:  
            print ('Düz Gidiyorum')    
            linear_x = 0.4
            angular_z= 0

        elif (regions['right']) < 0.5:  
            print ('Sola Dönuyorum')    
            linear_x = 0.4
            angular_z= 0.8

        elif (regions['right']) > 0.5 or regions['left']<0.5:  
            print ('Sağa Dönuyorum')    
            linear_x = 0.4
            angular_z= -0.8
         
                
    else:   
        print('DUR')
        angular_z = 1
        state_description = 'Önde Engel Tespit Edildi'
        rospy.loginfo(regions)


    rospy.loginfo(state_description)
    pub_target.publish(linear_x)
    pub_angular.publish(-angular_z)

def durdur():
    pub_target.publish(0)
    pub_angular.publish(0)
    print("mapping durduruldu.")
    

def main():
    global pub_target
    global pub_angular
    
    rospy.init_node('otonom')
    
    pub_target = rospy.Publisher("/Desired_position",Float32,queue_size=10)

    pub_angular = rospy.Publisher("/rotate",Float32,queue_size=10)  
    
    sub = rospy.Subscriber('/lidar/laser/scan', LaserScan, clbk_laser)
    
    rospy.spin()

if __name__ == '__main__':
    rospy.on_shutdown(durdur)
    main()

    
