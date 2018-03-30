import cv2
import random
import numpy as np

class Controller:
    def __init__(self, camera):
        self.randname = str(random.randint(1, 100))
        self.cap = cv2.VideoCapture(camera)
        ret,frame = self.cap.read()
        cv2.imshow("frame", frame)
        try:
            cv2.imwrite("images/pres" + self.randname + "nt.png", frame)
        except:
            self.randname = str(random.randint(1, 100))
            cv2.imwrite("images/pres" + self.randname + "nt.png", frame)
        self.face_cascade = cv2.CascadeClassifier('face_data.xml')
        self.eye_cascade = cv2.CascadeClassifier('eyes_data.xml')

    def feedFace(self, img):
        ret, img = self.cap.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = self.face_cascade.detectMultiScale(gray, 1.3, 5)
        self.x1, self.y1, self.w1, self.h2 = 0,0,0,0
        for (x,y,w,h) in faces:
            cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
            [self.x1, self.y1, self.w1, self.h2] = [x,y,w,h]
        

