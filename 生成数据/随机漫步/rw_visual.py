# -*- coding: utf-8 -*-
"""
Created on Tue Jun 19 15:44:08 2018
随机漫步是这样行走得到的路径：
    每次行走都完全是随机的，没有明确的方向，结果是由一系列随即决策决定的
@author: lenovo
"""

import matplotlib.pyplot as plt

from random_walk import RandomWalk

# 创建一个RandomWalk类的实例，并将其包含的点都绘制出来
# 只要程序处于活动状态，就不断模拟随机漫步
while True:
    rw = RandomWalk(50000)
    rw.fill_walk()
    
    # 设置绘图窗口的尺寸
    plt.figure(figsize = (10, 6))   # 函数figure()用于制定图表的高度、宽度、分辨率和背景色
    
    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values, c = point_numbers, 
                cmap = plt.cm.Blues, edgecolor = 'none', s = 1)
    
    # 突出起点和终点
    plt.scatter(0, 0, c = 'green', edgecolors = 'none', s = 100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c = 'red',
                edgecolors = 'none', s = 100)
    
    # 隐藏坐标轴
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)
    
    plt.show()
    
    keep_running = input("进行另一次随机漫步吗？(y/n)")
    if keep_running == 'n':
        break