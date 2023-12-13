import cv2
from pyfirmata import Arduino, util
import modules.finger_distancer as FingerDistancer

board = Arduino('COM5') # Change 'COM4' to your Arduino's serial port

pwmPin = board.get_pin('d:9:s')     # Digital output pin 13
moterIN1 = board.get_pin('d:6:o')   # Digital output pin 12
moterIN2 = board.get_pin('d:5:o')    # Digital output pin 11

# OpenCV setup
cap = cv2.VideoCapture(0)

# Main loop
while cap.isOpened():
    ret, frame = cap.read()

    # Call the function from the module
    frame, speed = FingerDistancer.main_process(frame)

    pwmPin.write(speed)
    moterIN1.write(1)
    moterIN1.write(1)

    # Display the frame
    cv2.imshow("Display", frame)

    # Break the loop when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()

# Release resources from the fingerdistance module
fingerdistance.release_resources()
