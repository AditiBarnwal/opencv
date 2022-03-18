import numpy as np
import cv2 as cv

img = cv.imread('pattern image - Google Search.png')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

corners = cv.goodFeaturesToTrack(gray, 100, 0.01, 10)

corners = np.int0(corners)

for i in corners:
    x, y = i.ravel()
    cv.circle(img, (x, y), 3, [55, 167, 60], -1)

cv.imshow('Shi-Tomasi Corner Detector', img)

cv.waitKey(0)
cv.destroyAllWindows()
