import cv2

# Load an image from the specified file path
img = cv2.imread(r"Lenna.png")

# Convert the image to grayscale
grayimage = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Convert the image to HSV color space
hsvimage = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Convert the image to RGB color space
rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Apply Gaussian blur to the image
blurimage = cv2.GaussianBlur(img, (11, 11), cv2.BORDER_DEFAULT)

# Display the original image
cv2.imshow("Image", img)

# Display the grayscale image
cv2.imshow("Grayscale", grayimage)

# Display the HSV image
cv2.imshow("HSV", hsvimage)

# Display the blurred image
cv2.imshow("Blur", blurimage)

# Display the RGB image
cv2.imshow("RGB", rgb)

# Wait for a key press and close all windows
cv2.waitKey(0)
cv2.destroyAllWindows()
