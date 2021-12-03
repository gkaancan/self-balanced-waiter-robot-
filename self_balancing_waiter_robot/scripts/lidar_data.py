#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'lidar_data.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import rospy
from std_msgs.msg import Float32
from sensor_msgs.msg import LaserScan

class Ui_LidarWindow(object):
    
    def setupUi(self, LidarWindow):
        LidarWindow.setObjectName("LidarWindow")
        LidarWindow.resize(240, 195)
        LidarWindow.setMinimumSize(QtCore.QSize(240, 195))
        LidarWindow.setMaximumSize(QtCore.QSize(240, 195))
        self.centralwidget = QtWidgets.QWidget(LidarWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(10, 10, 221, 161))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.formLayout_2 = QtWidgets.QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setObjectName("formLayout_2")
        self.etiket_fleft = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.etiket_fleft.setObjectName("etiket_fleft")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.etiket_fleft)
        self.etiket_fright = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.etiket_fright.setObjectName("etiket_fright")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.etiket_fright)
        self.etiket_left = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.etiket_left.setObjectName("etiket_left")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.etiket_left)
        self.etiket_front = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.etiket_front.setObjectName("etiket_front")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.etiket_front)
        self.etiket_right = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.etiket_right.setObjectName("etiket_right")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.etiket_right)
        self.line_front = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.line_front.setReadOnly(True)
        self.line_front.setObjectName("line_front")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.line_front)
        self.line_fleft = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.line_fleft.setReadOnly(True)
        self.line_fleft.setObjectName("line_fleft")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.line_fleft)
        self.line_fright = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.line_fright.setReadOnly(True)
        self.line_fright.setObjectName("line_fright")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.line_fright)
        self.line_left = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.line_left.setReadOnly(True)
        self.line_left.setObjectName("line_left")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.line_left)
        self.line_right = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.line_right.setReadOnly(True)
        self.line_right.setObjectName("line_right")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.line_right)
        LidarWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(LidarWindow)
        self.statusbar.setObjectName("statusbar")
        LidarWindow.setStatusBar(self.statusbar)
        self.regions={}
        self.retranslateUi(LidarWindow)
        QtCore.QMetaObject.connectSlotsByName(LidarWindow)

    def retranslateUi(self, LidarWindow):
        _translate = QtCore.QCoreApplication.translate
        LidarWindow.setWindowTitle(_translate("LidarWindow", "Lidar Data"))
        self.etiket_fleft.setText(_translate("LidarWindow", "Front Left:"))
        self.etiket_fright.setText(_translate("LidarWindow", "Front Right:"))
        self.etiket_left.setText(_translate("LidarWindow", "Left:"))
        self.etiket_front.setText(_translate("LidarWindow", "Front:"))
        self.etiket_right.setText(_translate("LidarWindow", "Right:"))
        rospy.init_node("robot_controller")

        rospy.Subscriber('/lidar/laser/scan', LaserScan,self.callbackLaser)
        
    def callbackLaser(self,msg):
        self.regions = {
            'right':  min(min(msg.ranges[0:143]), 10),
            'fright': min(min(msg.ranges[144:287]), 10),
            'front':  min(min(msg.ranges[288:431]), 10),
            'fleft':  min(min(msg.ranges[432:575]), 10),
            'left':   min(min(msg.ranges[576:719]), 10),
        }
        self.actions()
    def actions (self):
        if self.regions['fleft']>=10:
           self.line_front.setText('>=10')
        else:
            self.line_front.setText(str(round(self.regions['front'],3)))

        if self.regions['fleft']>=10:
           self.line_fleft.setText('>=10')
        else:
            self.line_fleft.setText(str(round(self.regions['fleft'],3)))

        if self.regions['fright']>=10:
           self.line_fright.setText('>=10')
        else:
            self.line_fright.setText(str(round(self.regions['fright'],3)))

        if self.regions['left']>=10:
           self.line_left.setText('>=10')
        else:
            self.line_left.setText(str(round(self.regions['left'],3)))

        if self.regions['right']>=10:
           self.line_right.setText('>=10')
        else:
            self.line_right.setText(str(round(self.regions['right'],3)))    
        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    LidarWindow = QtWidgets.QMainWindow()
    ui = Ui_LidarWindow()
    ui.setupUi(LidarWindow)
    LidarWindow.show()
    sys.exit(app.exec_())
