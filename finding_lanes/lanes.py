import cv2
import numpy as np


image = cv2.imread('test_image.jpg')
#cv2.imshow("result",image)
#cv2.waitKey(0)

image_lane = np.copy(image)
gray = cv2.cvtColor(image_lane, cv2.COLOR_RGB2GRAY)
#cv2.imshow("result2",gray)
#cv2.waitKey(0)

blur = cv2.GaussianBlur(gray, (5, 5), 0)

edge = cv2.Canny(blur,50,150) # low_threshold, upper_threshold
cv2.imshow("result3",edge)
cv2.waitKey(0)
