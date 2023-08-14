#Apply Canny edge detection function to the image
import cv2

# Load the input image 
img = cv2.imread(r"Lenna.png")

# The numbers 51 and 51 are the lower and upper thresholds for edge detection
edge_detect = cv2.Canny(img, 51, 51)

# Display the final edge detection image in a window named "canny edge detection"
cv2.imshow("canny edge detection", edge_detect)

# Wait for a key press; the program will continue till any key is pressed
cv2.waitKey(0)

# Close all OpenCV windows
cv2.destroyAllWindows()
