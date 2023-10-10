import speech_recognition as sr

while True:

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source, phrase_time_limit=5)
        #audio = r.listen(source)

        try:
            text = r.recognize_google(audio)
            print("Recognizing...")
            dataText = format(text.strip())
            print(f"Out: {dataText}")

        except Exception as e:
            print(e)
