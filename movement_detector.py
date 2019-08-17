import cv2
import numpy as np
import time
import os
b = False
cap = cv2.VideoCapture(0)
ret1, frame1 = cap.read()
ret2, frame2 = cap.read()
os.system("touch log")
log = open("log", "w")
while True :   
    frame1_gray = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
    frame2_gray = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)
    bframe1 = cv2.GaussianBlur(frame1_gray,(21,21),0)
    bframe2 = cv2.GaussianBlur(frame2_gray,(21,21),0)
    diff = cv2.absdiff(bframe1, bframe2)
    thresh = cv2.threshold(diff, 20, 225,cv2.THRESH_BINARY)[1]
    white_pixels = np.sum(thresh)/255
    rows , cols = thresh.shape
    total = rows * cols
    if white_pixels > total * 0.01 :
        if b == False :
            print('case1')
            log.write("[Detected]"+str(time.localtime()[3:6])+"\n")
        b = True
        print('case2')
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(frame1, "--Movement Detected--", (10,50), font, 1, (0,0,255), 2, cv2.LINE_AA)
    else : 
        if b == True: 
            print('case3')
            log.write("[Disapeared]"+str(time.localtime()[3:6])+"\n")  
        print('case4')       
        b = False
    cv2.imshow("Motion", frame1)
    frame1 = frame2
    ret, frame2 = cap.read()
    if not ret : 
        break
    k = cv2.waitKey(10)
    if k == ord('q') : 
        break

cv2.destroyAllWindows()