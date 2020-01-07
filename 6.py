"""
图像
常用RGBA图像， A代表alpha 透明度，0 - 255之间， 0 代表完全透明， 100代表部分透明

这个世界上有很多存储图像的方式（也就是有很多图片格式），比如JPEG、PNG等，Pygmae都能很好的支持，具体支持的格式如下：


JPEG（Join Photograhpic Exper Group)，极为常用，一般后缀名为.jpg或者.jpeg。数码相机、网上的图片基本都是这种格式。这是一种有损压缩方式，尽管对图片质量有些损坏，但对于减小文件尺寸非常棒。优点很多只是不支持透明。
PNG（Portable Network Graphics）将会大行其道的一种格式，支持透明，无损压缩。对于网页设计，软件界面设计等等都是非常棒的选择！
GIF 网上使用的很多，支持透明和动画，只是只能有256种颜色，软件和游戏中使用很少
BMP Windows上的标准图像格式，无压缩，质量很高但尺寸很大，一般不使用
PCX
TGA
TIF
LBM, PBM
XPM
"""

import pygame

#  使用Surface对象
#  对于Pygame，加载图片就是pygame.image.load()，返回一个Surface对象，可以做涂画，变形，复制等操作，事实上屏幕也是一个Surface对象

# 1、创建
# imd = pygame.image.load()  # 这个surface有着和图像相同的尺寸和颜色
bland_surface = pygame.Surface((256, 256))  #创建一个256×256像素的surface
# 如果不指定尺寸，那么就创建和屏幕大小一致的
# 参数：
# 第一个参数是flags:
#     HWSURFACE: 类似于前面讲的，更快，不过最好 不设定，pygame会自己优化
#     SRCALPHA: 有alpha通道的surface，如果你需要透明就需要这个选项，这个选项的使用需要第二个参数为32

# 第二个参数是depth ，和pygame.display.set_mode()中一样，可以不设定，Pygame会自动设的和display一致。不过如果你使用了SRCALPHA，还是设为32吧：
# bland_alpha_surface = pygame.Surface((256, 256), flags=SRCALPHA, depth=32)

# 2、转换Surface
# 通常你不用在意surface里的具体内容，不过也许需要把这些surface转换一下已获得更高的性能
bg = pygame.image.load('./images/bg.jpg').convert()
mouse_cursor = pygame.image.load('./images/boss_bullet_sun_particle.png').convert_alpha()
# 第一个是普通转换，等于display
# 第二句是带alpha通道的转换，如果给convert或者convert_alpha一个surface对象，那么这个会被作为目标来转换

# 矩形对象（Rectangle Objects）
# 矩形是最常见的绘制图形，




