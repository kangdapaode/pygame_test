import pygame

# pygame.cdrom	访问光驱
# pygame.cursors	加载光标
# pygame.display	访问显示设备
# pygame.draw	绘制形状、线和点
# pygame.event	管理事件
# pygame.font	使用字体
# pygame.image	加载和存储图片
# pygame.joystick	使用游戏手柄或者 类似的东西
# pygame.key	读取键盘按键
# pygame.mixer	声音
# pygame.mouse	鼠标
# pygame.movie	播放视频
# pygame.music	播放音频
# pygame.overlay	访问高级视频叠加
# pygame	就是我们在学的这个东西了……
# pygame.rect	管理矩形区域
# pygame.sndarray	操作声音数据
# pygame.sprite	操作移动图像
# pygame.surface	管理图像和屏幕
# pygame.surfarray	管理点阵图像数据
# pygame.time	管理时间和帧信息
# pygame.transform	缩放和移动图像

if pygame.font is None:
    print("The font module is not available!")
    exit()


from pygame.locals import *
import sys

pygame.init()

screen = pygame.display.set_mode((640,  480))
pygame.display.set_caption('hello world')

background = pygame.image.load('images/timg.jpg').convert()
img = pygame.image.load('images/boss_bullet_sun_particle.png').convert_alpha()


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    screen.blit(background, (0, 0))

    x, y = pygame.mouse.get_pos()
    x -= img.get_width()
    y -= img.get_height()

    screen.blit(img, (x, y))
    pygame.display.update()


# set_mode 会返回一个Surface对象， 代表了在桌面上出现的窗口，参数为 （元组（代表分辨率）， 标志位， 色深）
# 标志位	功能
# FULLSCREEN	创建一个全屏窗口
# DOUBLEBUF	创建一个“双缓冲”窗口，建议在HWSURFACE或者OPENGL时使用
# HWSURFACE	创建一个硬件加速的窗口，必须和FULLSCREEN同时使用
# OPENGL	创建一个OPENGL渲染的窗口
# RESIZABLE	创建一个可以改变大小的窗口
# NOFRAME	创建一个没有边框的窗口

# convert函数是将图像数据都转化为Surface对象，每次加载完图像以后就应该做这件事件（事实上因为 它太常用了，如果你不写pygame也会帮你做）；
# convert_alpha相比convert，保留了Alpha 通道信息（可以简单理解为透明的部分），这样我们的光标才可以是不规则的形状。

# 游戏的主循环是一个无限循环，直到用户跳出。在这个主循环里做的事情就是不停地画背景和更新光标位置，虽然背景是不动的，我们还是需要每次都画它， 否则鼠标覆盖过的位置就不能恢复正常了。

# blit是个重要函数，第一个参数为一个Surface对象，第二个为左上角位置。画完以后一定记得用update更新一下，否则画面一片漆黑。

