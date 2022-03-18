from matplotlib import pyplot as plt
import cv2
import numpy as np

# REMEMBER: matplotlib reads the image in RGB format,
# OpenCV reads image in BGR format.

img = cv2.imread('butterfly.png', -1)
cv2.imshow('image', img)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

plt.imshow(img)
plt.xticks([]), plt.yticks([])  # gonna hide the tick in matplotlib
plt.show()

cv2.waitKey()
cv2.destroyAllWindows()
