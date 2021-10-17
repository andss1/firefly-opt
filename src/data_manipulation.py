import cv2 as cv
import numpy as np

H = 128
W = 128

def iou_result(ff, d):
    """
    :param ff: Firefly
    :param d: Num. of weights
    :return: iou average
    """
    iou = 0
    return iou


def iou_coef(img_p, img_g):
    """
    :param img_p: pipeline image
    :param img_g: gold image
    :return: iou result
    """

    lin = np.size(img_p, 0)
    col = np.size(img_p, 1)

    total_pixel = lin*col
    acc = 0

    for n in range(lin):
        for m in range(col):
            if np.array_equal(img_p[n][m], img_g[n][m]):
                acc += 1

    iou = acc/total_pixel
    return iou


def read_img(p):
    """
    :param p: path of image
    :return: image as numpy array
    """
    img = cv.imread(p)
    img = cv.resize(img, (W, H))
    img_c = np.copy(np.asarray(img)).astype(np.uint8)
    return img_c
