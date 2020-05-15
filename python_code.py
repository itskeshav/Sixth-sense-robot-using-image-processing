import numpy as np
import cv2 as cv
import serial
import time

Arduino = serial.Serial('com3',9600)
time.sleep(2)

cam = cv.VideoCapture(0)

#when we use blue ball
lower_bound = np.array([110,50,50]) 
upper_bound = np.array([130,255,255]) 

# WHEN WE USE RED BALL
#lower_bound = np.array([0,125,125])
#upper_bound = np.array([10,255,255])

while(True):

    ret , frame = cam.read()
    frame = cv.flip(frame , 1)

    w = frame.shape[1]
    h = frame.shape[0]

    #smoothing the image
    image_smooth = cv.GaussianBlur(frame , (7,7) , 0)

    #define ROI
    mask = np.zeros_like(frame)

    mask[50:350 , 50:350] = [255 , 255 , 255]

    image_roi = cv.bitwise_and(image_smooth , mask)
    cv.rectangle(frame , (50,50) , (350,350) , (0,0,255) , 2)
    cv.line(frame , (150,50) , (150,350) , (0,0,255) , 1)
    cv.line(frame , (250,50) , (250,350) , (0,0,255) , 1)
    cv.line(frame , (50,150) , (350,150) , (0,0,255) , 1)
    cv.line(frame , (50,250) , (350,250) , (0,0,255) , 1)


    #threshold the image for red color
    img_hsv = cv.cvtColor(image_roi , cv.COLOR_BGR2HSV)
    img_threshold = cv.inRange(img_hsv , lower_bound , upper_bound)


    # find countours
    contours, hierarchy = cv.findContours(img_threshold, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

    # FIND THE Index of the largest countour
    if (len(contours)!=0):
        areas = [cv.contourArea(c) for c in contours]
        max_index = np.argmax(areas)
        cnt = contours[max_index]


        #pointers on video
        M = cv.moments(cnt)
        if (M['m00'] != 0):
            cx = int(M['m10']/M['m00'])
            cy = int(M['m01']/M['m00'])
            cv.circle(frame , (cx, cy) , 4 , (0,255,0) , -1)

            #cursor motion
            if cx in range(150,250):
                if cy < 150:
                    Arduino.write(b'f')
                    print("FORWARD")
                elif cy > 250:
                    Arduino.write(b'b')
                    print("BACKWARD")
                else:
                    Arduino.write(b's')
                    print("STOP")

            if cy in range(150,250):
                if cx < 150:
                    Arduino.write(b'l')
                    print("LEFT")
                elif cx >250:
                    Arduino.write(b'r')
                    print("RIGHT")
                else:
                    Arduino.write(b's')
                    print("STOP")


    cv.imshow('Frame' , frame)

    key = cv.waitKey(100)
    if key == 27:
        break
cv.destroyAllWindows()
                    
                    
                    
            