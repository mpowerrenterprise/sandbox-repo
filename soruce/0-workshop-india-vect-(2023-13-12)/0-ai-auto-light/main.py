import cv2
import modules.color_detection as ColorDetection
import numpy as np
from pyfirmata import Arduino, util

board = Arduino('COM4') # Change 'COM4' to your Arduino's serial port

red_pin = board.get_pin('d:13:o')     # Digital output pin 13
green_pin = board.get_pin('d:12:o')   # Digital output pin 12
blue_pin = board.get_pin('d:11:o')    # Digital output pin 11

# Open the camera
cap = cv2.VideoCapture(0)

while True:
    # Read a frame from the camera
    ret, frame = cap.read()

    # Get the dominant color in the frame
    color = ColorDetection.get_color(frame)

    if color == "Red":
        red_pin.write(1)

    elif color == "Green":
        green_pin.write(1)

    elif color == "Blue":
        blue_pin.write(1)
    else:
        red_pin.write(0)
        green_pin.write(0)
        blue_pin.write(0)

    # Display the annotated frame
    cv2.imshow('AI AutoLight', frame)

    # Break the loop when 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close all windows
cap.release()
cv2.destroyAllWindows()