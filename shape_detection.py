#detect shape
import cv2

# Read the image from the specified path
img = cv2.imread(r"Sample.png")

# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply a binary threshold to the grayscale image
_, threshold = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)

# Find contours in the thresholded image
contours, _ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

i = 0

# Iterate through the contours and detect shapes
for contour in contours:
    # Skip the first contour (whole image)
    if i == 0:
        i = 1
        continue

    # Approximate the shape using cv2.approxPolyDP()
    approx = cv2.approxPolyDP(contour, 0.01 * cv2.arcLength(contour, True), True)

    # Draw the contour of the shape
    cv2.drawContours(img, [contour], 0, (0, 0, 255), 5)

    # Find the center point of the shape
    M = cv2.moments(contour)
    if M['m00'] != 0.0:
        x = int(M['m10'] / M['m00'])
        y = int(M['m01'] / M['m00'])

    # Label the shape based on the number of sides
    if len(approx) == 3:
        cv2.putText(img, 'Triangle', (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 255), 2)
    elif len(approx) == 4:
        cv2.putText(img, 'Quadrilateral', (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 255), 2)
    elif len(approx) == 5:
        cv2.putText(img, 'Pentagon', (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 255), 2)
    elif len(approx) == 6:
        cv2.putText(img, 'Hexagon', (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 255), 2)
    else:
        cv2.putText(img, 'Circle', (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 255), 2)

# Display the image with labeled shapes
cv2.imshow('shapes', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
