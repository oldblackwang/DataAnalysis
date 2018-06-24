# -*- coding: utf-8 -*-
"""
Created on Thu Jun 21 20:37:18 2018

@author: lenovo
"""

# 骰子根据面数命名，6面为D6
from die import Die
import pygal

# 创建一个D6骰子
die = Die()

# 掷几次骰子，并将结果存储在一个列表中
results = []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)

# 分析结果
frequencies = []    # 存储每种点数出现的次数
for value in range(1, die.num_sides + 1):
    frequency = results.count(value)    # 统计该点数在结果中出现了多少次
    frequencies.append(frequency)

# 对结果进行可视化：绘制直方图
hist = pygal.Bar()

hist.title = "投掷1000次6面骰子的结果"
hist.x_labels = ['1', '2', '3', '4', '5', '6']
hist.x_title = "点数"
hist.y_title = "点数出现的频数"

# 使用add()将一系列值添加到图表中，向它传递要给添加的值指定的标签，和一个包含将出现在
# 图表中的值的列表
hist.add('D6', frequencies) 
hist.render_to_file('die_visual.svg')