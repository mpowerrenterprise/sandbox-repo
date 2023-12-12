import cv2
import colordetection
import numpy as np
from pyfirmata import Arduino, util

board = Arduino('COM4') # Change 'COM4' to your Arduino's serial port

red_pin = board.get_pin('d:13:o')     # Digital output pin 13
green_pin = board.get_pin('d:12:o')   # Digital output pin 12
blue_pin = board.get_pin('d:11:o')    # Digital output pin 11

# Open the camera
cap = cv2.VideoCapture(2)

while True:
    # Read a frame from the camera
    ret, frame = cap.read()

    if not ret:
        print("Error reading frame")
        break

    # Get the dominant color in the frame
    dominant_color = colordetection.get_dominant_color(frame)

    # Draw the dominant color on the frame
    cv2.putText(frame, f"Dominant Color: {dominant_color}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)


    if dominant_color == "Red":
        red_pin.write(1)

    elif dominant_color == "Green":
        green_pin.write(1)

    elif dominant_color == "Blue":
        blue_pin.write(1)
    else:
        red_pin.write(0)
        green_pin.write(0)
        blue_pin.write(0)


    # Display the annotated frame
    cv2.imshow('Dominant Color Detection', frame)

    # Break the loop when 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close all windows
cap.release()
cv2.destroyAllWindows()