# 如何加载位图
import pygame
import math
import time


# 1、 pygame 常用的数学函数
# 角度和弧度转换的函数
# math.degress()  math.radians()  用法很简单，只要将 数值传入
# math.cos(angle), math.sin(angle)  angle 表示弧度，因此首先需要将角度用 math.redians()转变为弧度

from datetime import datetime
today = datetime.today()

# print(today.time())
# print(today.date())
# print(datetime.today().time())
# datetime.today().time() Time有很多属性，Time.hour Time.minute Time.second  Time.microsecond,看名字就知道是什么了。

# 2、 Pygame中加载位图，绘制位图
#    加载位图
# pygame.image.load()   # 支持jpg,png,gif,bmp,pcx,tif,tga等多种图片格式


# space = pygame.image.load("C:/Users/v_xmzqwang/Desktop/微信图片_20191018145316.jpg").convert_alpha()

# convert_alpha()方法会使用透明的方法绘制前景对象，因此在加载一个有alpha通道的素材时（比如PNG TGA），需要使用convert_alpha()方法，当然普通的图片也是可以使用这个方法的，用了也不会有什么副作用。

# 绘制位图
# screen.blit(space, (0, 0))


import sys
import random
import math
import pygame
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('星空')

img = pygame.image.load("image/space.png")

plane = pygame.image.load('image/earth.jpg').convert()
plane.set_colorkey((255, 255, 255), RLEACCEL)
width, height = plane.get_size()


# super_man = pygame.image.load('image/superman.jpg').convert()
# super_man = pygame.transform.smoothscale(super_man, (width//2, height//2))
# super_man.set_colorkey((255, 255, 255), RLEACCEL)


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    keys = pygame.key.get_pressed()
    if keys[K_ESCAPE]:
        sys.exit()

    screen.blit(img, (0, 0))

    screen.blit(plane, (400-width/2, 300-height/2))

    # screen. blit(super_man, (50, 50))

    pygame.display.update()

    time.sleep(1)
    pygame.quit()
    sys.exit()


#  下面绘制一个地球


