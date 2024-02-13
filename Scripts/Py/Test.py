import tensorflow as tf
import scipy.io
import os
import cv2
import numpy as np
from tensorflow.keras import datasets, layers, models
import matplotlib.pyplot as plt

#이미지 및 랜드마크 전처리 후에도 잘 매핑이 되나 테스트

fileCategory = "AFW"

filename = "134212_2_5"

dirpath = f"Data/landmarks/DataProcessed"

path = f"C:/Users/67160_m3548ob/Documents/TF/Data/Images/DataProcessed/{fileCategory}_{filename}.jpg"
img = cv2.imread(path)
f = open(f'Data/landmarks/DataProcessed/{fileCategory}_{filename}_pts.txt')

lines = f.readlines()

for line in lines:
    x = int(float(line.split(',')[0]) * 225)
    y = int(float(line.split(',')[1]) * 225)
    cv2.line(img,(x,y),(x,y),(0,0,255),3)

cv2.imshow("Test",img)




cv2.waitKey(0)