import numpy as np
import cv2
import pyautogui
import time

cap = cv2.VideoCapture(1)
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(3,3))
fgbg = cv2.createBackgroundSubtractorMOG2()
fgbg2 = cv2.createBackgroundSubtractorMOG2()
start = time.time() + 1
while(1):
    ret, frame = cap.read()
    width = cap.get(3)  # float
    height = cap.get(4) # float
    fgmask = fgbg.apply(frame)
    fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_OPEN, kernel)
    preimg = fgmask[0:int(height//4), 0:int(width)]
    ret, frame = cap.read()
    fgmask2 = fgbg.apply(frame)
    fgmask2 = cv2.morphologyEx(fgmask2, cv2.MORPH_OPEN, kernel)
    crrimg = fgmask2[0:int(height//4), 0:int(width)]
    diff = cv2.absdiff(preimg, crrimg)
    diffsum = diff.sum() 
    #cv2.imshow('frame',fgmask)
    #cv2.imshow('frame',fgmask2)
    cv2.putText(diff,str(diffsum), (10,20), cv2.FONT_HERSHEY_SIMPLEX, 2, 255)
    cv2.imshow('diff',diff)
    if diffsum//1000000 > 0:
        if (int(time.time()-start) > 1):
            pyautogui.press('right')
            start = time.time()
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
    

cap.release()
cv2.destroyAllWindows()
