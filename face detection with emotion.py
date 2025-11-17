import cv2

face_cascade=cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
eye_cascade=cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_eye.xml')

cap=cv2.VideoCapture(0)

if not cap.isOpened():
    print("ERROR!COULD NOT OPEN CAMERA.")
    exit()

while True:
    ret,frame=cap.read()
    if not ret:
        print("error!failed to capture image.")
        break

    grey=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces=face_cascade.detectMultiScale(grey,1.1,5)

    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)

        roi_gray=grey[y:y+h, x:x+w]
        eyes=eye_cascade.detectMultiScale(roi_gray,1.2,10)

        emotion="Neutral"

        if len(eyes)==2:
            (ex1,ey1,ew1,eh1)=eyes[0]
            (ex2,ey2,ew2,eh2)=eyes[1]

            if abs(ey1-ey2)>20:
                emotion="Angry"
            elif ey1 < h*0.25 and ey2 < h*0.25:
                emotion="Happy"
            elif ey1 > h*0.45 and ey2 > h*0.45:
                emotion="Sad"
            else:
                emotion="Neutral"
        else:
            emotion="Neutral"

        cv2.putText(frame,emotion,(x,y-10),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)

    cv2.imshow("Emotion Detection - press q to quit",frame)

    if cv2.waitKey(1) & 0xFF==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
