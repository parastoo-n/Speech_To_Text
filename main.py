import speech_recognition as sr
import pyttsx3

recognizer = sr.Recognizer()
engine = pyttsx3.init()


#def

def speak_text(command):
     engine.say(command)
     engine.runAndWait()


def listen_and_transcribe():
    with sr.Microphone() as source:
        print("...صحبت")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

        try:
            print("تشخیص دادن...")
            text = recognizer.recognize_google(audio, language="fa-IR")
            print(f"شما گفتید: {text}")
            speak_text(f"شما گفتید: {text}")

        except sr.UnknownValueError:
            print("متاسفم، متوجه نشدم.")
            

if __name__ == "__main__":
    listen_and_transcribe()            
           
        