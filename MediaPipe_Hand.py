#real-time hand tracking using the MediaPipe library
import cv2
import time
import mediapipe as mp

# Initialize the webcam
cap = cv2.VideoCapture(0)

# Initialize the hand tracking module from MediaPipe
mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

# Initialize variables for tracking time
pTime = 0
cTime = 0

while True:
    # Capture a frame from the webcam
    success, img = cap.read()

    # Convert the frame to RGB format (required for MediaPipe)
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # Process the frame to detect hand landmarks
    results = hands.process(imgRGB)

    # If hand landmarks are detected
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):
                lm_l = []
                h, w, c = img.shape
                # Calculate pixel coordinates for landmarks
                cx, cy = int(lm.x * w), int(lm.y * h)
                lm_l.append([id, cx, cy])
                #print(lm_l)
            
            # Draw hand landmarks and connections on the frame
            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

    # Calculate frames per second (FPS)
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    # Display FPS on the frame
    cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)

    # Display the processed frame
    cv2.imshow("Image", img)

    # Break the loop when the 'Esc' key (key code 27) is pressed
    if cv2.waitKey(1) == 27:
        break

# Release the webcam and close OpenCV windows
cap.release()
cv2.destroyAllWindows()
