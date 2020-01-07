import pygame
import sys


# 引入pygame中的所有常量
from pygame.locals import *

#  初始化pygame
# pygame.init()
#
# #  创建一个窗口，与程序进行交互
# screen = pygame.display.set_mode((600, 500))
#
# #  1、打印字体
# myfont = pygame.font.Font(None, 60)
# white = 255, 255, 255
# blue = 0, 0, 200
# textImage = myfont.render("焦若拙臭弟弟", True, white)
# screen.fill(blue)
# screen.blit(textImage, (100,100))
# # pygame.display.update()

# import pygame
# from pygame.locals import *
# import sys
#
#
# white = 255, 255, 255
# pygame.init()
# screen = pygame.display.set_mode((600,500))
#
# myfont = pygame.font.SysFont('SimHei', 60)
# textImage = myfont.render(""" 若若 铸铸 雪雪""", True, white)
# while True:
#     for event in pygame.event.get():
#         if event.type in (QUIT, KEYDOWN):
#            sys.exit()
#     screen.fill((150, 40, 50))
#     screen.blit(textImage, (100, 100))
#     pygame.display.update()


# 2、 pygame的事件
# 可以处理游戏中的任何事件
# QUIT,ACTIVEEVENT,KEYDOWN,KEYDOWN,MOUSEMOTION,MOUSEBUTTONUP,MOUSEBUTTONDOWN,JOYAXISMOTION,JOYBALLMOTION,JOYHATMOTION........   http://www.pygame.org/docs/index.html

# 实时事件循环

# while True:
#     for event in pygame.event.get():
#         if event.type == QUIT:
#             pygame.quit()
#             sys.exit()

#  键盘事件
#  最典型的就是keyup 和 keydown ，当按键按下时响应keydown事件，通常可以设置一个事件变量，然后根据keyup  和  keydown 给它赋值
# while True:
#     for event in pygame.event.get():
#         if event.type == QUIT:
#             pygame.quit()
#         elif event.type == KEYDOWN:
#             key_flag = True
#         elif event.type == KEYUP:
#             key_flag = False
#         else:
#             pass


#  默认的话， pygame不会重复的响应一个一直被按住的键，只是在第一下响应一次
# 如有需要(一个以毫秒为单位的值)：
# pygame.key.set_repeat(10)

# 鼠标事件
# MOUSEMOTION, MOUSEBUTTONDOWN, MOUSEBUTTONUP, MOUSEWHEEL
# for event in pygame.event.get():
#     if event.type == MOUSEMOTION:
#         mouse_x, mouse_y = event.pos
#         move_x, move_y = event.rel

# 设备轮询
# 除了pygame事件，还可以用设备轮询来检验是否有事件发生，而且在python里是没有switch语句的，因此处理事件过多时，if else 难以满足
# 1、 轮询键盘
# 在 pygame 中，使用pygame.key.get_pressed()来轮询键盘接口，这个方法会返回布尔值的列表，其中每个键一个标志，使用键常量值来匹配按键，不必遍历时间系统便可以自动检测多个按键的按下。

# keys = pygame.key.get_pressed()
# if keys[K_ESCAPE]:
#     pygame.quit()
#     sys.exit()

# 设计一个打字测速小游戏来综合练习一下键盘的轮询

import sys, random, pygame, time
from pygame.locals import *

def print_text(font, x, y, text, color=(255, 255, 255)):
    imgtxt = font.render(text, True, color)
    screen.blit(imgtxt, (x, y))

#  主程序
pygame.init()  # 初始化
screen = pygame.display.set_mode((600, 500))
pygame.display.set_caption("Keyboard Demo")
font1 = pygame.font.Font(None, 24)
font2 = pygame.font.Font(None, 200)
white = 255, 255, 255
yellow = 255, 255, 0
color = 125, 100, 210

key_flag = False
correct_answer = 97
seconds = 10
score = 0
clock_start = 0
game_over = True

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            key_flag = True
        elif event.type == KEYUP:
            KEY_FLAG = False
    keys = pygame.key.get_pressed()
    if keys[K_ESCAPE]:
        sys.exit()

    if keys[K_RETURN]:
        if game_over:
            game_over = False
            score = 0
            seconds = 11
            clock_start = time.clock()

    current = time.clock() - clock_start
    speed = score * 6
    if seconds - current < 0:
        game_over = True
    elif current <= 10:
        if keys[correct_answer]:
            correct_answer = random.randint(97, 122)
            score += 1

    # 清屏
    screen.fill(color)
    print_text(font1, 0, 20, 'try to keep up for 10 seconds...')

    if key_flag:
        print_text(font1, 450, 0, 'you are keying...')

    if not game_over:
        print_text(font1, 0, 80, ' Time :' + str(int(seconds - current)))

    print_text(font1, 0, 100, 'Speed:' + str(speed) + 'letters/min')

    if game_over:
        print_text(font1, 0, 160, 'press enter to start...')

    print_text(font2, 0, 240, chr(correct_answer - 32), yellow)

    # 更新
    pygame.display.update()

#  Random.randint(x,y);看名字知道这个函数的作用了，它可以返回一个x~y之间的随机数。
# 另外一个模块是time。time.clock()函数会返回从程序启动到现在为止的时间。

# 2. 轮询鼠标
# 同样我们可以使用类似的方法去轮询鼠标事件
# 设立有3个相关函数
# （1）、pygame.mouse.get_pos()
# （2）、 pygame.mouse.get_rel()
#         rel_x, rel_y = pygame.mouse.get_rel()
# （3）、 btn_one, btn_two, btn_three = pygame.mouse.get_pressed()
# 利用这个函数， 可以获取鼠标按钮的状态， 比如当左键按下的时候btn_one的值会被赋予1，鼠标按键弹起时赋予0

# 同样可以自己设计一个小安利来熟悉鼠标轮询，比如当鼠标按下的时候打印按下的是鼠标左键还是右键，鼠标的点击位置，鼠标当前的坐标等

import time
pygame.init()
screen = pygame.display.set_mode((600, 500))    # 设置大小
pygame.display.set_caption("guess mouse")   # 命名
font = pygame.font.Font(None, 24)

white = 255, 255, 255
yellow = 255, 255, 0
color = 125, 100, 210
game_over = False
key_flag = False
chances = 10

is_up = {
    1: 'down',
    0: 'up'
}


def print_text(font, x, y, text, color=(255, 255, 255)):
    img_txt = font.render(text, True, color)
    screen.blit(img_txt, (x, y))

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == MOUSEBUTTONDOWN:
            key_flag = True
        elif event.type == MOUSEBUTTONUP:
            key_flag = False
    btn_1, btn_2, btn_3 = pygame.mouse.get_pressed()
    mouse_x, mouse_y = pygame.mouse.get_pos()
    # rel_x, rel_y = pygame.mouse.get_rel()

    screen.fill(color)
    chances -= 1
    if chances == 0:
        game_over = True

    print_text(font, 0, 24, 'The location of mouse is: (%s, %s)' % (mouse_x, mouse_y))
    if key_flag:
        print_text(font, 0, 50, 'left mouse %s  | middle mouse %s  |  right mouse %s' % (is_up[btn_1], is_up[btn_2], is_up[btn_3]))
        # print_text(font, 0, 100, 'last click location: (%s, %s)' % (rel_x, rel_y))

    # if game_over:
    #     print_text(font, 0, 160, 'GAME OVER...')
    #     sys.exit()
    pygame.display.update()






