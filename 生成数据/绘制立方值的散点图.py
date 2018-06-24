# -*- coding: utf-8 -*-
"""
Created on Tue Jun 19 15:26:26 2018
绘制立方值的散点图
@author: lenovo
"""

import matplotlib.pyplot as plt

x_values = list(range(1, 5001))
y_values = [x ** 3 for x in x_values]
plt.scatter(x_values, y_values, c = y_values, cmap = plt.cm.Reds, 
            edgecolor = 'none', s = 40)
# s为点大小，edgecolor为点轮廓颜色，c为点颜色
# 参数cmap告诉pyplot使用哪个颜色映射。此处将y较小的点设置为浅蓝色，较大的为深蓝色

# 设置图表标题并给坐标轴加上标签
plt.title("Cubes of values", fontsize = 24)
plt.xlabel("Value", fontsize = 14)
plt.ylabel("Cube of Value", fontsize = 14)

# 设置刻度标记的大小
plt.tick_params(axis = 'both', which = 'major', labelsize = 14)

# 设置每个坐标轴的取值范围
plt.axis([0, 6100, 0, 136000000000])

# 保存图表为文件，第一个参数为文件名，第二个参数将图标多余的空白区域裁剪掉
plt.savefig("cubes_plot.png", bbox_inches = 'tight')