import cv2
import numpy as np

# Function that does nothing; used as a placeholder for trackbars
def nothing(x):
    pass

# Initialize webcam capture
cap = cv2.VideoCapture(0)

# Create a window to hold trackbars
cv2.namedWindow("Trackbars")

# Create trackbars for adjusting lower and upper thresholds
cv2.createTrackbar("LT", "Trackbars", 0, 255, nothing)
cv2.createTrackbar("UT", "Trackbars", 0, 255, nothing)

while True:
    # Capture a frame from the webcam
    ret, frame = cap.read()
    
    # Apply Gaussian blur to the frame
    frame = cv2.GaussianBlur(frame, (9, 9), cv2.BORDER_DEFAULT)
    
    # Flip the frame horizontally (mirror effect)
    image = cv2.flip(frame, 1)
    frame1 = image
    
    # Get the current positions of the lower and upper thresholds from trackbars
    l_h = cv2.getTrackbarPos("LT", "Trackbars")
    l_s = cv2.getTrackbarPos("UT", "Trackbars")
    
    # Convert the frame to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Apply Canny edge detection with the specified lower and upper thresholds
    edged = cv2.Canny(gray, l_h, l_s)
    
    # Convert the edged image to BGR color format
    edgedc = cv2.cvtColor(edged, cv2.COLOR_GRAY2BGR)
    img_bgr = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)
    
    # Stack the original frame, the edged frame, and the grayscale frame side by side
    stacked = np.hstack((frame1, edgedc, img_bgr))
    
    # Resize and display the stacked frames in the "Trackbars" window
    cv2.imshow("Trackbars", cv2.resize(stacked, None, fx=0.4, fy=0.4))
    
    # Wait for a key press; if 'Esc' (key code 27) is pressed, exit the loop
    key = cv2.waitKey(1)
    if key == 27:
        break

# Release the webcam capture
cap.release()

# Close all OpenCV windows
cv2.destroyAllWindows()
