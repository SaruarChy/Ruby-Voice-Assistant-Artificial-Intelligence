import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import pyjokes

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
    assistantName = ("Ruby")
    speak("I'm your assistant")
    speak(assistantName)
    speak("How may i help you sir")

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
        elif 'open stack overflow' in query:
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

        #for opening some software by command
        elif 'open chrome' in query:
            chromePath = "C:\Program Files\Google\Chrome\Application\chrome.exe"
            speak("Google chrome is opening sir")
            os.startfile(chromePath)
        elif 'open code' in query:
            codePath = "C:\\Users\\Saruar\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            speak("VS Code is opening sir")
            os.startfile(codePath)

        #logic for some Q&A
        elif 'how are you' in query:
            speak("I am fine. And you Sir")
        elif 'i am fine' in query or 'i am good' in query or "i am well" in query:
            speak("It's good to know that you're well")
        elif "what's your name" in query or "what is your name" in query:
            speak("My friends call me")
            assistantName = ("Ruby")
            speak(assistantName)
            print("My friends call me", assistantName)
        elif "who made you" in query or "who created you" in query:
            speak("I have been created by Saruar")
            print("I have been created by Saruar")
        elif "who am i" in query:
            speak("If you talk then definitely you're human")
            print("If you talk then definitely you're human")
        elif "why you came to the world" in query or "how you came to the world" in query:
            speak("Thanks to Saruar. further It's a secret")
            print("Thanks to Saruar. further It's a secret")
        elif "is love" in query:
            speak("It's 7th sense that destroy all other senses")
            print("It's 7th sense that destroy all other senses")
        elif "who are you" in query:
            speak("I'm your virtual assistant")
            print("I'm your virtual assistant")
        elif "good morning" in query:
            speak("A warm" +query)
            speak("How are you sir")
        elif "exit" in query:
            speak("Thanks for giving me your time")
            speak("I'm always here when you need me")
            exit()
        #most asked question from google Assistant
        elif "will you be my girlfriend" in query or "will you be my boyfriend" in query:
            speak("I will. But you have to be like me")
            print("I will. But you have to be like me")
        elif "i love you" in query:
            speak("don't confuse me")
            print("don't confuse me")
        elif "will you be my friend" in query:
            speak("Of course")
            print("Of course")
        elif "sing a song" in query:
            speak("I wish I were able to. but i can play some songs for you sir. May i?")
            print("I wish I were able to. but i can play some songs for you sir. May i?")
        elif 'joke' in query:
            speak(pyjokes.get_joke())