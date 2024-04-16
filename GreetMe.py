import pyttsx3
import datetime

engine=pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice",voices[1].id)
engine.setProperty("rate",170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def greetMe():
    hour =int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("Good Morning, Ritik Bhai")  
    elif hour>12 and hour<=18:
        speak("Good Afternoon, Ritik Bhai")

    else:
        speak("Good Evening,Ritik Bhai")

    speak("Please tell me, How can I help you ? ")       
