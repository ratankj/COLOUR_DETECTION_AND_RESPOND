import cv2

cap = cv2.VideoCapture()


if not cap.isOpened():
    print("Error: Failed to open webcam")
    exit()
while True:
    ret,frame = cap.read()

    cv2.imshow('frame',frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()

cv2.destroyAllWindows()