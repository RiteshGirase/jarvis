# import speech_recognition as sr
import pyttsx3
def speak(cmd):
    engine = pyttsx3.init()
    engine.say(cmd )
    print(cmd )
    engine.runAndWait()
    return

