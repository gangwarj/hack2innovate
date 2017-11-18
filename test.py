import scipy.misc
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

#Pixels higher than this will be 1. Otherwise 0.
THRESHOLD_VALUE = 200

#Load image and convert to greyscale
img = Image.open("test.jpg")
img = img.convert("L")

imgData = np.asarray(img)
thresholdedData = (imgData > THRESHOLD_VALUE) * 1.0
#thresholdedData.save('asdfd.jpg')
scipy.misc.imsave('outfile.jpg', thresholdedData)
