# -*- coding: utf-8 -*-
"""
Created on Mon Jun 25 12:52:00 2018
创建一个突出北美、中美、南美的简单地图
@author: lenovo
"""

import pygal.maps.world

wm = pygal.maps.world.World()
wm.title = 'North, Central, and South America'

# 方法add()接受一个标签和一个列表，后者包含我们要突出的国家的国别码
wm.add('North America', ['ca', 'mx', 'us'])
wm.add('Central America', ['bz', 'cr', 'gt', 'hn', 'ni', 'pa', 'sv'])
wm.add('South America', ['ar', 'bo', 'br', 'cl', 'co', 'ec', 'gf', 
                         'gy', 'pe', 'py', 'sr', 'uy', 've'])

wm.render_to_file('americas.svg')