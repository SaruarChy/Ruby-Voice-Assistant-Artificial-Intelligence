import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os

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
    while True:
        query = takeCommand().lower()
        # Logic for executing tasks based on query

        #for the results from wikipedia
        if 'wikipedia' in query:
            speak('Searching wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query,sentences = 2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        
        #for opening some popular websites
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
        elif 'open github' in query:
            webbrowser.open("github.com")
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open facebook' in query:
            webbrowser.open("facebook.com")
        elif 'open instagram' in query:
            webbrowser.open("instagram.com")
        elif 'open codeforces' in query:
            webbrowser.open("codeforces.com")
        elif 'open codechef' in query:
            webbrowser.open("codechef.com")
        
        #for playing musics
        elif 'play music' in query or "play song" in query:
            speak("Here you go with music")
            music_dir = 'C:\\Users\\Saruar\\Music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        #for telling the time
        elif 'time now' in query or "the time" in query:
            timeNow = datetime.datetime.now().strftime("%H:%M:%S")
            print(timeNow)
            speak(f"Sir, the time is{timeNow}") 