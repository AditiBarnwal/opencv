import cv2
import numpy as np

img1 = cv2.imread("butterfly.png")
img2 = cv2.imread("vector.png")

# for adding two images their size shd be same
# so resizing images in tuple

img1 = cv2.resize(img1, (512, 512))
img2 = cv2.resize(img2, (512, 512))

dst = cv2.add(img1, img2)
# cv2.imshow("image1", img1)
cv2.imshow("image", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
