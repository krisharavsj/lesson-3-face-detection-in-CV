import cv2
import numpy as np
cap =cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error: Could not open webcam")
    exit()

while True:
    ret,frame=cap.read
    if not ret:
        print("Error: failed to capture image")
        break
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    lower_skin=np.array([0,20,70],dtype=np.unit)