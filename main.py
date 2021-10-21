from src.fireflyAlg import firefly
from src.data_manipulation import *

#firefly(2, 10, 1.0, 0.97, 1.0, 100)

path_1 = './data/pipeline1/predict_0.png'
path_2 = './data/pipeline1/predict_0.png'
path_3 = './data/gold/img_0.png'

#print(iou_coef(read_img(path_1), read_img(path_3)))
#print(iou_result())
#print(read_img(path_3))
#print('===========')
'''
t = []

t.append(read_img(path_3))
t.append(read_img(path_3))'''

result_image(read_img(path_3), read_img(path_3))
#print(result_image(read_img(path_3), read_img(path_2)))

#print(weighted_image(read_img(path_3), 0.7))
