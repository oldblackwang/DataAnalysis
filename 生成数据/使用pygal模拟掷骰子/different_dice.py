# -*- coding: utf-8 -*-
"""
Created on Fri Jun 22 10:34:26 2018
同时掷两个面数不同的骰子
@author: lenovo
"""

# 骰子根据面数命名，6面为D6
from die import Die
import pygal

# 创建一个D6骰子，一个D10骰子
die_1 = Die()
die_2 = Die(10)

# 掷骰子多次，并将结果存储在一个列表中
results = []
for roll_num in range(50000):
    result = die_1.roll() + die_2.roll()    # 计算每次的总点数
    results.append(result)

# 分析结果
frequencies = []    # 存储每种点数出现的次数
max_result = die_1.num_sides + die_2.num_sides  # 可能出现的最大点数
for value in range(2, max_result + 1):
    frequency = results.count(value)    # 统计该点数在结果中出现了多少次
    frequencies.append(frequency)

# 对结果进行可视化：绘制直方图
hist = pygal.Bar()

hist.title = "投掷1000次一个6面骰子和一个10面骰子的结果"
hist.x_labels = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12',
                 '13', '14', '15', '16']
hist.x_title = "点数"
hist.y_title = "点数出现的频数"

# 使用add()将一系列值添加到图表中，向它传递要给添加的值指定的标签，和一个包含将出现在
# 图表中的值的列表
hist.add('D6 + D10', frequencies) 
hist.render_to_file('different_dice_visual.svg')