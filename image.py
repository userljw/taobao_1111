# -*- coding: utf-8 -*-
from PIL import Image, ImageDraw

im01 = Image.open("screencut.png")
Img = im01.convert('L')
Img.save("screencut_gray.png")

# 自定义灰度界限，大于这个值为黑色，小于这个值为白色
threshold = 200

table = []
for i in range(256):
    if i < threshold:
        table.append(0)
    else:
        table.append(1)

# 图片二值化
photo = Img.point(table, '1')
photo.save("screencut_01.png")
