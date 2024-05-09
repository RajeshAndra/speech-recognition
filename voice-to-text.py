import speech_recognition as sr
import pyaudio

init_rec = sr.Recognizer()
print("Let's speak!!")
text=""
while text!="Quit":
    with sr.Microphone() as source:
        try:
            audio_data = init_rec.record(source, duration=2)
            text = init_rec.recognize_google(audio_data)
            print(text)
        except Exception as e:
            pass