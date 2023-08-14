#capture video from webcam and apply gaussian blur
import cv2
import numpy as np 

def nothing(x):
    pass

# Initialize webcam capture
cap = cv2.VideoCapture(0)

# Create a window to hold trackbars
cv2.namedWindow("Trackbars")


#  trackbar value can range from 0 to 20
cv2.createTrackbar("blur", "Trackbars", 0, 20, nothing)

while True:
    # Capture a frame from the webcam
    ret, frame = cap.read()
    
    # Flip the frame horizontally (mirror effect)
    image = cv2.flip(frame, 1)
    
    # Get the current position of the "blur" trackbar
    val = cv2.getTrackbarPos("blur", "Trackbars")
    
    # Compute the kernel size for Gaussian blur
    val = (2 * val) + 1
    
    # Convert the frame to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Apply Gaussian blur to the frame using the computed kernel size
    blur = cv2.GaussianBlur(image, (val, val), cv2.BORDER_DEFAULT)
    
    # Convert the grayscale frame back to BGR color format
    img_bgr = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)
    
    # Stack the original frame, the blurred frame, and the grayscale frame side by side
    stacked = np.hstack((image, blur, img_bgr))
    
    # Display the stacked frames in the "Trackbars" window
    cv2.imshow("Trackbars", cv2.resize(stacked, None, fx=0.8, fy=0.8))
    
    # Wait for a key press; if 'Esc' (key code 27) is pressed, exit the loop
    key = cv2.waitKey(1)
    if key == 27:
        break

# Release the webcam capture
cap.release()

# Close all OpenCV windows
cv2.destroyAllWindows()
