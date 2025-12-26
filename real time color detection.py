import cv2 
import numpy as np

def apply_color(image,ftype):
    img=image.copy()
    if ftype=="red tint":
        img[:,:,1]=img
    elif ftype=="green_tint":
        img[:,:,0]=img[:,:,2]=0
    elif ftype=="green tint":
        img[:,:,0]=img[:,:,2]=0
    elif ftype=="blue tint":
        img[:,:,1]=img[:,:,2]=0
    elif ftype=="sobel":
        gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
        sx=cv2.Sobel(gray,cv2.cv2CV_64F,1,0,ksize=3)
        sy=cv2.Sobel(gray,cv2.cv2CV_64F,0,1,ksize=3)
        sob=cv2.bitwise_or(sx.astype('unit8'),sy.astype('unit8'))
        img=cv2.cvtColor(sob,cv2.COLOR_BGR2GRAY)
    elif ftype=="canny":
        gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
        can=cv2.canny(gray,100,200)
        img=cv2.cvtColor(can,cv2.COLOR_BGR2GRAY)
    elif