# -*- coding: utf-8 -*-
"""
Created on Tue Feb 21 21:08:36 2017

@author: chenshengkang
"""
from PIL import ImageGrab

#截取图片
bbox = (1040,767,1160,820)
im = ImageGrab.grab(bbox)

#判断验证码类型（1行还是2行）
def imgType(im):
    region = (0,35,120,53)
    cropImg = im.crop(region)
    pix = cropImg.load()
    width = cropImg.size[0]
    height = cropImg.size[1]
    RGBlist = []
    for x in range(width):
        for y in range(height):
            r,g,b=pix[x,y]
            RGBlist.extend([r,g,b])
    colour = 0.0
    for RGB in RGBlist:
        if RGB < 250:
            colour += 1.0
    if colour/len(RGBlist)>0.1:
        imgtype = 2
    else:
        imgtype = 1
    return imgtype
imgType(im)

region = (0,0,20,26)
cropImg = im.crop(region)
cropImg.show()
region = (0,24,22,50)
cropImg = im.crop(region)
cropImg.show()

region = (20,0,40,26)
cropImg = im.crop(region)
cropImg.show()
region = (20,24,40,50)
cropImg = im.crop(region)
cropImg.show()

region = (38,0,60,26)
cropImg = im.crop(region)
cropImg.show()
region = (38,24,60,50)
cropImg = im.crop(region)
cropImg.show()

region = (58,0,75,26)
cropImg = im.crop(region)
cropImg.show()
region = (58,24,75,50)
cropImg = im.crop(region)
cropImg.show()

region = (75,0,92,26)
cropImg = im.crop(region)
cropImg.show()
region = (75,24,92,50)
cropImg = im.crop(region)
cropImg.show()

region = (92,0,110,26)
cropImg = im.crop(region)
cropImg.show()
region = (92,24,110,50)
cropImg = im.crop(region)
cropImg.show()

xregion = [[0,20],[0,22],[38,60],[58,75],[75,92],[92,110]
yregion = []
'''
通过RGBlist RGB信息分类颜色种类
提出颜色占位小于？%的数字
计算位置信息返回出对应位置的图片占位符
'''

'''
im.show()
import os 
fr = open('C:\\Users\\chenshengkang\\Desktop\\1.png')

bits = map(numberToBinary,range(256))

all = fr.readlines()

for b in all:
    print b
'''