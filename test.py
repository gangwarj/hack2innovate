import numpy as np
import cv2
import colorsys
image = cv2.imread('test.jpg')
image_hsv = colorsys.rgb_to_hsv(0.2, 0.4, 0.4)
cv2.imwrite('asdfgh.jpg',image_hsv)

