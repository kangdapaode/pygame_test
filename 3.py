"""

显示窗口

"""
import pygame
from pygame.locals import *
import sys


# 将第二个参数设置为 FULLSCREEN时， 显示全屏窗口

# screen = pygame.display.set_mode((600, 480), FULLSCREEN, 32)

# 注意：如果你的程序有什么问题，很可能进入了全屏模式就不太容易退出来了，所以最好先用窗口模式调试好，再改为全屏模式。

#  切换屏显方式
# pygame.init()
#
# screen = pygame.display.set_mode((640, 480), 0, 32)
# pygame.display.set_caption('fullscreen')
# FULLScreen = False
# bg = pygame.image.load("images/timg.jpg").convert()
# while True:
#     for event in pygame.event.get():
#         if event.type == QUIT:
#             pygame.quit()
#             sys.exit()
#         if event.type == KEYDOWN:
#             if event.key == K_f:
#                 FULLScreen = not FULLScreen
#             if FULLScreen:
#                 screen = pygame.display.set_mode((600, 480), FULLSCREEN, 32)
#             else:
#                 screen = pygame.display.set_mode((600, 480), 0, 32)
#             screen.fill((0, 0, 0))
#     pygame.display.update()

#  可变尺寸的显示
# pygame默认窗口不能通过拖动来改变大小，可通过如下程序修改：
pygame.init()
screen = pygame.display.set_mode((600, 480))
pygame.display.set_caption('修改窗口')
bg = pygame.image.load("images/bg.jpg").convert()

while True:
    event = pygame.event.wait()
    if event.type == QUIT:
        pygame.quit()
        sys.exit()
    if event.type == VIDEORESIZE:
        SCREEN_SIZE = event.size
        screen = pygame.display.set_mode(SCREEN_SIZE, RESIZABLE, 32)
        pygame.display.set_caption('resized to ' + str(SCREEN_SIZE))

        screen_width, screen_height = SCREEN_SIZE
        for y in range(0, screen_height, bg.get_height()):
            for x in range(0, screen_width, bg.get_width()):
                screen.blit(bg, (x, y))
    pygame.display.update()

# 修改大小后，后端控制台会显示出新的尺寸
#  事件： VIDEORESIZE， 包含：
# size -- 二维数组， 值为更改后的窗口尺寸 size[0] 为宽 size[1]为高
# w  -- 宽
# h  -- 高

#  其他复合模式
# 一般来说窗口就用0全屏就用FULLSCREEN

# 如果你想创建一个硬件显示（surface会存放在显存里，从而有着更高的速度），你必须和全屏一起使用：

# screen = pygame.display.set_mode((6000, 480), HWSURFACE | FULLSCREEN, 32)

# 当然你完全可以把双缓冲（更快）DOUBLEBUF也加上，使用pygame.display.flip()来刷新显示, 是交替显示的
# pygame.display.update()是将数据画到前面显示

# 双缓冲 ：
# 出黑板报， 如果我有两块黑板，那么可以挂一块给别人看，我自己在底下写另一块，
# 写好了把原来的换下来换上新的，这样一来别人基本总是看到完整的内容了。
# 双缓冲就是这样维护两个显示区域，快速的往屏幕上换内容，而不是每次都慢慢地重画

# 还有OPENGL模式，这是一个得到广泛应用的3D加速显示模式。不过一旦使用了这个模式，pygame中的2D图像函数就不能用了，我们会在以后讲详细的内容。