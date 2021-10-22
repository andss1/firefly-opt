import os
from src.data_manipulation import *

#Average IoU
def iou_result(ff):
    """
    :param ff: Firefly
    :return: iou average
    """
    path_pl1 = './data/pipeline1'
    path_pl2 = './data/pipeline2'
    path_gold = './data/gold'

    files_pl1 = os.listdir(path_pl1)
    files_pl2 = os.listdir(path_pl2)
    files_gold = os.listdir(path_gold)

    total_img = 0
    acc_iou = 0
    for index, file in enumerate(files_pl1):
        pl1 = path_pl1 + '/' + file
        pl2 = path_pl2 + '/' + files_pl2[index]
        gold = path_gold + '/' + files_gold[index]

        img1 = read_img(pl1)
        img2 = read_img(pl2)
        img_gold = read_img(gold)

        img_res = result_image(weighted_image(img1, ff[0]), weighted_image(img2, ff[1]))

        acc_iou = acc_iou + iou_coef(img_res, img_gold)
        total_img = index
    total_img += 1

    avg_iou = acc_iou/total_img
    return avg_iou

#IoU coefficient
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