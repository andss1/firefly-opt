import sys

import cv2 as cv
import numpy as np

np.set_printoptions(threshold=sys.maxsize)

H = 128
W = 128

def read_img(p):
    """
    :param p: path of image
    :return: image as numpy array
    """
    img = cv.imread(p)
    img = cv.resize(img, (W, H))
    img_c = np.copy(np.asarray(img)).astype(np.float)
    return img_c


def weighted_image(img, w):
    """
    :param img: image (numpy array)
    :param w: weight of firefly
    :return: new image
    """
    img_c = np.copy(np.asarray(img)).astype(np.float)

    lin = np.size(img_c, 0)
    col = np.size(img_c, 1)
    for n in range(lin):
        for m in range(col):
            for k in range(len(img_c[n][m])):
                img_c[n][m][k] = img_c[n][m][k]*w

    return img_c


def result_image(img1, img2):
    lin = np.size(img1, 0)
    col = np.size(img1, 1)
    res = np.zeros((128, 128, 3))

    for n in range(lin):
        for m in range(col):
            for k in range(len(res[n][m])):
                res[n][m][k] = img1[n][m][k] + img2[n][m][k]
    return res
