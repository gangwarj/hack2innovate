
#import cv2
#import numpy as np
#import copy
#import math
#from appscript import app
from PIL import Image
frame = Image.open('./A-train0001.ppm').convert("L")

frame.save('test1.jpg')
#bgModel = cv2.BackgroundSubtractorMOG2(0, bgSubThreshold)
#fgmask = bgModel.apply(frame)
#res = cv2.bitwise_and(frame, frame, mask=fgmask)




#im.shape

