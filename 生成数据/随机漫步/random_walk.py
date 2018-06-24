# -*- coding: utf-8 -*-
"""
Created on Tue Jun 19 15:48:19 2018
 为模拟随机漫步，我们创建一个名为RandomWalk的类，它随机地选择前进方向。这个类需要三个
属性，其中一个是存储随机漫步次数的变量，其他两个是列表，分别存储随机漫步经过的每个点的
x和y坐标
@author: lenovo
"""

from random import choice  # 每次决策时都使用choice()来决定使用哪种选择

class RandomWalk():
    """一个生成随机漫步的类"""
    
    def __init__(self, num_points = 5000):  # 随机漫步包含的默认点数为5000
        """初始化随机漫步的属性"""
        self.num_points = num_points
        
        # 所有随机漫步都始于(0, 0)
        self.x_values = [0]  # 存储x值
        self.y_values = [0]  # 存储y值
    
    def fill_walk(self):
        """计算随机漫步包含的所有点"""
        
        # 不断漫步，直到列表达到指定的长度
        while len(self.x_values) < self.num_points:
            # 决定前进方向以及沿这个方向前进的距离
            x_step = self.get_step()
            y_step = self.get_step()
            
            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance
            
            # 拒绝原地踏步
            if x_step == 0 and y_step == 0:
                continue
            
            #  计算下一个点的x和y值
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step
            
            self.x_values.append(next_x)
            self.y_values.append(next_y)
        
    def get_step(self):
        """沿指定方向走指定距离"""
        x_direction = choice([1, -1])   # 选择1或-1决定向右走或向左走
        x_distance = choice([0, 1, 2, 3, 4])    # 走的距离绝对值
        x_step = x_direction * x_distance   # 沿指定方向走指定距离
        return x_step
        