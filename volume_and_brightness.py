import cv2
import mediapipe as mp
import numpy as np
import math
import subprocess

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
)
mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

def set_volume(volume_percent):
    volume_percent = int(volume_percent)
    subprocess.call([
        "osascript",
        "-e",
        f"set volume output volume {volume_percent}"
    ])

def set_brightness(brightness_percent):
    brightness_value = brightness_percent / 100
    subprocess.call([
        "brightness",
        f"{brightness_value}"
    ])

while True:
    success, img = cap.read()
    if not success:
        break

    img = cv2.flip(img, 1)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    result = hands.process(img_rgb)

    if result.multi_hand_landmarks:
        for hand in result.multi_hand_landmarks:
            lm_list = []

            for id, lm in enumerate(hand.landmark):
                h, w, _ = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                lm_list.append((id, cx, cy))

            if lm_list:
                x1, y1 = lm_list[4][1], lm_list[4][2]
                x2, y2 = lm_list[8][1], lm_list[8][2]

                cv2.circle(img, (x1, y1), 10, (0, 255, 0), -1)
                cv2.circle(img, (x2, y2), 10, (0, 255, 0), -1)
                cv2.line(img, (x1, y1), (x2, y2), (255, 0, 0), 3)

                distance = math.hypot(x2 - x1, y2 - y1)

                volume = np.interp(distance, [30, 200], [0, 100])
                brightness = np.interp(distance, [30, 200], [0, 100])

                set_volume(volume)
                set_brightness(brightness)

                cv2.putText(
                    img,
                    f"Volume: {int(volume)}%  Brightness: {int(brightness)}%",
                    (10, 50),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1,
                    (0, 255, 255),
                    2
                )

            mp_draw.draw_landmarks(img, hand, mp_hands.HAND_CONNECTIONS)

    cv2.imshow("Mac Volume & Brightness Control", img)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()