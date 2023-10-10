import cv2
import math
import playsound
import mediapipe as mp

# Initialize MediaPipe Hand
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()

# Initialize MediaPipe Drawing
mp_drawing = mp.solutions.drawing_utils

# Initialize OpenCV for webcam input
cap = cv2.VideoCapture(0)

while cap.isOpened():
    # Read a frame from the webcam
    ret, frame = cap.read()
    if not ret:
        continue

    # Convert the frame to RGB for MediaPipe
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process the frame and get hand landmarks
    results = hands.process(frame_rgb)

    # Draw hand landmarks on the frame
    if results.multi_hand_landmarks:
        for landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(
                frame, landmarks, mp_hands.HAND_CONNECTIONS)

            # Get the landmarks for points 4 and 8
            landmark_4 = landmarks.landmark[4]
            landmark_8 = landmarks.landmark[8]

            # Calculate the Euclidean distance between points 4 and 8
            distance = math.sqrt((landmark_4.x - landmark_8.x)**2 + (landmark_4.y - landmark_8.y)**2)

            if(distance < 0.04):
                playsound.playsound("beep-sound.mp3")
                



    # Display the frame with hand landmarks
    cv2.imshow('Hand Landmark Detection', frame)

    # Break the loop when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close OpenCV windows
cap.release()
cv2.destroyAllWindows()
