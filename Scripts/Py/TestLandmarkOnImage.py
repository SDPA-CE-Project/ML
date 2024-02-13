import cv2
import scipy.io
import mat73
import numpy as np

fileCategory = "AFW"
filename = "134212_2_5"


f = scipy.io.loadmat(f'Data\\landmarks\\{fileCategory}\\{fileCategory}_{filename}_pts.mat')


pts2d = f['pts_2d']
pts3d = f['pts_3d'] #해당 데이터의 구조는 아직 잘 모르겠음

path = f"C:/Users/67160_m3548ob/Documents/TF/Data/Images/{fileCategory}/{fileCategory}_{filename}.jpg"
img = cv2.imread(path)

len = 68

print(pts2d[0][0])


for i in range(len):
    cv2.line(img,(int(pts2d[i][0]), int(pts2d[i][1])),(int(pts2d[i][0]),int(pts2d[i][1])),(0,0,255),5)
    #cv2.line(img,(int(pts3d[i][0]),int(pts3d[i][1])),(int(pts3d[i][0]),int(pts3d[i][1])),(0,255,0),5)

cv2.imshow("Test",img)




cv2.waitKey(0)