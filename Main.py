import numpy as np
import cv2
import pyautogui
import time

face_cascade = cv2.CascadeClassifier('face_data.xml')
eye_cascade = cv2.CascadeClassifier('eyes_data.xml')
cap = cv2.VideoCapture(1)
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(3,3))
fgbg = cv2.createBackgroundSubtractorMOG2()
fgbg2 = cv2.createBackgroundSubtractorMOG2()
start = time.time() + 1
x1, y1, w1, h2 = 0,10,10,10
flag = False
while True:
    flag = False
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        [x1, y1, w1, h2] = [x,y,w,h]
        flag = True
    width = cap.get(3) 
    height = cap.get(4)
    fgmask = fgbg.apply(frame)
    fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_OPEN, kernel)
    preimg = fgmask[0:int(y1//2), 0:int(width)]
    ret, frame = cap.read()
    fgmask2 = fgbg.apply(frame)
    fgmask2 = cv2.morphologyEx(fgmask2, cv2.MORPH_OPEN, kernel)
    crrimg = fgmask2[0:int(y1//2), 0:int(width)]
    diff = cv2.absdiff(preimg, crrimg)
    diffsum = diff.sum() 
    #cv2.imshow('frame',fgmask)
    #cv2.imshow('frame',fgmask2)
    cv2.putText(diff,str(diffsum), (10,20), cv2.FONT_HERSHEY_SIMPLEX, 2, 255)
    #cv2.imshow('diff',diff)
    cv2.imshow('frame',frame)
    #need to          this   | remove if dont work
    if diffsum//1000000 > 0 and flag:
        if (int(time.time()-start) > 1):
            
            leftimg = diff[0:int(y1//2), 0:int(x1 + w1//2)]
            rightimg = diff[0:int(y1//2), int(x1 + w1//2):int(width)]
            if leftimg.sum() > rightimg.sum():
                pyautogui.press('right')
                print("right pressed")
            else:
                pyautogui.press('left')
                print("left pressed")
            start = time.time()
    if cv2.waitKey(17) == ord('q'):
        break
    

cap.release()
cv2.destroyAllWindows()
