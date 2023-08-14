# perform several image processing operations using OpenCV 
import cv2

#capture the video from given file
capture=cv2.VideoCapture(r"sample_video.mp4")

#keep displaying images
while True:

    #read  function that returns two parameters that is boolean result and frames of the video
    result,frame=capture.read()

    #display each frame one by one
    cv2.imshow("Video",frame)

    print(result)
    #display the first 100 second and while displaying if "esc" key pressed, then stop
    if cv2.waitKey(100)== 27:
        break
cv2.destroyAllWindows()