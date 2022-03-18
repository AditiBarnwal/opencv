# Morphological transformations are some simple operations based on the image shape.

# performed on binary images
# when we apply ths morphological transformation two things are required
# 1. original image
# 2. structuring element called as kernel(which decides the nature of the operation
# KERNEL:: tells how to change the value of any given pixel by
#          combining it with different amounts of neighboring pixels


import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('butterfly.png', cv2.IMREAD_GRAYSCALE)
_, mask = cv2.threshold(img, 220, 255, cv2.THRESH_BINARY_INV)

kernal = np.ones((5, 5), np.uint8)

dilation = cv2.dilate(mask, kernal, iterations=2)
erosion = cv2.erode(mask, kernal, iterations=1)
opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernal)
closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernal)
morphgra = cv2.morphologyEx(mask, cv2.MORPH_GRADIENT, kernal)
morphth = cv2.morphologyEx(mask, cv2.MORPH_TOPHAT, kernal)

titles = ['image', 'mask', 'dilation', 'erosion', 'opening', 'closing', 'morphgra', 'morphth']
images = [img, mask, dilation, erosion, opening, closing, morphgra, morphth]

for i in range(8):
    plt.subplot(2, 4, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()
