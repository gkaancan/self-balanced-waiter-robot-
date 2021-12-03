#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import rospy
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Twist
from std_msgs.msg import Float32
from PyQt5 import QtCore, QtGui, QtWidgets
from lidar_data import Ui_LidarWindow
from sensor_msgs.msg import LaserScan

class Ui_MainWindow(object):
    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(755, 300)
        MainWindow.setMinimumSize(QtCore.QSize(755, 300))
        MainWindow.setMaximumSize(QtCore.QSize(755, 300))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 30, 201, 205))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.etiket_x = QtWidgets.QLabel(self.formLayoutWidget)
        self.etiket_x.setObjectName("etiket_x")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.etiket_x)
        self.etiket_y = QtWidgets.QLabel(self.formLayoutWidget)
        self.etiket_y.setObjectName("etiket_y")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.etiket_y)
        self.etiket_phi = QtWidgets.QLabel(self.formLayoutWidget)
        self.etiket_phi.setObjectName("etiket_phi")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.etiket_phi)
        self.etiket_theta = QtWidgets.QLabel(self.formLayoutWidget)
        self.etiket_theta.setObjectName("etiket_theta")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.etiket_theta)
        self.label_5 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.etiket_velocity = QtWidgets.QLabel(self.formLayoutWidget)
        self.etiket_velocity.setObjectName("etiket_velocity")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.etiket_velocity)
        self.etiket_angularvel = QtWidgets.QLabel(self.formLayoutWidget)
        self.etiket_angularvel.setObjectName("etiket_angularvel")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.etiket_angularvel)
        self.line_y = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.line_y.setReadOnly(True)
        self.line_y.setObjectName("line_y")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.line_y)
        self.line_x = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.line_x.setReadOnly(True)
        self.line_x.setObjectName("line_x")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.line_x)
        self.line_phi = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.line_phi.setReadOnly(True)
        self.line_phi.setObjectName("line_phi")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.line_phi)
        self.line_theta = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.line_theta.setObjectName("line_theta")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.line_theta)
        self.line_velocity = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.line_velocity.setReadOnly(True)
        self.line_velocity.setObjectName("line_velocity")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.line_velocity)
        self.line_angularvel = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.line_angularvel.setReadOnly(True)
        self.line_angularvel.setObjectName("line_angularvel")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.line_angularvel)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 131, 20))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(280, 40, 161, 131))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.button_stop = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.button_stop.setObjectName("button_stop")
        self.gridLayout.addWidget(self.button_stop, 1, 1, 1, 1)
        self.button_sag = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.button_sag.setObjectName("button_sag")
        self.gridLayout.addWidget(self.button_sag, 1, 2, 1, 1)
        self.button_geri = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.button_geri.setObjectName("button_geri")
        self.gridLayout.addWidget(self.button_geri, 2, 1, 1, 1)
        self.button_ileri = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.button_ileri.setObjectName("button_ileri")
        self.gridLayout.addWidget(self.button_ileri, 0, 1, 1, 1)
        self.button_sol = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.button_sol.setObjectName("button_sol")
        self.gridLayout.addWidget(self.button_sol, 1, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(280, 10, 161, 20))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.button_lidar = QtWidgets.QPushButton(self.centralwidget)
        self.button_lidar.setGeometry(QtCore.QRect(280, 177, 89, 25))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.button_lidar.setFont(font)
        self.button_lidar.setObjectName("button_lidar")
        self.button_gmapping = QtWidgets.QPushButton(self.centralwidget)
        self.button_gmapping.setGeometry(QtCore.QRect(280, 210, 89, 25))
        self.button_gmapping.setObjectName("button_gmapping")
        self.button_getmap=QtWidgets.QPushButton(self.centralwidget)
        self.button_getmap.setGeometry(QtCore.QRect(280, 243, 89, 25))
        self.button_getmap.setObjectName("button_gmetmap")
        

        self.etiket_map = QtWidgets.QLabel(self.centralwidget)
        self.etiket_map.setGeometry(QtCore.QRect(510, 10, 220, 250))
        self.etiket_map.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.etiket_map.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.etiket_map.setText("")
        self.etiket_map.setScaledContents(True)
        self.etiket_map.setObjectName("etiket_map")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        
        
    def lidarArayuz(self):
        self.window = QtWidgets.QMainWindow()
        self.ui=Ui_LidarWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Robot Controller"))
        self.etiket_x.setText(_translate("MainWindow", "Position x:"))
        self.etiket_y.setText(_translate("MainWindow", "Position y:"))
        self.etiket_phi.setText(_translate("MainWindow", "Phi:"))
        self.etiket_theta.setText(_translate("MainWindow", "Theta:"))
        self.etiket_velocity.setText(_translate("MainWindow", "Velocity(m/s):"))
        self.etiket_angularvel.setText(_translate("MainWindow", "Angular Vel:"))
        self.label.setText(_translate("MainWindow", "Information Panel"))
        self.button_stop.setText(_translate("MainWindow", "Stop"))
        self.button_sag.setText(_translate("MainWindow", "→"))
        self.button_geri.setText(_translate("MainWindow", "↓"))
        self.button_ileri.setText(_translate("MainWindow", "↑"))
        self.button_sol.setText(_translate("MainWindow", "←"))
        self.label_2.setText(_translate("MainWindow", "Robot Control Panel"))
        self.button_lidar.setText(_translate("MainWindow", "Get Lidar Data"))
        self.button_gmapping.setText(_translate("MainWindow", "Gmapping"))
        self.button_getmap.setText(_translate("MainWindow","Get Map"))

        rospy.init_node("robot_controller")
        self.pub_target = rospy.Publisher("/Desired_position",Float32,queue_size=10)

        self.pub_angular = rospy.Publisher("/rotate",Float32,queue_size=10) 

        rospy.Subscriber("/odom",Odometry,self.odomCallback)
        rospy.Subscriber("/target_speed",Float32,self.targetspeedCallback)
        rospy.Subscriber("/yaw",Float32,self.yawCallback)
        rospy.Subscriber("/pitch",Float32,self.pitchCallback)
        
    

        self.button_ileri.clicked.connect(self.robotIleri)
        self.button_geri.clicked.connect(self.robotGeri)
        self.button_sag.clicked.connect(self.robotSag)
        self.button_sol.clicked.connect(self.robotSol)
        self.button_stop.clicked.connect(self.robotDur)
        self.button_lidar.clicked.connect(self.lidarArayuz)
        
        self.button_getmap.clicked.connect(self.folderSelect)
        self.button_gmapping.clicked.connect(self.gMapping)
        
        
        self.line_x.setText(str(0.0))
        self.line_y.setText(str(0.0))
        self.line_angularvel.setText(str(0.0))
        self.line_velocity.setText(str(0.0))
        self.line_phi.setText(str(0.0))
        self.line_theta.setText(str(0.0))


    def gMapping(self):
        self.sub_lidar=rospy.Subscriber('/lidar/laser/scan', LaserScan, self.clbk_laser)
 
    def clbk_laser(self,msg):
        regions = {
            'right':  min(min(msg.ranges[0:143]), 10),
            'fright': min(min(msg.ranges[144:287]), 10),
            'front':  min(min(msg.ranges[288:431]), 10),
            'fleft':  min(min(msg.ranges[432:575]), 10),
            'left':   min(min(msg.ranges[576:719]), 10),
        }
        
        self.take_action(regions)
        
    def take_action(self,regions):
        linear_x = 0
        angular_z = 0
        
        state_description = ''
        
        if regions['front'] > 1:
            linear_x = 0.75

            if (0.5< regions['right']) < 0.1 and regions['left']>0.5:  
                print ('Düz Gidiyorum')    
                linear_x = 0.75
                angular_z= 0

            elif (regions['right']) < 0.5:  
                print ('Sola Dönuyorum')    
                linear_x = 0.75
                angular_z= 1

            elif (regions['right']) > 0.5 or regions['left']<0.5:  
                print ('Sağa Dönuyorum')    
                linear_x = 0.75
                angular_z= -1
            
                    
        else:   
            print('DUR')
            angular_z = 1.5
            state_description = 'Önde Engel Tespit Edildi'
            rospy.loginfo(regions)


        rospy.loginfo(state_description)
        self.pub_target.publish(linear_x)
        self.pub_angular.publish(-angular_z)



    def folderSelect(self):
        
        fname=QtWidgets.QFileDialog.getOpenFileName(self,"Open File","/home/sitki/maps","Image files (*.jpg *.png)")
        mapPath=fname[0]
        pixmap=QtGui.QPixmap(mapPath)
        self.etiket_map.setPixmap(QtGui.QPixmap(pixmap))
        
    def yawCallback(self,data):
        self.line_theta.setText(str(round(data.data,3)))

    def pitchCallback(self,data):
        self.line_phi.setText(str(round(data.data,3)))

    def odomCallback(self,msg):
        self.line_x.setText(str(round(msg.pose.pose.position.x,3)))
        self.line_y.setText(str(round(msg.pose.pose.position.y,3)))

    def targetspeedCallback(self,data):
        self.line_velocity.setText(str(round(data.data)))
        
    def robotIleri(self):
        self.pub_target.publish(0.75)
        self.pub_angular.publish(0)
        self.line_angularvel.setText(str(0.0))

    def robotGeri(self):
        self.pub_target.publish(-0.75)
        self.pub_angular.publish(0)
        self.line_angularvel.setText(str(0.0))

    def robotSag(self):
        self.pub_target.publish(0)
        self.pub_angular.publish(0.75)
        self.line_angularvel.setText(str(-0.75))

    def robotSol(self):
        self.pub_target.publish(0)
        self.pub_angular.publish(-0.75)
        self.line_angularvel.setText(str(0.75))
    
    def robotDur(self):
        self.pub_target.publish(0)
        self.pub_angular.publish(0)
        self.line_angularvel.setText(str(0.0))
        self.sub_lidar.unregister()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
