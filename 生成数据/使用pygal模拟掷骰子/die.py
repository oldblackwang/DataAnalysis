# -*- coding: utf-8 -*-
"""
Created on Thu Jun 21 20:30:09 2018

@author: lenovo
"""
from random import randint   # 返回头尾值或这两个值之间的任何整数

class Die():
    """表示一个骰子的类"""
    
    def __init__(self, num_sides = 6):
        """骰子默认为6面"""
        self.num_sides = num_sides
    
    def roll(self):
        """返回一个位于1和骰子面数之间的随机值"""
        return randint(1, self.num_sides)   
