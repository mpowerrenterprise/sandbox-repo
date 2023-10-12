import voicebotutils
from pyfirmata import Arduino, util 

board = Arduino('COM7')                 # Communication Port

left_hand = board.get_pin('d:12:s')     # Left Hand Pin
right_hand = board.get_pin('d:11:s')    # Right Hand Pin
head = board.get_pin('d:10:s')          # Head Pin

left_hand.write(0)      # Left Hand Default Position
right_hand.write(170)   # Right Hand Default Position
head.write(90)          # Head Default Position

while True:

    text = str(voicebotutils.speech_recognizer())    # Speech to Text

    if "right hand up" in text:
        right_hand.write(0)

    elif "left hand up" in text:
        left_hand.write(180)

    elif "right hand down" in text:
        right_hand.write(170)

    elif "left hand down" in text:
        left_hand.write(0)

    elif "hands up" in text or "handsome" in text:
        left_hand.write(180)
        right_hand.write(0)

    elif "hands down" in text:
        left_hand.write(0)
        right_hand.write(170)

    elif "head left" in text:
        head.write(180)

    elif "head right" in text or "headlight" in text:
        head.write(0)

    elif "head forward" in text:
        head.write(90)
    
board.exit()
