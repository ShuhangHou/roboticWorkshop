import cv2
import cv2.aruco as aruco
import numpy as np
import os
from Motor import *
pwm = Motor()

def findArucoMarkers(img, markerSize = 6, totalMarkers=250, draw=True):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    key = 10
    arucoDict = aruco.Dictionary_get(key)
    arucoParam = aruco.DetectorParameters_create()
    bboxs, ids, rejected = aruco.detectMarkers(gray, arucoDict, parameters = arucoParam)
    # print(ids)
    if draw:
        aruco.drawDetectedMarkers(img, bboxs)
    return [bboxs, ids]
cap = cv2.VideoCapture(0)
#cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
#cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)
rotate = 0
while True:
    success, img = cap.read()
    arucofound = findArucoMarkers(img)
    
     # loop through all the markers and augment each one
    if  len(arucofound[0])!=0:
        
        for bbox, id in zip(arucofound[0], arucofound[1]):
            print(bbox)
            middle = sum(bbox[0,:,0])/2
            print(middle)
            if middle> 900:
                pwm.setMotorModel(800,800,-800,-800)
                #time.sleep(0.2)
                #PWM.setMotorModel(0,0,0,0)
                #time.sleep(0.2)
                rotate = 1
            elif middle <500:
                pwm.setMotorModel(-800,-800,800,800)
                #time.sleep(0.2)
                #PWM.setMotorModel(0,0,0,0)
                #time.sleep(0.2)
                rotate = 0
            else:
                PWM.setMotorModel(0,0,0,0)
                #time.sleep(0.2)
    else:
        if rotate == 0:
            pwm.setMotorModel(-800,-800,800,800)
            #time.sleep(0.2)
            #PWM.setMotorModel(0,0,0,0)
            #time.sleep(0.2)
        else:
            pwm.setMotorModel(800,800,-800,-800)
            #time.sleep(0.2)
            #PWM.setMotorModel(0,0,0,0)
            #time.sleep(0.2)
            rotate = 1
    cv2.imshow('img',img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        PWM.setMotorModel(0,0,0,0)
        break

cap.release()
cv2.destroyAllWindows()
