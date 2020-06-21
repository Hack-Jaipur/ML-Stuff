import win32com.client as wincl
import speech_recognition as sr
from nltk.stem import PorterStemmer


def voiceinput():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak Anything :")
        speak = wincl.Dispatch("SAPI.SpVoice")
        speak.Speak("Speak Anything")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            return text
        except:
            print("Sorry could not recognize your voice")


text = voiceinput()
# text = "i am having fever and some cough"

print(text)
