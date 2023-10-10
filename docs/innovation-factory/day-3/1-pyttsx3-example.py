import pyttsx3

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Set properties (optional)
engine.setProperty("rate", 150)  # Speed of speech (words per minute)
engine.setProperty("volume", 1.0)  # Volume (0.0 to 1.0)
#voices = engine.getProperty('voices')
#engine.setProperty('voice', voices[1].id)

# Text to be converted to speech
text = "Hello, this is a text-to-speech example using pyttsx."

# Convert the text to speech and play it
engine.say(text)

# Wait for the speech to finish
engine.runAndWait()
