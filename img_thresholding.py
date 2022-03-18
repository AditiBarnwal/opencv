import cv2
import numpy as np
from matplotlib import pyplot as plt

# In THRESHOLDING image shd be in grayscale image
# Thresholding is a technique in OpenCV, which is the assignment of
# pixel values in relation to the threshold value provided.

# In thresholding, each pixel value is compared with the threshold value.
# If the pixel value is smaller than the threshold, it is set to 0, otherwise,
# it is set to a maximum value (generally 255).


# if u want to know how methods are working then first apply on gradient image.
# u will understand the difference through that.
img = cv2.imread('black and white image - Google Search.png', 0)
# thresholding technique
# going to define two variables becoz the result of thresholding gives two result
# one is ret value and other is threshold add value of an image
_, th1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
_, th2 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)
_, th3 = cv2.threshold(img, 127, 255, cv2.THRESH_OTSU)
_, th4 = cv2.threshold(img, 127, 255, cv2.THRESH_TRUNC)
_, th5 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)

cv2.imshow('image', img)
cv2.imshow('th1', th1)
cv2.imshow('th2', th2)
cv2.imshow('th3', th3)
cv2.imshow('th4', th4)
cv2.imshow('th5', th5)

# OR in this form u can display images
# titles = ['image', 'binary', 'binary_inv', 'otsu', 'trunc', 'tozero']
# images = [img, th1, th2, th3, th4, th5]
# for i in range range(6):
#     plt.subplot(2, 3, i+1), plt.imshow(images[i], 'gray')
#     plt.title(titles[i])
#     plt.xticks([]), plt.yticks([])

#     plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
