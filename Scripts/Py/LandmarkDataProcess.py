import cv2
import scipy.io
import os

fileCategorys = ["IBUG","AFW","HELEN","LFPW"]

for fileCategory in fileCategorys:

    dirpath = f"C:/Users/67160_m3548ob/Documents/TF/Data/landmarks/{fileCategory}"  #원본 파일 폴더 위치에 따라 수정 필요
    
    TargetDirPath = f"C:/Users/67160_m3548ob/Documents/TF/Data/landmarks/DataProcessed" #전처리 파일 저장 폴더 위치
    
    datalist = os.listdir(dirpath)              #폴더안의 모든 파일 목록 불러오기
    if datalist.__contains__("desktop.ini"):    #윈도우 파일 탐색기로 해당 폴더를 열었을때 가끔씩 해당 파일이 끼어있음
        datalist.remove("desktop.ini")          #전처리에 필요 없으므로 리스트에서 삭제

    m  = len(datalist)
    n = 0

    #정규화 전처리
    for data in datalist:
        n += 1
        f = scipy.io.loadmat(f'Data\\landmarks\\{fileCategory}\\{data}')
        landmark = f['pts_2d']
        data = data.replace("mat","txt")
        fw = open(f'{TargetDirPath}/{data}',"w+")
        
        for i in range(68):
            x = landmark[i][0] / 450.0
            y = landmark[i][1] / 450.0
            fw.write(str(x) + ',' + str(y) + '\n')
        fw.close()
        print(str(n)+'/'+str(m))