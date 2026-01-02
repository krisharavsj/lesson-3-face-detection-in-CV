import cv2,time,pyautogui
import mediapipe as mp

mp_hands=mp.solutions.hands
hands=mp_hands.Hands(max_num_hands=1,min_detection_confidence=0.7)
mp_drawing=mp.solutions.drawing_utils

scroll_speed=300
scroll_delay=1
cam_width,cam_height=640,480

def detect_gesture(landmarks,handedness):
    fingers=[]
    tips=[mp_hands.HandLandmark.INDEX_FINGER_TIP,mp_hands.HandLandmark.MIDDLE_FINGER_TIP,
          mp_hands.HandLandmark.RING_FINGER_TIP,mp_hands.HandLandmark.PINKY_TIP]
    for tip in tips:
        if landmarks.landmark[tip].y<landmarks.landmark[tip-2].y:
            fingers.append(1)

            thumb_tip=landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
            thumb_ip=landmarks.landmark[mp_hands.HandLandmark.THUMB_IP]

            if (handedness=="Right" and thumb_tip.x>thumb_ip.x)or(handedness=="Left"and thumb_tip.x<thumb_ip.x):
                return "scroll_up"if sum(fingers)==5 else "scroll_down" if len(fingers)==0 else "none"
            cap=cv2.VideoCapture(0)
            cap.set(3,cam_width)
            cap.set(4,cam_height)
            lest_scroll=p_time=0
            
            print("gesture scroll control active/nopen palm: scroll up/nfist:scroll down/press'q' to exit")

            while cap.isOpened():
                success,img=cap.read()
                if not success:break

                img=cv2.flip(cv2.cvtColor(img,cv2.COLOR_BGR2RGB),1)
                results=hands.process(img)
                gesture,handedness="none","unknown"
                if results.multi_hand_landmarks:

                    for hand, handedness_info in zip(results.multi_hand_landmarks, results.multi_handedness):

                        handedness = handedness_info.classification[0].label

                        gesture = detect_gesture(hand, handedness)

                        mp_drawing.draw_landmarks(img, hand, mp_hands.HAND_CONNECTIONS)

                    if (time.time() - last_scroll) > SCROLL_DELAY:

            if gesture == "scroll_up":
                pyautogui.scroll(SCROLL_SPEED)

            elif gesture == "scroll_down":
                pyautogui.scroll(-SCROLL_SPEED)
