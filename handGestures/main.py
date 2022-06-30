# Necessary libraries
import cv2
import mediapipe as mp
import controller as cnt

drawing = mp.solutions.drawing_utils
hand = mp.solutions.hands

# Needed to detect the fingers
arrayForTips = [4, 8, 12, 16, 20]

# Capture the live video
video = cv2.VideoCapture(0)

# Using mediapipe
with hand.Hands(min_detection_confidence=0.5, min_tracking_confidence=0.5) as hands:
    while True:
        # Read all frames
        flag, img = video.read()

        # Convert BGR color format to RGB just to store in a different variable where writeable is false
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img.flags.writeable = False
        results = hands.process(img)
        img.flags.writeable = True

        # Undo the conversion
        img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

        # An array to store indices
        arr = []

        # If we find location of hand
        if results.multi_hand_landmarks:

            # Go for each points
            for location in results.multi_hand_landmarks:
                myHands = results.multi_hand_landmarks[0]
                for i, lm in enumerate(myHands.landmark):
                    h, w, c = img.shape
                    cx, cy = int(lm.x * w), int(lm.y * h)

                    # Storing the position
                    arr.append([i, cx, cy])

                # drawing positions
                drawing.draw_landmarks(img, location, hand.HAND_CONNECTIONS)

        # An array that will give us the answer
        fingers = []

        # If we have the hand detected
        if len(arr) != 0:

            # This is for all the remaining fingers
            for i in range(1, 5):
                if arr[arrayForTips[i]][2] < arr[arrayForTips[i] - 2][2]:
                    fingers.append(1)
                else:
                    fingers.append(0)

            # Special case of thumb detection
            if arr[arrayForTips[0]][1] > arr[arrayForTips[0] - 1][1]:
                fingers.append(1)
            else:
                fingers.append(0)

            # Count the number of fingers raised
            total = fingers.count(1)

            # Now call the controller.py file
            cnt.led(total)

            # Display the number pertaining to the total fingers
            if total == 0:
                cv2.rectangle(img, (20, 300), (400, 425), (0, 0, 0), cv2.FILLED)
                cv2.putText(img, "LIGHT OFF", (45, 375), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 0, 255), 5)

            elif total == 1:
                cv2.rectangle(img, (20, 300), (400, 425), (0, 0, 0), cv2.FILLED)
                cv2.putText(img, "LIGHT  ON", (45, 375), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 0, 255), 5)

        # Display the frame
        cv2.imshow("Image", img)

        # If user presses 'q', then code will be stopped
        k = cv2.waitKey(1)
        if k == ord('q') or k == ord('Q'):
            break

# Destroying and releasing the needed windows
video.release()
cv2.destroyAllWindows()