import numpy as np
import cv2
 
 
# Capturing video through webcam
img = cv2.imread(r"Sample.png")


# Convert the imageFrame in BGR(RGB color space) to HSV(hue-saturation-value) color space
hsvFrame = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)


# Set range for red color and define mask
red_lower = np.array([0,50,50], np.uint8)
red_upper = np.array([10, 255, 255], np.uint8)
red_mask = cv2.inRange(hsvFrame, red_lower, red_upper)
cv2.imshow("red mask",red_mask)

# Set range for green color and define mask
green_lower = np.array([25, 52, 72], np.uint8)
green_upper = np.array([102, 255, 255], np.uint8)
green_mask = cv2.inRange(hsvFrame, green_lower, green_upper)
cv2.imshow("green mask",green_mask)

# Set range for blue color and define mask
blue_lower = np.array([94, 80, 2], np.uint8)
blue_upper = np.array([120, 255, 255], np.uint8)
blue_mask = cv2.inRange(hsvFrame, blue_lower, blue_upper)
cv2.imshow("blue mask",blue_mask)  
# Morphological Transform, Dilation for each color and bitwise_and operator between img and mask determines to detect only that particular color
kernal = np.ones((5, 5), "uint8")
   
# For red color
red_mask = cv2.dilate(red_mask, kernal)
res_red = cv2.bitwise_and(img, img,
                            mask = red_mask)
cv2.imshow("and",res_red)


# For green color
green_mask = cv2.dilate(green_mask, kernal)
res_green = cv2.bitwise_and(img, img,
                            mask = green_mask)
   
# For blue color
blue_mask = cv2.dilate(blue_mask, kernal)
res_blue = cv2.bitwise_and(img, img,
                            mask = blue_mask)


# Creating contour to track red color
contours, hierarchy = cv2.findContours(red_mask,
                                        cv2.RETR_TREE,
                                        cv2.CHAIN_APPROX_SIMPLE)

print(contours)

for pic, contour in enumerate(contours):
    area = cv2.contourArea(contour)
    if(area > 300):
        x, y, w, h = cv2.boundingRect(contour)
        img = cv2.rectangle(img, (x, y),
                                    (x + w, y + h),
                                    (0, 0, 255), 2)
           
        cv2.putText(img, "Red Colour", (x, y),
                    cv2.FONT_HERSHEY_SIMPLEX, 1.0,
                    (0, 0, 255))    


# Creating contour to track green color
contours, hierarchy = cv2.findContours(green_mask,
                                        cv2.RETR_TREE,
                                        cv2.CHAIN_APPROX_SIMPLE)
   
for pic, contour in enumerate(contours):
    area = cv2.contourArea(contour)
    if(area > 300):
        x, y, w, h = cv2.boundingRect(contour)
        img = cv2.rectangle(img, (x, y),
                                    (x + w, y + h),
                                    (0, 255, 0), 2)
           
        cv2.putText(img, "Green Colour", (x, y),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1.0, (0, 255, 0))


# Creating contour to track blue color
contours, hierarchy = cv2.findContours(blue_mask,
                                        cv2.RETR_TREE,
                                        cv2.CHAIN_APPROX_SIMPLE)
for pic, contour in enumerate(contours):
    area = cv2.contourArea(contour)
    if(area > 300):
        x, y, w, h = cv2.boundingRect(contour)
        img = cv2.rectangle(img, (x, y),
                                    (x + w, y + h),
                                    (255, 0, 0), 2)
           
        cv2.putText(img, "Blue Colour", (x, y),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1.0, (255, 0, 0))
           
# Program Termination
cv2.imshow("Multiple Color Detection for Image", img)
cv2.waitKey(0)
