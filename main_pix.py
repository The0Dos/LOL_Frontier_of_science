
import cv2
import colorsys
from matplotlib import pyplot as plt
import operator
from PIL import Image
import numpy as np

im = Image.open('dab1.jpg')
pix = im.load()
print(im.size)

i = 0
y = 0
vosem = 1600
tis = 1200
green_count = 0
brown_count = 0

for i in range(0, 800) :
    for y in range(0, 1000):
        a, b, c = pix[i, y]

        if  b == 255:
            print("green")
            green_count+= 1

        y+= 1
    i+= 1

print("Зеленых пикселей на первом фото: ", green_count)
print("Коричневых пикселей на первом фото: ", brown_count)

if brown_count != 0:
    coef_1 = green_count / brown_count
else:
    coef_1 = green_count / 0.1

i1 = 0
y1 = 0
green_count1 = 0
brown_count1 = 0

im = Image.open('dab2.jpg')
pix = im.load()


for i1 in range(0, 800) :
    for y1 in range(0, 1000):
        a, b, c = pix[i1, y1]

        if  b == 255:
            print("green")
            green_count1+= 1
        elif a == 128:
            print("brown")
            brown_count1 += 1

        y1+= 1
    i1+= 1

print("Зеленых пикселей на первом фото: ", green_count)
print("Коричневых пикселей на первом фото: ", brown_count)

print("Зеленых пикселей на втором фото: ", green_count1)
print("Коричневых пикселей на втором фото: ", brown_count1)

coef_2 = green_count1/brown_count1
result = (coef_1 / coef_2) / (1600 * 1200)
print(result)

if result - 1.5 != 0:
    print("Вырубка леса")








    




    








