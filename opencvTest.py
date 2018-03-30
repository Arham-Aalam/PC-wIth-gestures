import numpy as np
import cv2
import pyautogui

face_cascade = cv2.CascadeClassifier('face_data.xml')
eye_cascade = cv2.CascadeClassifier('eyes_data.xml')

cap = cv2.VideoCapture(1)

while True:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    x1,x2,y1 = 0,0,0
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        [x1, x2, y1] = [x, x + w, y]
        print(x1, x2, y1)
    imgparsed = img[0:int(y1), int(x1+(x1//2)):int(x2+(x1//2))]
    
    '''
        pyautogui.press('left')
        pyautogui.press('right')
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
    '''
    cv2.imshow('img',img)
    try:
        cv2.imshow('imgparsed', imgparsed)
    except:
        pass    
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
