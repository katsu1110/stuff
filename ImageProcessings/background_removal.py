# -*- coding: utf-8 -*-
"""
Created on Sat Jan 20 11:00:40 2018

@author: katsuhisa
based on 
http://www.codepasta.com/site/vision/segmentation/
"""

import numpy as np
import cv2

img = cv2.imread(r'C:\Users\katsuhisa\Documents\shukatsu\picture3.png')

# noise removal
blurred = cv2.GaussianBlur(img, (5,5),0) 

# edge detection
def edgedetect(channel):
    sobelX = cv2.Sobel(channel, cv2.CV_16S, 1, 0)
    sobelY = cv2.Sobel(channel, cv2.CV_16S, 0, 1)
    sobel = np.hypot(sobelX, sobelY)    
    sobel[sobel > 255] = 255
    return sobel

edgeimg = np.max(np.array([edgedetect(blurred[:,:,0]),
                                      edgedetect(blurred[:,:,1]),
                                      edgedetect(blurred[:,:,2])]), axis=0)

# further noise reduction
edgeimg[edgeimg <= np.mean(edgeimg)] = 0

# contour detection
def findSignificantContours (img, edgeimg):
    image, contours, heirarchy = cv2.findContours(edgeimg, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # Find level 1 contours
    level1 = []
    for i, tupl in enumerate(heirarchy[0]):
        # Each array is in format (Next, Prev, First child, Parent)
        # Filter the ones without parent
        if tupl[3] == -1:
            tupl = np.insert(tupl, 0, [i])
            level1.append(tupl)
    
    # From among them, find the contours with large surface area.
    significant = []
    tooSmall = edgeimg.size * 5 / 100 # If contour isn't covering 5% of total area of image then it probably is too small
    for tupl in level1:
        contour = contours[tupl[0]];
        area = cv2.contourArea(contour)
        if area > tooSmall:
            significant.append([contour, area])

            # Draw the contour on the original image
            cv2.drawContours(img, [contour], 0, (0,255,0),2, cv2.LINE_AA, maxLevel=1)

    significant.sort(key=lambda x: x[1])
    #print ([x[1] for x in significant])
    return [x[0] for x in significant]

edgeimg_8u = np.asarray(edgeimg, np.uint8)
contours = findSignificantContours(img, edgeimg_8u)

# mask
mask = edgeimg.copy()
mask[mask > 0] = 0
cv2.fillPoly(mask, contours, 255)

# invert mask
mask = np.logical_not(mask)

# white the background
img[mask] = 255

# plot image
cv2.imshow('Image',img)

