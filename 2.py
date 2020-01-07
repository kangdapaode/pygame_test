"""

理解事件

"""

# 事件是什么，其实从名称来看我们就能想到些什么，而且你所想到的基本就是事件的真正意思了。
# 我们上一个程序，会一直运行下去，直到你关闭窗口而产生了一个QUIT事件，Pygame会接受用户的各种操作（比如按键盘，移动鼠标等）产生事件。
# 事件随时可能发生，而且量也可能会很大，Pygame的做法是把一系列的事件存放一个队列里，逐个的处理。

# 事件检索

# 上个程序中，使用了pygame.event.get()来处理所有的事件，这好像打开大门让所有的人进入。
# 如果我们使用pygame.event.wait()，Pygame就会等到发生一个事件才继续下去，就好像你在门的猫眼上盯着外面一样，来一个放一个……一般游戏中不太实用，
# 因为游戏往往是需要动态运作的；而另外一个方法pygame.event.poll()就好一些，一旦调用，它会根据现在的情形返回一个真实的事件，或者一个“什么都没有”。
# 下表是一个常用事件集：
# QUIT	用户按下关闭按钮	none
# ATIVEEVENT	Pygame被激活或者隐藏	gain, state
# KEYDOWN	键盘被按下	unicode, key, mod
# KEYUP	键盘被放开	key, mod
# MOUSEMOTION	鼠标移动	pos, rel, buttons
# MOUSEBUTTONDOWN	鼠标按下	pos, button
# MOUSEBUTTONUP	鼠标放开	pos, button
# JOYAXISMOTION	游戏手柄(Joystick or pad)移动	joy, axis, value
# JOYBALLMOTION	游戏球(Joy ball)?移动	joy, axis, value
# JOYHATMOTION	游戏手柄(Joystick)?移动	joy, axis, value
# JOYBUTTONDOWN	游戏手柄按下	joy, button
# JOYBUTTONUP	游戏手柄放开	joy, button
# VIDEORESIZE	Pygame窗口缩放	size, w, h
# VIDEOEXPOSE	Pygame窗口部分公开(expose)?	none
# USEREVENT	触发了一个用户事件	code


import pygame
from pygame.locals import *
import sys
#
# pygame.init()
#
# SCREEN_SIZE = (640, 480)
# screen = pygame.display.set_mode((640, 480), 0, 32)
# font = pygame.font.SysFont('arial', 16)
# font_height = font.get_linesize()
# event_text = []
#
# while True:
#     event = pygame.event.wait()
#     event_text.append(str(event))
#     event_text = event_text[-SCREEN_SIZE[1]//font_height:]
#
#     if event.type == QUIT:
#         pygame.quit()
#         sys.exit()
#
#     # screen.fill((255, 255, 255))
#     screen.fill((0, 0, 0))
#     y = 480 - font_height
#
#     for text in reversed(event_text):
#         screen.blit(font.render(text, True, (0, 255, 0)), (0, y))
#         y -= font_height
#
#     pygame.display.update()

# 该程序展示了在移动鼠标时，产生了海量的数据

# ============== 处理鼠标事件
# MOUSEMOTION 事件会在鼠标动的时候发生，它有4个参数
# pos : 鼠标的位置
# rel：代表这次事件和上次鼠标事件的距离
# button：一个包含3个数字的数组，分别代表左中右按键的状态，按下为1
# window

# 类似的还有MOUSEBUTTONDOWN MOUSEBUTTONUP,很多时候，你只需要知道鼠标点下就可以了，那就可以不用上面那个比较强大（也比较复杂）的事件了,它们的参数是：
# button – 看清楚少了个s，这个值代表了哪个按键被操作
# pos – 和上面一样

# ========== 处理键盘事件
# KEYUP KEYDOWN

pygame.init()
screen = pygame.display.set_mode((600, 480))
pygame.display.set_caption('aaaa')
bg = pygame.image.load("images/boss_bullet_sun_particle.png").convert()

x, y = 0, 0
move_x, move_y = 0, 0

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == K_LEFT:
                move_x = -1
            elif event.key == K_RIGHT:
                move_x = 1
            elif event.key == K_UP:
                move_y = -1
            elif event.key == K_DOWN:
                move_y = 1
        elif event.type == KEYUP:
            move_x = 0
            move_y = 0

    x += move_x
    y += move_y
    screen.fill((0, 0, 0))
    screen.blit(bg, (x, y))
    pygame.display.update()


# KEYDOWN和KEYUP的参数描述如下：
#
# key – 按下或者放开的键值，是一个数字，估计地球上很少有人可以记住，所以Pygame中你可以使用K_xxx来表示，比如字母a就是K_a，还有K_SPACE和K_RETURN等。
# mod – 包含了组合键信息，如果mod & KMOD_CTRL是真的话，表示用户同时按下了Ctrl键。类似的还有KMOD_SHIFT，KMOD_ALT。
# unicode – 代表了按下键的Unicode值，

#  ======== 事件过滤
# pygame.event.set_blocked(事件名)  也可以传递列表，如： [KEYUP, KEYDOWN]
# 与之相对的是： pygame.event.set_allowed()


#  产生事件
# 通常玩家做什么，Pygame就会产生相应的事件，不过有时候需要模拟出事件来，比如：录像回放
# 为了产生事件，必须先造一个出来，然后传递
# my_event = pygame.event.Event(KEYDOWN, key=K_SPACE, mod=0, unicode=u'')
# pygame.init()
# screen = pygame.display.set_mode((500, 600))
#
# # my_event = pygame.event.Event(KEYDOWN, {'key': K_SPACE, 'mod': 0, 'unicode': u''})
# # pygame.event.post(my_event)
#
# # 你甚至可以产生一个完全自定义的全新事件，有些高级的话题，暂时不详细说，仅用代码演示一下：
# CATONKEYBOARD = USEREVENT + 1
# myevent = pygame.event.Event(CATONKEYBOARD, message="Bad cat")
#
# for event in pygame.event.get():
#     if event.type == CATONKEYBOARD:
#         print(event.message)
