import datetime
import pyttsx3
import speech_recognition as sr 
import webbrowser as wb
from time import sleep
import subprocess
import pyjokes
import os

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voices',voices[1].id) # 0-2 range for different voices
voicespeed = 140 # seeting speed
engine.setProperty('rate',voicespeed)
chrome_path = "C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe %s"


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('listening...')
        r.pause_threshold=1
        audio = r.listen(source)

    try:
        print('Recognising...')
        query = r.recognize_google(audio,language='en-us')
    except Exception as e:
        print('--')
        return '--'
    return query

def time():
    time = datetime.datetime.now().strftime('%H:%M:%S')
    speak(time)
    print(time)

def date():
    day = int(datetime.datetime.now().day)
    month = int(datetime.datetime.now().month)
    year = int(datetime.datetime.now().year)
    speak("The current date is")
    print(day, month, year)
    speak(day)
    speak(month)
    speak(year)

def wishme():
    speak("welcome back ghost")

    hour = datetime.datetime.now().hour
    if hour >= 6 and hour<12:
        speak('Good morning')
    elif hour >= 12 and hour<18:
        speak('Good afternoon')
    elif hour >= 18 and hour<24:
        speak('Good evening')
    else:
        speak('Good night')

    speak('How can i help you my boss')

def open_chrome():
    url = "https://www.google.com"
    wb.get(chrome_path).open(url)

if __name__ == "__main__":
    wishme()
    while True:
        query = takecommand().lower()
        print(query)

        if "good" in query:
            speak("Good morning Sir")

        elif "hi" in query:
            speak("hai bos")

        elif "how are you" in query:
            speak("i am good") 
       

        elif "time" in query:
            time()
 
        elif "date" in query:
            date()
            
        elif "open google" in query:
            speak("google is activated,,,,,,,,,,,,, 3,,,,,,,,,,,,2,,,,,,,,,,1")
            open_chrome()

        elif "close google" in query:
            speak("google is unactive")
            google.terminate()

        elif "search" in query:
            speak("what should i search?")
            search = takecommand().lower()
            wb.get(chrome_path).open_new_tab(search + ".com")
            print(search) 

        elif "info" in query:
            speak(pyjokes.get_jokes())

        elif "logout" in query:
            speak('logging out in 5 second')
            sleep(5)
            os.system("shutdown - l")

        elif "shutdown" in query:
            speak('shutting down in 5 second')
            sleep(5)
            os.system("shutdown /s /t 1")
            
        elif "restart" in query:
            speak('restarting in 5 second')
            sleep(5)
            os.system("shutdown /r /t 1")