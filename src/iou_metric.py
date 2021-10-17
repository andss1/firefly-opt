



def iou_result(ff):
    if ff[0] >= 0.9:
        return 0.99
    elif ff[0] >= 0.8:
        return 0.98
    elif ff[0] >= 0.7:
        return 0.97
    elif ff[0] >= 0.6:
        return 0.91
    elif ff[0] > 0.5:
        return 0.80
    elif ff[0] > 0.4:
        return 0.79
    elif ff[0] > 0.3:
        return 0.78
    elif ff[0] > 0.2:
        return 0.77
    else:
        return 0.01
