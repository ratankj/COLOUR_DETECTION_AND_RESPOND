import numpy as np
import cv2
import pyautogui

# Function to check if a square is red
def is_red_square(img, contour):
    x, y, w, h = cv2.boundingRect(contour)
    roi = img[y:y+h, x:x+w]
    hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
    lower_red = np.array([0, 100, 100])
    upper_red = np.array([10, 255, 255])
    mask = cv2.inRange(hsv, lower_red, upper_red)
    return cv2.contourArea(contour) > 100 and cv2.countNonZero(mask) > 0

while True:
    # Capture the screen
    screenshot = pyautogui.screenshot()
    frame = np.array(screenshot)
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
    
    # Convert to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Detect contours
    contours, _ = cv2.findContours(gray, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # Check each contour
    for contour in contours:
        if cv2.contourArea(contour) > 100:
            if is_red_square(frame, contour):
                print("Red square detected!")
                # Add your trigger action here
                
    # Display the captured screen
    cv2.imshow('Screen', frame)
    
    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
