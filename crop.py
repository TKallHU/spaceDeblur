import os
import math
import cv2
import h5py
import numpy as np
from random import randint
from random import uniform
import matplotlib.pyplot as plt
from skimage.color import rgb2gray
# from keras.preprocessing import image

q_folder = 
m_folder =
trainimage_path = 
labelimage_path = 

size_input = 32  
size_label = 32 
stride = 25 

imglist = os.listdir(m_folder) 
vallist = os.listdir(q_folder)
imglist.sort(key=lambda x: int(x[:-4]))
vallist.sort(key=lambda x: int(x[:-4]))
length = len(imglist)
print(length)
count = 0
temp = 0
k = 0
l = 0
j = 0
# print(imglist)

for i in range(length):
    # print(length)
    fn2 = vallist[i]
    print(fn2)
    imagepath1 = os.path.join(q_folder, fn2) 

    img = cv2.imread(imagepath1,0)



    [hei, wid] = [img.shape[0], img.shape[1]]
    # print(hei, wid)
    for x in range(0, hei - size_input + 1, stride):
        for y in range(0, wid - size_input + 1, stride):
            
            b = img[x: x + size_input, y: y + size_input]
            [m, n] = b.shape
            
            for p in range(m):
                for q in range(n):
                    if b[p, q] == 0:
                        l += 1
            if l > 32 * 32 * 9 / 10:
                l = 0
                continue

            labeldata_name = labelimage_path + '/' + str(temp) + '.png'
            temp += 1
            cv2.imwrite(labeldata_name, b)

            fn = imglist[i]
            imagepath2 = os.path.join(m_folder, fn)
            img1 = cv2.imread(imagepath2,0)

            a = img1[x: x + size_input, y: y + size_input]

            [m, n] = a.shape

            imagedata_name = trainimage_path + '/' + str(count) + '.png'
            count += 1
            cv2.imwrite(imagedata_name, a)

print("ok!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
