import cv2
import math
import numpy as np
import mediapipe as mp


# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()

# Function to calculate distance between two points
def calculate_distance(point1, point2):
    return math.sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)


def main_process(frame):

    # Flip the frame horizontally for a later selfie-view display
    frame = cv2.flip(frame, 1)

    # Convert the BGR image to RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process the frame with MediaPipe Hands
    results = hands.process(rgb_frame)

    volume = 0

    # Check if hands are detected
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            # Get landmarks for index finger (Landmark 8) and thumb (Landmark 4)
            index_finger = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP.value]
            thumb = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP.value]

            # Calculate distance between index finger and thumb
            distance = calculate_distance((index_finger.x, index_finger.y), (thumb.x, thumb.y))

            # Map the distance to a volume range (adjust as needed)
            volume = int(np.interp(int(distance * 100), [5, 60], [0, 255]))

            # Draw a line between index finger and thumb
            cv2.line(frame, (int(index_finger.x * frame.shape[1]), int(index_finger.y * frame.shape[0])),
                     (int(thumb.x * frame.shape[1]), int(thumb.y * frame.shape[0])), (0, 255, 0), 2)

            # Draw small red circles at the ends of index finger and thumb
            cv2.circle(frame, (int(index_finger.x * frame.shape[1]), int(index_finger.y * frame.shape[0])), 5, (0, 0, 255), -1)
            cv2.circle(frame, (int(thumb.x * frame.shape[1]), int(thumb.y * frame.shape[0])), 5, (0, 0, 255), -1)
            # Display the volume on the top left corner
            cv2.putText(frame, f"Speed: {volume}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)

    return frame, volume


def release_resources():
    # Release the hands object
    hands.close()

# Make sure to call release_resources() when done
