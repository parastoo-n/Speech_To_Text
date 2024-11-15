import speech_recognition as sr
import pyttsx3

recognizer = sr.Recognizer()
engine = pyttsx3.init()


#def

def speak_text(command):
     engine.say(command)
     engine.runAndWait()