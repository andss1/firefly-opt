from src.fireflyAlg import firefly
from src.data_manipulation import *
from src.iou_metric import *

firefly(2, 5, 1.0, 0.97, 1.0, 10)

#path_2 = './data/pipeline1/predict_0.png'
#path_3 = './data/gold/img_0.png'

#print(iou_coef(read_img(path_1), read_img(path_3)))
#print(iou_result())
#print(read_img(path_3))
#print('===========')
'''
t = []

t.append(read_img(path_3))
t.append(read_img(path_3))'''

#result_image(read_img(path_3), read_img(path_3))
#print(result_image(read_img(path_3), read_img(path_2)))

#print(weighted_image(read_img(path_3), 0.7))

'''path_1 = './data/pipeline1/predict_0.png'
ff1 = [0.7, 0.3]
img1 = read_img(path_1)

mx1 = weighted_image(img1, ff1[0])
mx2 = weighted_image(img1, ff1[1])

r = result_image(mx1, mx2)
print(iou_result(ff1))'''

#print(iou_coef(mx2, read_img(path_3)))

