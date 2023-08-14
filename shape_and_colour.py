#detect shape and colour
import cv2
import numpy as np

# Read the image
img = cv2.imread(r"Sample.png")

# Define the color ranges as dictionaries
lower_hsv = {'red': ([0, 50, 50]), 'green': ([40, 52, 72]), 'blue': ([94, 80, 2]),
             'yellow': ([25, 255, 255]), 'orange': ([10, 100, 100])}
upper_hsv = {'red': ([10, 255, 255]), 'green': ([102, 255, 255]), 'blue': ([120, 255, 255]),
             'yellow': ([35, 255, 255]), 'orange': ([25, 255, 255])}

# Convert the image to HSV color space
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Create a list to store shape-color-centroid information
shape_color_centroid_list = []

for (key, value) in upper_hsv.items():
    # Create a mask for each color range
    lower_color = np.array(lower_hsv[key], np.uint8)
    upper_color = np.array(upper_hsv[key], np.uint8)
    mask = cv2.inRange(hsv, lower_color, upper_color)
    
    # Find contours in the masked image
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    for contour in contours:
        shape = ""
        # Detect the shape based on the number of sides
        approx = cv2.approxPolyDP(contour, 0.01 * cv2.arcLength(contour, True), True)
        
        # Calculate the centroid of the shape
        M = cv2.moments(contour)
        if M['m00'] != 0.0:
            x = int(M['m10'] / M['m00'])
            y = int(M['m01'] / M['m00'])
        
        # Determine the shape based on the number of sides
        if len(approx) == 3:
            shape = "Triangle"
        elif len(approx) == 4:
            (x1, y1, w, h) = cv2.boundingRect(approx)
            if (float(w) / h) >= 0.955 and (float(w) / h) <= 1.1:
                shape = "Square"
            else:
                shape = "Rectangle"
        elif len(approx) == 5:
            shape = "Pentagon"
        elif len(approx) == 6:
            shape = "Hexagon"
        else:
            shape = "Circle"
        
        # Add shape-color-centroid information to the list
        shape_color_centroid_list.append([key, shape, (x, y)])

# Print the shape-color-centroid information list
print(shape_color_centroid_list)
