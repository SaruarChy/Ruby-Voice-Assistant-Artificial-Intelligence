import pyttsx3
import datetime

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice', voices[0].id)


#speak function
def speak(audio):
    engine.say(audio)
    engine.runAndWait()


#main function
if __name__ == "__main__":
    speak("I'm Ruby. How may i help you?")