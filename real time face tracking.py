import cv2

face_cascade=cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
cap=cv2.VideoCapture(0)

if not cap.isOpened():
    print("ERROR!Cant open the camera")
    exit()
while True:
    ret,frame=cap.read()
    if not ret:
        print("error!failed to capture image")
        break
    grey=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces=face_cascade.detectMultiScale(grey,scaleFactor=1.1,minNeighbors=5,minSize=(30,30))
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        font=cv2.FONT_HERSHEY_COMPLEX
        cv2.putText(frame,f'People Count:{len(faces)}',(10,30),font,1,(255,0,0),2,cv2.LINE_AA)
        cv2.imshow("face detection-press q to quit",frame)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
cap.release()
cv2.destroyAllWindows