import cv2
import mediapipie as mp
import numpy as np
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from comtypes import CLSCTX
from math import hypot
import screen_brightness_control as sbc

mp_hands=mp.solutions.hands
hands=mp_hands.Hands(min_detection_confidence=0.7,min_tracking_confidence=0.7)
mp_draw=mp.solutions.drawing_utils

try:
    devices=AudioUtilities.GetSpeakers()
    interface=devices.activate(IAudioEndpointVolume._iid_,CLSCTX_ALL,None)
    volume=interface.QueryInterFace(IAudioEndpointVolume)
    min_vol,max_vol=volume.GetVolumeRange()[0:2]
except Exception as e:
    print(f"Pycaw error:{e}")
    exit()

cap=cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error: Webcam not accessible")
    exit()

while True:
    ret, img=cap.read()
    if not ret:
        break
    img=cv2.flip(img, 1)
    img_rgb=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    results=hands.process(img_rgb)
    h, w,_=img.shape
    if results.multi_hand_landmarks  and results.multi_handness:
        for i,handLms in enumerate(results.multi_hand_landmarks):
            label=results.multi_handness[i].classififcation[0].label
            mp_draw.draw_landmarks(img, handLms, mp_hands.HAND.CONNETCTIONS)

            thumb=handLms.landmark[mp_hands.HandLandmark.THUMB_TIP]
            index=handLms.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
            thumb_pos=(int(thumb.x*w),int(thumb.y*h))
            index_pos=(int(index.x*w),int(thumb.y*h))
            cv2.circle(img, thumb_pos, 10, (255,0,0),cv2.FILLED)
            cv2.circle(img, index_pos, 10, (255,0,0),cv2.FILLED)
            cv2.line(img, thumb_pos, index_pos,(0,255,0),3)

            

