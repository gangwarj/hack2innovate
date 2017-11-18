
#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Binarize (make it black and white) an image with Pyhton."""
import colorsys
from PIL import Image
from scipy.misc import imsave
import numpy
import colorsys
import cv2
image = cv2.imread('test.jpg')
image_hsv = colorsys.rgb_to_hsv(0.2, 0.4, 0.4)
cv2.imwrite('qwertygf.jpg',image_hsv)
"""

def binarize_image(img_path, target_path, threshold):
    image_file = Image.open(img_path)
    image = colorsys.rgb_to_hsv(359,1,1)
    image = image_file.convert('L')  # convert image to monochrome
    image = numpy.array(image)
    image = binarize_array(image, threshold)
    imsave(target_path, image)


def binarize_array(numpy_array, threshold=200):
    for i in range(len(numpy_array)):
        for j in range(len(numpy_array[0])):
            if numpy_array[i][j] > threshold:
                numpy_array[i][j] = 255
            else:
                numpy_array[i][j] = 0
    return numpy_array


def get_parser():
    from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter
    parser = ArgumentParser(description=__doc__,formatter_class=ArgumentDefaultsHelpFormatter)
    parser.add_argument("-i", "--input",dest="input", help="read this file",metavar="FILE", required=True)
    parser.add_argument("-o", "--output",dest="output",help="write binarized file hre",metavar="FILE",required=True)
    parser.add_argument("--threshold",dest="threshold", default=200,type=int,help="Threshold when to show white")
    return parser


if __name__ == "__main__":
    args = get_parser().parse_args()
    binarize_image(args.input, args.output, args.threshold)

"""
