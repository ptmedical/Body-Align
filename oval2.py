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

    # Perform edge detection using Canny
    edges = cv2.Canny(gray, 50, 150)


    # Find contours in the edged image
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # List to store the polygon points
    polygons = []

    # Iterate over the contours
    for contour in contours:
        # Approximate the contour to a polygon
        epsilon = 0.02 * cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, epsilon, True)

        # Draw the polygon on the frame
        cv2.polylines(frame, [approx], isClosed=True, color=(0, 255, 0), thickness=2)

        # Save the polygon points
        polygons.append(approx)

    # Display the resulting frame
    cv2.imshow('Frame', frame)
    cv2.imshow('EDges', edges)

    # Check for key presses
    key = cv2.waitKey(1) & 0xFF

    # Break the loop on 'q' key press
    if key == ord('q'):
        break

    # Save the frame and polygon points on 's' key press
    if key == ord('s'):
        # Save the current frame as an image
        cv2.imwrite('captured_frame.png', frame)
        print("Frame captured and saved as 'captured_frame.png'.")

        # Save the polygon points to a file
        with open('contours.txt', 'w') as file:
            for polygon in polygons:
                file.write(f"{polygon.reshape(-1, 2).tolist()}\n")
        print("Contour polygon points saved to 'contours.txt'.")

# Release the webcam and close the window
cap.release()
cv2.destroyAllWindows()