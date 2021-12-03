#!/usr/bin/python3
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

point_array = np.loadtxt("/home/kaan/points_cloud.txt")



plt.plot(point_array[1],point_array[0])
plt.xlabel("Time")
plt.ylabel("velocity")
plt.show()


