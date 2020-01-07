"""
图像化：视觉体验

"""
import pygame
from pygame.locals import *
import sys

#  ============== 像素的威力
# 图像是由一个一个点构成的，这就是像素，屏幕分辨率如：1280 * 1024 就是由1310270个像素构成的，每个像素可以显示16.7万种颜色

# pygame.init()
# screen = pygame.display.set_mode((640, 480))
# all_colors = pygame.Surface((4096, 4096), depth=24)


# rgb取值0~255就不说了，主要是x和y坐标。
# 我们希望用r来分隔每个小方格（即一个小方格里的r是相同的），小方格的填法事先水平填满，再起一行，直到完成。
# 那么小方格起始坐标就需要，x从0、256、512…到3840后重新开始，y则是0、0、0（16遍）、256、256、256（16遍）…直到结束。两个位操作就是来做这个的，你可以把x和y的值打出来看看。
# for r in range(256):
#     print(r + 1, 'out of 256')
#     x = (r & 15) * 256
#     y = (r >> 4) * 256
#     for g in range(256):
#         for b in range(256):
#             all_colors.set_at((x + g, y + b), (r, g, b))
# pygame.image.save(all_colors, 'images/all_color.bmp')


#  =============== 色彩的威力
# 李涛的PhotoShop讲座吧，VeryCD上有下的，讲的还是很清楚的

# pygame.init()
# screen = pygame.display.set_mode((640, 480), 0, 32)
#
# def create_scales(height):
#     red_scale_furface = pygame.surface.Surface((640, height))
#     green_scale_furface = pygame.surface.Surface((640, height))
#     blue_scale_furface = pygame.surface.Surface((640, height))
#     for x in range(640):
#         c = int((x / 640)*255)
#         red = (c, 0, 0)
#         green = (0, c, 0)
#         blue = (0, 0, c)
#         line_rect = Rect(x, 0, 1, height)
#         pygame.draw.rect(red_scale_furface, red,  line_rect)
#         pygame.draw.rect(green_scale_furface, green, line_rect)
#         pygame.draw.rect(blue_scale_furface, blue, line_rect)
#     return red_scale_furface, green_scale_furface, blue_scale_furface
#
# red_scale, green_scale, blue_scale = create_scales(80)
# color = [127, 127, 127]
# while True:
#
#     for event in pygame.event.get():
#         if event.type ==QUIT:
#             pygame.quit()
#             sys.exit()
#     screen.fill((0, 0, 0))
#     screen.blit(red_scale, (0, 00))
#     screen.blit(green_scale, (0, 80))
#     screen.blit(blue_scale, (0, 160))
#     x, y = pygame.mouse.get_pos()
#     if pygame.mouse.get_pressed()[0]:
#         for component in range(3):
#             if y > component * 80 and y  < (component + 1 ) * 80:
#                 color[component] = int((x/639) * 255)
#         pygame.display.set_caption('pygame color test - ' + str(tuple(color)))
#
#     for component in range(3):
#         pos = (int((color[component]/255) * 639), component * 80 + 40)
#         pygame.draw.circle(screen, (255, 255, 255), pos, 20)
#     pygame.draw.rect(screen, tuple(color), (0, 240, 640, 240))
#     pygame.display.update()

# 在这个例子里，你可以用鼠标移动三个白点，代表了三原色的量，下面就是不同混合得到的结果，在标题上你可以看到RGB三个数值。
#
# ======== 颜色的缩放

# 当我们有了一个颜色，比如说一颗流星划过天际，那么那个时候它是个“火球般的橘黄色”，不过一旦它着地了，它就会灭掉，慢慢变暗，如何能找到比这个“火球般的橘黄色”更暗的颜色？

# 把颜色的RGB每一个数值乘以一个小于1的正小数，颜色看起来就会变暗了（记住RGB都是整数所以可能需要取整一下）

# 很自然的可以想到，如果乘以一个大于1的数，颜色就会变亮，
# 不过同样要记住每个数值最多255，所以一旦超过，你得把它归为255！
# 使用Python的内置函数min，你可以方便的做到这事情，也不多说了。如果你乘的数字偏大，颜色很容易就为变成纯白色，就失去了原来的色调。
# 而且RGB也不可能是负数，所以谨慎选择你的缩放系数！

# 颜色的混合
# 很多时候我们还需要混合颜色，比如一个僵尸在路过一个火山熔岩坑的时候，它会由绿色变成橙红色，再变为正常的绿色，这个过程必须表现的很平滑，这时候我们就需要混合颜色。

# 我们用一种叫做“线性插值(linear interpolation)”的方法来做这件事情。
# 为了找到两种颜色的中间色，我们将这第二种颜色与第一种颜色的差乘以一个0~1之间的小数，然后再加上第一种颜色就行了。
# 如果这个数为0，结果就完全是第一种颜色；是1，结果就只剩下第二种颜色；中间的小数则会皆有两者的特色。

screen = pygame.display.set_mode((640, 480), 0, 32)
color_1 = (221, 99, 20)
color_2 = (96, 130, 51)
factor = 0

def blend_color(color_1, color_2, blend_factor):
    r1, g1,  b1 = color_1
    r2, g2,  b2 = color_2
    r = r1 + (r2 - r1) * blend_factor
    g = g1 + (g2 - g1) * blend_factor
    b = b1 + (b2 - b1) * blend_factor
    return int(r), int(g), int(b)

while True:

    for event in pygame.event.get():
        if event.type ==  QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((255, 255, 255))
    tri = [(0, 120), (639, 100), (639, 140)]
    pygame.draw.polygon(screen, (0, 255, 0), tri)
    pygame.draw.circle(screen, (0, 0, 0), (int(factor * 639.0), 120), 10)
    x, y = pygame.mouse.get_pos()
    if pygame.mouse.get_pressed()[0]:
        factor = x / 639.0
        pygame.display.set_caption('pygame color blend test - %.3f'%factor)

    color = blend_color(color_1, color_2, factor)
    pygame.draw.rect(screen, color, (0, 240, 640, 240))

    pygame.display.update()

