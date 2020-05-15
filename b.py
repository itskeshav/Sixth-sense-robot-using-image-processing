import numpy as np
import cv2 as cv




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


    cv.namedWindow('mask', cv.WINDOW_NORMAL)
    cv.namedWindow('frame', cv.WINDOW_NORMAL)
    cv.namedWindow('bit', cv.WINDOW_NORMAL)
    cv.namedWindow('hsv', cv.WINDOW_NORMAL)
    cv.namedWindow('threshold', cv.WINDOW_NORMAL)

    
    cv.imshow('frame' , frame)
    cv.imshow('mask' , mask)
    cv.imshow('bit' , image_roi)
    cv.imshow('hsv' , img_hsv)
    cv.imshow('threshold' , img_threshold)
    #cv.imshow('threshold' , bit)

    key = cv.waitKey(100)
    if key == 27:
        break
cv.destroyAllWindows()












    
