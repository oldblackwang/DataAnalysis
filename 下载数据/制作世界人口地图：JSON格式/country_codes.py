# -*- coding: utf-8 -*-
"""
Created on Sun Jun 24 20:28:22 2018

@author: lenovo
"""

from pygal_maps_world.i18n import COUNTRIES    # 字典COUNTRIES包含的键和值分别为两个字母的国别码和国家名

def get_country_code(country_name):
    """根据指定的国家，返回Pygal使用的两个字母的国别码"""
    for code, name in COUNTRIES.items():
        if name == country_name:
            return code
    # 如果没有找到指定的国家，就返回None
    return None
    
# print(get_country_code('Andorra'))
# print(get_country_code('United Arab Emirates'))
# print(get_country_code('Afghanistan'))