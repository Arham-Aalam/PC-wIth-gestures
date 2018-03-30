import time
import os
import controller
import cv2
import pyautogui

def main():
    time.sleep(10)
    controlPC = controller.Controller(1)
    savedimg = cv2.imread("images/pres" + controlPC.randname + "nt.png")
    capt = cv2.VideoCapture(1)
    flag = True
    pdiffsum, diffsum = 0,0
    while True:
        pdiffsum = diffsum
        ret,frame1 = capt.read()
        controlPC.feedFace(frame1)
        if(controlPC.x1 + controlPC.y1  > 0):
            newsaveimg = savedimg[0:controlPC.y1-(controlPC.y1//2), controlPC.x1:controlPC.x1 + controlPC.w1]
            newsaveimg = cv2.GaussianBlur(newsaveimg,(8,8),0)
            graysaved = cv2.cvtColor(newsaveimg, cv2.COLOR_BGR2GRAY)
            #ret,frame1 = capt.read()
            frame2 = frame1[0:controlPC.y1-(controlPC.y1//2), controlPC.x1:controlPC.x1 + controlPC.w1]
            frame2 = cv2.GaussianBlur(frame2,(8,8),0)
            grayframe2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)
            diff = cv2.absdiff(grayframe2, graysaved)
            if flag:
                diffsum = diff.sum()
                flag = False
            else:
                diffsum = diff.sum()
                if (abs(pdiffsum - diffsum)//1000000) > 0 :
                    pyautogui.press('right')
                    print("key pressed with difference " + str(abs(pdiffsum - diffsum)))
            _, thresh = cv2.threshold(diff, 0, 255, cv2.THRESH_BINARY)
            cv2.imshow("thresh", thresh)
        cv2.imshow("frame", frame1)
        k = cv2.waitKey(30) & 0xff
        if k == 27:
            break

    capt.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
