import cv2
import numpy as np
import ast

# Function to read the contour points from the file
def read_contours_from_file(file_path):
    contours = []
    with open(file_path, 'r') as file:
        for line in file:
            # Convert the string representation of the list back to a list
            contour = ast.literal_eval(line.strip())
            contours.append(np.array(contour, dtype=np.int32))
    return contours

# Initialize the webcam
cap = cv2.VideoCapture(0)

# Check if the webcam is opened correctly
if not cap.isOpened():
    print("Error: Could not open video device.")
    exit()

# Set video frame width and height
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# Read the contours from the file
contours = read_contours_from_file('contours.txt')

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    
    if not ret:
        print("Failed to grab frame.")
        break

    # Draw the polygons on the current frame
    for contour in contours:
        cv2.polylines(frame, [contour], isClosed=True, color=(0, 255, 0), thickness=2)

    # Display the resulting frame
    cv2.imshow('Frame', frame)

    # Break the loop on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close the window
cap.release()
cv2.destroyAllWindows()
