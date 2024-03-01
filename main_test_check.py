import cv2

# Initialize webcam
cap = cv2.VideoCapture()

# Check if webcam is opened successfully
if not cap.isOpened():
    print("Error: Failed to open webcam")
    exit()

# Main loop for capturing and displaying frames
while True:
    # Read frame from webcam
    ret, frame = cap.read()

    # Check if frame is read successfully
    if not ret:
        print("Error: Failed to capture frame")
        break

    # Display frame
    cv2.imshow('frame', frame)

    # Check for 'q' key press to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release webcam and close windows
cap.release()
cv2.destroyAllWindows()
