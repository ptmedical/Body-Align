import cv2
import numpy as np

# Initialize the webcam
cap = cv2.VideoCapture(0)


# Check if the webcam is opened correctly
if not cap.isOpened():
    print("Error: Could not open video device.")
    exit()


# Set video frame width and height
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

while True:

    # Capture frame-by-frame
    ret, frame = cap.read()
    
    if not ret:
        print("Failed to grab frame.")
        break

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Draw the polygon on the frame
    cv2.polylines(frame, [approx], isClosed=True, color=(0, 255, 0), thickness=2)

    # Display the resulting frame
    cv2.imshow('Frame', frame)

    # Check for key presses
    key = cv2.waitKey(1) & 0xFF

    # Break the loop on 'q' key press
    if key == ord('q'):
        break


# Release the webcam and close the window
cap.release()
cv2.destroyAllWindows()
