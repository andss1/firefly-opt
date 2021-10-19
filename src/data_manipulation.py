import os

import cv2 as cv
import numpy as np

H = 128
W = 128


def iou_result():
    """
    :param ff: Firefly
    :param d: Num. of weights
    :return: iou average
    """
    path_pl1 = './data/pipeline1'
    path_gold = './data/gold'
    files_pl1 = os.listdir(path_pl1)
    files_gold = os.listdir(path_gold)

    total_img = 0
    acc_iou = 0
    for index, file in enumerate(files_pl1):
        pl1 = path_pl1 + '/' + file
        gold = path_gold + '/' + files_gold[index]
        acc_iou = acc_iou + iou_coef(read_img(pl1), read_img(gold))
        total_img = index
    total_img += 1

    avg_iou = acc_iou/total_img

    return avg_iou


def iou_coef(img_p, img_g):
    """
    :param img_p: pipeline image
    :param img_g: gold image
    :return: iou result
    """

    lin = np.size(img_p, 0)
    col = np.size(img_p, 1)

    total_pixel = lin * col
    acc = 0

    for n in range(lin):
        for m in range(col):
            if np.array_equal(img_p[n][m], img_g[n][m]):
                acc += 1

    iou = acc / total_pixel
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
