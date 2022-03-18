import cv2
import numpy as np


# object tracking through video capture
def nothing(x):
    pass


cap = cv2.VideoCapture(0)
# a named window for tracking which is used for adjusting the lower boundness of hsv colors
# for trackbar
cv2.namedWindow("Tracking")
# lower hue value and next argument is window name then strt and end value and in end callback function.
cv2.createTrackbar("LH", "Tracking", 0, 255, nothing)
cv2.createTrackbar("LS", "Tracking", 0, 255, nothing)  # lower saturation value
cv2.createTrackbar("LV", "Tracking", 0, 255, nothing)   # lower value
cv2.createTrackbar("UH", "Tracking", 255, 255, nothing)  # upper hue value
cv2.createTrackbar("US", "Tracking", 255, 255, nothing)  # upper saturation value
cv2.createTrackbar("UV", "Tracking", 255, 255, nothing)  # upper value

while True:

    _, frame = cap.read()

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    l_h = cv2.getTrackbarPos("LH", "Tracking")  # get trackbar position from LH
    l_s = cv2.getTrackbarPos("LS", "Tracking")
    l_v = cv2.getTrackbarPos("LV", "Tracking")
    u_h = cv2.getTrackbarPos("UH", "Tracking")
    u_s = cv2.getTrackbarPos("US", "Tracking")
    u_v = cv2.getTrackbarPos("UV", "Tracking")

    l_b = np.array([l_h, l_s, l_v])  # once u have the values of lower hue(l_h) and others then provide here
    u_b = np.array([u_h, u_s, u_v])

    mask = cv2.inRange(hsv, l_b, u_b)

    # applying on video capture
    # Bitwise operations are used in image manipulation and used for extracting essential parts in the image
    # in order to apply mask on frame for lower_blue value(l_b) and upper_blue value(u_p)
    res = cv2.bitwise_and(frame, frame, mask=mask)

    # now for windows visible
    cv2.imshow("frame", frame)  # for frame
    cv2.imshow("mask", mask)   # for mask showing
    cv2.imshow("res", res)  # for variable result

    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()

# Yeah!!!! Now play with the trackbar.
