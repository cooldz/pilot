from email.mime import audio
import speech_recognition as sr

recognizer = sr.Recognizer()


with sr.Microphone() as source:
    audio = recognizer.listen(source)

    print(recognizer.recognize_sphinx(audio))