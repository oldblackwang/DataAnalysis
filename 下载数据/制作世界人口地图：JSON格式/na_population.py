# -*- coding: utf-8 -*-
"""
Created on Mon Jun 25 13:03:21 2018
创建一幅地图，显示三个北美国家的人口数量
@author: lenovo
"""

import pygal.maps.world

wm = pygal.maps.world.World()
wm.title = 'Populations of Countries in North America'
wm.add('North America', {'ca': 34126000, 'us': 309349000, 'mx': 113423000})

wm.render_to_file('na_populations.svg')