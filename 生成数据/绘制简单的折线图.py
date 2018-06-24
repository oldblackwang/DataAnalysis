# -*- coding: utf-8 -*-
"""
Created on Tue Jun 19 14:40:10 2018
使用plot()绘制简单的折线图
@author: lenovo
"""

import matplotlib.pyplot as plt  # 模块pyplot包含了很多用于生成图标的函数

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]
plt.plot(input_values, squares, linewidth = 5)    # linewidth决定绘制线条的粗细

# 设置图标主题，并给坐标轴加上标签
plt.title("Square Numbers", fontsize = 24)  # 给图表制定标题
plt.xlabel("Value", fontsize = 14)  # 为x轴设置标题
plt.ylabel("Square of Value", fontsize = 14)

# 设置刻度标记的大小
plt.tick_params(axis = 'both', labelsize = 14)

plt.show()