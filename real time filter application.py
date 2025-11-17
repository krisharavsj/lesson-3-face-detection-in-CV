import cv2

cap = cv2.VideoCapture(0)
r, g, b = 1, 1, 1

while True:
    ret, frame = cap.read()
    if not ret:
        break

    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        r = min(r + 0.1, 3)
    elif key == ord('a'):
        r = max(r - 0.1, 0)
    elif key == ord('w'):
        g = min(g + 0.1, 3)
    elif key == ord('s'):
        g = max(g - 0.1, 0)
    elif key == ord('e'):
        b = min(b + 0.1, 3)
    elif key == ord('d'):
        b = max(b - 0.1, 0)
    elif key == ord('p'):
        cv2.imwrite("filtered_image.jpg", frame)

    frame[:, :, 2] = cv2.multiply(frame[:, :, 2], r)
    frame[:, :, 1] = cv2.multiply(frame[:, :, 1], g)
    frame[:, :, 0] = cv2.multiply(frame[:, :, 0], b)

    cv2.imshow("Filtered", frame)

    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()
