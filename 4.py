# -*- coding: utf-8 -*-
"""
字体模块和错误处理

"""
import pygame
import sys
from pygame.locals import *

# pygame.init()
# screen = pygame.display.set_mode((600, 480), 0, 32)
# pygame.display.set_caption('font')
# bg = pygame.image.load('images/boss_bullet_sun_particle.png')
# #
# # 使用字体模块 -- 避免寒碜
# font = pygame.font.SysFont('arial', 30)
# img = font.render(' I am here !', True, (255, 255, 255))
#
# while True:
#     for event in pygame.event.get():
#         if event.type == QUIT:
#             pygame.quit()
#             sys.exit()
#
#
#     screen.blit(bg, (0, 0))
#     screen.blit(img, (0, 0))
#     pygame.display.update()

# 第一个参数是字体名，第二个是大小，一般来说“Arial”字体在很多系统都是存在的，如果找不到的话，就会使用一个默认的字体，
# 这个默认的字体和每个操作系统相关，你也可以使用pygame.font.get_fonts()来获得当前系统所有可用字体
# 还有一个更好的方法的，使用TTF的方法：
# my_font = pygame.font.Font("my_font.ttf", 16)
# 这个语句使用了一个叫做“my_font.ttf”，这个方法之所以好是因为你可以把字体文件随游戏一起分发，避免用户机器上没有需要的字体。一旦你创建了一个font对象，你就可以使用render方法来写字了，然后就能blit到屏幕上：

# text_surface = my_font.render("Pygame is cool!", True, (0, 0, 0), (255, 255, 255))
# 第一个参数是写的文字；第二个参数是个布尔值: 是否开启抗锯齿，就是说True的话字体会比较平滑，不过相应的速度有一点点影响；第三个参数是字体的颜色；第四个是背景色，如果你想没有背景色（也就是透明），那么可以不加这第四个参数。


# my_name = "Will McGugan"
# import pygame
# pygame.init()
# my_font = pygame.font.SysFont("arial", 64)
# name_surface = my_font.render(my_name, True, (0, 0, 0), (255, 255, 255))
# pygame.image.save(name_surface, "name.png")

"""
显示中文：

用一个可以使用中文的字体，宋体、黑体什么的，或者你直接用中文TTF文件，然后文字使用unicode，即u”中文的文字”这种
最后不要忘了源文件里加上一句关于文件编码的“魔法注释”，具体的可以查一下Python的编码方面的文章。
"""

# font = pygame.font.SysFont('宋体', 30)   # 不显示文字
# # font = pygame.font.SysFont('SimHei', 30)
# text_surface = font.render(u'我出现啦', True, (255, 255, 255))
#
# x = 0
# y = (480 - text_surface.get_height()) / 2
#
# while True:
#     for event in pygame.event.get():
#         if event.type == QUIT:
#             pygame.quit()
#             sys.exit()
#     screen.blit(bg, (0, 0))
#     x -= 2
#     if x < -text_surface.get_width():
#         x = 640 - text_surface.get_width()
#
#     screen.blit(text_surface, (x, y))
#
#     pygame.display.update()

# pygame 的错误处理
# 程序总会出错的，比如当内存用尽的时候Pygame就无法再加载图片，或者文件根本就不存在。再比如下例：
screen = pygame.display.set_mode((640, -1))
# pygame.error: Cannot set negative sized display mode

# 对付：
# try:
#     screen = pygame.display.set_mode(SCREEN_SIZE)
# except pygame.error, e:
#     print("Can't create the display :-(")
#     print(e)
#     exit()