import speech_recognition as sr

# Initialize recognizer class (for recognizing the speech)
recognizer = sr.Recognizer()

# Use the microphone as the source of the audio
with sr.Microphone() as source:
    print("Adjusting for ambient noise... Please wait")
    recognizer.adjust_for_ambient_noise(source, duration=1)
    print("Listening...")
    
    # Capture the audio from the microphone
    audio = recognizer.listen(source)
    
    try:
        # Recognize speech using Google Web API (you can replace with any other engine like Sphinx)
        text = recognizer.recognize_google(audio)
        print(f"Recognized Text: {text}")
        
    except sr.UnknownValueError:
        print("Sorry, I did not understand the audio")
    except sr.RequestError as e:
        print(f"Could not request results from the service; {e}")
