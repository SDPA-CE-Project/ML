import cv2
import os

fileCategorys = ["IBUG","AFW","HELEN","LFPW"]

for fileCategory in fileCategorys:
    
    dirpath = f"C:/Users/67160_m3548ob/Documents/TF/Data/Images/{fileCategory}" #원본 파일 폴더 위치에 따라 수정 필요
    
    datalist = os.listdir(dirpath)  #폴더안의 모든 파일 목록 불러오기
    
    if datalist.__contains__("desktop.ini"):    #윈도우 파일 탐색기로 해당 폴더를 열었을때 가끔씩 해당 파일이 끼어있음
        datalist.remove("desktop.ini")          #전처리에 필요 없으므로 리스트에서 삭제

    dataSaveDirPath = f"C:/Users/67160_m3548ob/Documents/TF/Data/Images/DataProcessed"  #전처리 파일 저장 폴더 위치

    n = 0

    m = len(datalist)

    #전처리는 그레이스케일 변환 과 크기 축소
    
    
    for imgname in datalist:
        filepath = dirpath + f"/{imgname}"
        dataSavePath = dataSaveDirPath + f"/{imgname}"
        img = cv2.imread(filepath)
        resized_img = cv2.resize(img,(225,225),interpolation=cv2.INTER_LINEAR)
        gray = cv2.cvtColor(resized_img, cv2.COLOR_BGR2GRAY)
        cv2.imwrite(dataSavePath,gray)
        n +=1
        print(str(n) + '/' + str(m))



#print(len(datalist))

#img = cv2.imread('')