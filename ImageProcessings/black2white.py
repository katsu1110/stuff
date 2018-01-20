# -*- coding: utf-8 -*-
"""
Created on Sat Jan 20 12:06:46 2018

@author: katsuhisa
set the black background image to white
"""

import cv2

# my pathes
impath = r'C:\Users\katsuhisa\Documents\shukatsu\picture3.png'
savepath = r'C:\Users\katsuhisa\Documents\shukatsu\picture4.png'

# load image
img = cv2.imread(impath,1)

# black background to white
img[img == 0] = 255

# plot image
cv2.imshow('Gaussian Blurring',img)

# save image
cv2.imwrite(savepath, img)
