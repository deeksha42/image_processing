#program to demonstrate thresholding
import cv2

# Read the image from the specified path
image = cv2.imread(r"Lenna.png")

# Convert the image to grayscale
img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Create a copy of the grayscale image (used for custom thresholding)
img2 = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Types of thresholding techniques (all applied on the grayscale image)
ret, thresh1 = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY)
ret, thresh2 = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY_INV)
ret, thresh3 = cv2.threshold(img, 120, 255, cv2.THRESH_TRUNC)
ret, thresh4 = cv2.threshold(img, 120, 255, cv2.THRESH_TOZERO)
ret, thresh5 = cv2.threshold(img, 120, 255, cv2.THRESH_TOZERO_INV)

# Custom binary threshold function
def binary_threshold(img):
    for i in range(512):
        for j in range(512):
            if img2[i][j] > 120:
                img2[i][j] = 255
            elif img2[i][j] <= 120:
                img2[i][j] = 0
    return img2

# Display the original image and thresholded results
cv2.imshow("original", image)
cv2.imshow("binary threshold", thresh1)
cv2.imshow("custom binary threshold", binary_threshold(img))
cv2.imshow("binary threshold inverted", thresh2)
cv2.imshow("truncated threshold", thresh3)
cv2.imshow("set to 0", thresh4)
cv2.imshow("set to zero inverted", thresh5)

# Wait for a key press and close the windows if the Esc key is pressed
if cv2.waitKey(0) == 27:
    cv2.destroyAllWindows()
