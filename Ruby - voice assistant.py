import pyttsx3
import speech_recognition as sr
import datetime


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice', voices[1].id)


#speak function
def speak(audio):
    engine.say(audio)
    engine.runAndWait()


#wish me function
def wish_me():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour <12:
        speak("Good morning sir.")
    
    elif hour >=12 and hour < 16:
        speak("Good noon sir.")
    
    elif hour >=16 and hour < 18:
        speak("Good afternoon sir.")

    else:
        speak("Good evening sir.")
    
    speak("I'm Ruby. How may I help you?")

#take microphone input from user and returns string output
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query

#main function
if __name__ == "__main__":
    wish_me()
    takeCommand()