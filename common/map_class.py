# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: yanghuizhi
# Time: 2020/3/29 5:33 下午

import pygame
from config import setting as cf
# 创建地图类
class Map():
    #3 存储两张不同颜色的图片名称
    map_names_list = [cf.IMAGE_PATH + 'map1.png', cf.IMAGE_PATH + 'map2.png']
    #3 初始化地图
    def __init__(self, x, y, img_index):
        self.image = pygame.image.load(Map.map_names_list[img_index])
        self.position = (x, y)
        # 是否能够种植
        self.can_grow = True
    #3 加载地图
    def load_map(self):
        MainGame.window.blit(self.image,self.position)
