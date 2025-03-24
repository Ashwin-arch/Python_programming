import cv2
import mediapipe as mp
import pyautogui

# Initialize Mediapipe Hand Tracking
mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)

# Open Webcam
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Flip the frame horizontally for a mirror effect
    frame = cv2.flip(frame, 1)
    h, w, _ = frame.shape

    # Convert frame to RGB for Mediapipe processing
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb_frame)

    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Get the X-coordinates of key fingers (index and thumb)
            index_x = hand_landmarks.landmark[8].x * w  # Index Finger Tip
            thumb_x = hand_landmarks.landmark[4].x * w  # Thumb Tip

            # Get the Y-coordinates
            index_y = hand_landmarks.landmark[8].y * h
            middle_y = hand_landmarks.landmark[12].y * h

            # Control logic based on hand gestures
            if thumb_x < index_x - 40:
                pyautogui.press('left')  # Move Left
                print("Moving Left")
            elif thumb_x > index_x + 40:
                pyautogui.press('right')  # Move Right
                print("Moving Right")
            elif index_y < middle_y - 20:
                pyautogui.press('up')  # Move Forward
                print("Moving Forward")
            elif index_y > middle_y + 20:
                pyautogui.press('down')  # Move Backward
                print("Moving Backward")

    cv2.imshow("Car Control", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
