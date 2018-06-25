# -*- coding: utf-8 -*-
"""
Created on Fri Jun 22 10:50:49 2018

@author: lenovo
"""

import csv
from datetime import datetime
from matplotlib import pyplot as plt

# 从文件中获取日期、最低气温和最高气温
filename = 'sitka_weather_2014.csv'  # 阿拉斯加锡特卡天气数据
with open(filename) as f:
    reader = csv.reader(f)  # 创建一个与文件相关联的阅读器对象
                            # reader处理文件中以逗号分隔的第一行数据，并将每项数据都作为一个元素存储在列表中
    header_row = next(reader)   # next()函数，将阅读器对象传递给它时，返回文件中的下一行
                                # 此处为第一行，包含文件头
    
    '''
    for index, column_header in enumerate(header_row):
        """enumerate()来获取每个元素的索引及其值，由此判断日期和最高气温的索引"""
        print(index, column_header)
    '''
    
    dates, highs, lows = [], [], []
    for row in reader:
        """将最高气温转换成数字并存储在列表中"""
        current_date = datetime.strptime(row[0], "%Y-%m-%d")    # 日期索引为0
        dates.append(current_date)
        
        high = int(row[1])  # 最高气温索引为1
        highs.append(high)
        
        low = int(row[3])   # 最低气温索引为3
        lows.append(low)    
    
    # print(highs)
    
    # 根据数据绘制图形
    fig = plt.figure(dpi = 128, figsize = (10, 6))
    plt.plot(dates, highs, c = 'red', alpha = 0.5)  # alpha制定颜色透明度
    plt.plot(dates, lows, c = 'blue', alpha = 0.5)  # 0为完全透明，为完全不透明
    
    # fill_between()接受一个x值系列和两个y值系列，并填充两个y值系列之间的空间
    plt.fill_between(dates, highs, lows, facecolor = 'blue', alpha = 0.1)
    
    # 设置图形格式
    plt.title("Daily high and low temperatures - 2014", fontsize = 24)
    plt.xlabel('', fontsize = 16)
    fig.autofmt_xdate() # 绘制斜的日期标签
    plt.ylabel("Temperature(F)", fontsize = 16)
    plt.tick_params(axis = 'both', which = 'major', labelsize = 16)
    
    plt.savefig('阿拉斯加锡特卡2014年最高气温和最低气温.png', 
                bbox_inches = 'tight')