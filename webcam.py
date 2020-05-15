import numpy as np
import cv2 as cv

url = "http://192.168.43.221:8080/shot.jpg"


while(True):
    cam = cv.VideoCapture(url)
    
    ret , frame = cam.read()
    
    cv.namedWindow('LiveFrame', cv.WINDOW_NORMAL)

    cv.imshow('LiveFrame' , frame)

    key = cv.waitKey(100) &0xFF
    if key == 27:
        break
cam.release()
cv.destroyAllWindows()

'''
Ip - Webcam = app
https://play.google.com/store/apps/details?id=com.pas.webcam&hl=en_IN

'''
