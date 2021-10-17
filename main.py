from src.fireflyAlg import firefly
from src.data_manipulation import *

#firefly(2, 10, 1.0, 0.97, 1.0, 100)

path_1 = './data/pipeline1/predict_0.png'
path_2 = './data/pipeline1/predict_0.png'
path_3 = './data/gold/img_0.png'

print(iou_coef(read_img(path_1), read_img(path_3)))


