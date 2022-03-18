#  Adaptive thresholding is the method where the threshold value is
#  calculated for smaller regions and therefore,
#  there will be different threshold values for different regions.

import cv2
import numpy as np

img = cv2.imread("black and white image - Google Search.png", 0)
_, th1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
# 2 types of adaptive
th2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
th3 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

cv2.imshow('image', img)
cv2.imshow('th1', th1)
cv2.imshow('th2', th2)
cv2.imshow('th3', th3)

cv2.waitKey(0)
cv2.destroyAllWindows()
