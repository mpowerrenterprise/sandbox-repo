import os
import pyttsx3
import playsound

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


while True:
    userInp = input("You: ").lower()

    if userInp == "hello":
        print("Hello, buddy")
    
    elif userInp == "play a song":
        playsound.playsound("kavaala-song.mp3")

    elif userInp == "show me a car image":
        os.system("car-image.jpg")

    elif userInp == "hi":
        engine.say("Hello dear")
        engine.runAndWait()

    elif userInp == "what is your name":
        engine.say("Hi, My name is cool bot")
        engine.runAndWait()


