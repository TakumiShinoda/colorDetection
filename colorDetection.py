import cv2
import numpy as np

cap = cv2.VideoCapture(0)
frame_degree = 1
accurate = 3
lower = np.array([0,58,88])
upper = np.array([25,173,229])

def display(frame):
    cv2.imshow("frame",frame)

def detection(frame):
    count = 0
    size = (frame.shape[1] / frame_degree,frame.shape[0] / frame_degree)
    frame = cv2.resize(frame,size)
    pixels = frame.shape[0] * frame.shape[1]
    
    frameSmooth = cv2.medianBlur(frame,7);
    frameHSV = cv2.cvtColor(frameSmooth,cv2.cv.CV_BGR2HSV)
    
    frameHSV = cv2.inRange(frameHSV,lower,upper)
    min_pixels = pixels / accurate
    
    for content in frameHSV:
        count += np.count_nonzero(content)

    if count > min_pixels: 
        return count
    else:
        return 0

while True:
    left = 0
    right = 0
    ret,frame = cap.read()
    h = frame.shape[0]
    w = frame.shape[1]
    frame_left = frame[0:h,w / 2:w]
    frame_right = frame[0:h,0:w / 2]
    
    left = detection(frame_left)
    right = detection(frame_right)
    
    if left > right:
        print("left")
    elif left < right:
        print("right")

    display(cv2.inRange(cv2.cvtColor(cv2.medianBlur(frame,7),cv2.cv.CV_BGR2HSV),lower,upper))
            
    cv2.waitKey(1)
