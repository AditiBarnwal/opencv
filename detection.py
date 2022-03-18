

import numpy as np
import cv2 as cv
img = cv.imread('balls images - Google Search.png')
output = img.copy()
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
gray = cv.medianBlur(gray, 5)
circles = cv.HoughCircles(gray, cv.HOUGH_GRADIENT, 1, 20,
                          param1=50, param2=30, minRadius=0, maxRadius=0)


 #   YET NOT DONE



cv.imshow('output', output)
cv.waitKey(0)
cv.destroyAllWindows()