import cv2
import numpy as np

img = cv2.imread("butterfly.png")
# shape returns a tuple of number of rows, column, and channels of image
print(img.shape)
# size returns total no pixels is accessed.
print(img.size)
# dtype returns image data type
print(img.dtype)
# split() is used to split coloured/multi-channel image into separate single-channel images
b, g, r = cv2.split(img)
# merge() is used to merge several single-channel images into a colored/multi-channel image.
img = cv2.merge((b, g, r))

# ||||||
# For ROI: Region of Interest
# first know the coordinate of a portion of an image that you want to filter or operate on.
# find the coordinates Where u want to place
# through mouse click event

# using numpy indexing [give one left corner pt,right corner pt]
# bubble = img[:, :]
# place the above indexing image
# img[:, :] = bubble
# ||||||

cv2.imshow("image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
