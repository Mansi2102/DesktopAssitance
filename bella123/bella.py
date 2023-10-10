import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")
    elif hour>=12 and hour<18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    
    speak("Hello! My name is Bella. How May I help you?")

def takeCommand():
    #it takes microphone input from user and return string output
    r=sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("Listening...")
        r.pause_threshold=1
        audio=r.listen(source,timeout=3, phrase_time_limit=3)
    try:
        print("Recognizing...")
        query=r.recognize_google(audio)
        print(f"user said:,{query}\n")
    except Exception as e:
        print("Say that again please")
        return "None"
    return query

def new_func(takeCommand):
    query=takeCommand().lower()
    return query


if __name__=="__main__":
    wishMe()
    while True:
        query = new_func(takeCommand)

        #logic for executing task based on query
        if 'wikipedia' in query:
            speak("Searching wikipedia...")
            query=query.replace("wikipedia","") 
            results=wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        

        elif 'the time' in query:

            
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is:,{strTime}")
        elif 'open vs code' in query:
            codePath="C:\\Users\\lenovo\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        elif 'open notepad' in query:
            editorPath="%windir%\\system32\\notepad.exe"
            os.startfile(editorPath)
        elif 'who are you' in query:
            speak("Hello I am your virtual assistance and my name is Bella and I am here to make your life easier")

        elif 'who am i' in query:
            speak("You are probably a human")

        elif 'how are you' in query:
            speak("I am fine,Thank you! how are you?")

        elif 'i am fine' or 'i am good' in query:
            speak("Thats great")

