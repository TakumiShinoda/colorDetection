import cv2
import numpy as np
import os

cap = cv2.VideoCapture(0)
frame_degree = 1
accurate = 3
lower = np.array([0,58,88])
upper = np.array([25,173,229])

def display(frame):
    cv2.imshow("frame",frame)

while True:
    count = 0
    ret,frame = cap.read()
    size = (frame.shape[1] / frame_degree,frame.shape[0] / frame_degree)

    frame = cv2.resize(frame,size)
    h = frame.shape[0]
    w = frame.shape[1]
    pixels = h * w

    frameSmooth = cv2.medianBlur(frame,7);
    frameHSV = cv2.cvtColor(frameSmooth,cv2.cv.CV_BGR2HSV)
    
    frameHSV = cv2.inRange(frameHSV,lower,upper)
    min_pixels = pixels / accurate
    
    for content in frameHSV:
        count += np.count_nonzero(content)

    if count > min_pixels:
        print("detected")
    
    display(frameHSV)
            
    cv2.waitKey(1)
