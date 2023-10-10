import cv2
import mediapipe as mp
import math

# Initialize MediaPipe Pose
mp_pose = mp.solutions.pose
pose = mp_pose.Pose()

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

    # Process the frame and get the pose landmarks
    results = pose.process(frame_rgb)

    # Draw landmarks on the frame
    if results.pose_landmarks:
        mp_drawing.draw_landmarks(
            frame, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

        # Get the landmarks for points 15 and 23
        landmark_15 = results.pose_landmarks.landmark[15]
        landmark_23 = results.pose_landmarks.landmark[23]

        # Calculate the Euclidean distance between points 15 and 23
        distance = math.sqrt((landmark_15.x - landmark_23.x)**2 + (landmark_15.y - landmark_23.y)**2)

        print(distance)

        # Print the formatted distance on the frame
        #cv2.putText(frame, f'Distance 15-23: {formatted_distance}',
                    #(10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # Display the frame with landmarks
    cv2.imshow('Body Pose Detection', frame)

    # Break the loop when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close OpenCV windows
cap.release()
cv2.destroyAllWindows()
