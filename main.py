
import os
import pyttsx3
import speech_recognition as sr
import datetime
import cv2
import wikipedia
from requests import get
import webbrowser
import pywhatkit
import time
import sys
import pyjokes



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices',voices[0].id)


def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

#text to speach
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source, timeout=5, phrase_time_limit=8)

    try:
        print("Recognising...")
        query = r.recognize_google(audio, language='en-us')
        print(f"user said: {query}")
        
    except Exception as e:
        print("some thing went worng..")
        return "none"
    return query
 
def wish():
    speak("Welcome back sir")
    hour = int(datetime.datetime.now().hour)
    
    if hour>=0 and hour<=12:
        speak("Good morning ")
    elif hour>12 and hour<=18:
        speak("good afternoon")
    elif hour>18 and hour<=24:
        speak("good evening ")
    else: 
        speak("good Night")
    speak("how can i help you ")     
    
def date():
    day = int(datetime.datetime.now().day)
    month = int(datetime.datetime.now().month)
    year = int(datetime.datetime.now().year)
    speak("The current date is")
    print(day, month, year)
    speak(day)
    speak(month)
    speak(year)

def time():
    time = datetime.datetime.now().strftime("%H:%M:%S")
    speak(time)
    print(time)

def whatsap():
            speak("Ok sir, tell me the number")
            
            spoken_number = takeCommand().lower()
            
            print(spoken_number)
            length = len(spoken_number)
            if length != 0 and length == 12:
                speak("what should i message")
                code = "+91"
                number_nospace = spoken_number.replace(" ","")
                numb = code + number_nospace
                print(numb)
                message = takeCommand().lower()     
                hour = int(datetime.datetime.now().hour)
                min = int(datetime.datetime.now().minute)
                time_what = min + 1
                pywhatkit.sendwhatmsg(numb, message, hour , time_what)
                time.sleep(120)
            else:
                speak("oh there was some problem pls try again late")
                whatsap()

if __name__ == "__main__":
   
    
    while True:
        
        query = takeCommand().lower()
        
        if "open notepad" in query:
            npath = "C:\\Windows\\notepad.exe"
            os.startfile(npath)
            
        elif "open camera" in query:
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow('webcam', img)
                k = cv2.waitKey(50)
                if k == 27:
                    break
                cap.release()
                
        elif "time" in query:
                time()
        elif "date" in query:
                date()
                
        elif "hello jarvis" in query:
                wish()
                
        elif "wikipedia" in query:
                speak("Searching wikipedia ...")
                query = query.replace("wikipedia", "")
                result = wikipedia.summary(query, sentences=2)
                speak("According to wikipedia")
                speak(result)
                print(result)
                
        elif "IP address" in query:
                ip = get('https://api.ipify.org/').text
                speak = (f"your ip address is {ip}")
                
        elif "whatsapp" in query:
            whatsap()
            
        elif "bye jarvis" in query:
            speak("bye sir see you again. Have a good day")
            sys.exit()
       
        elif "close notepad" in query:
            speak("closing notepad")
            os.system("taskkill /f /im notepad.exe")
            
        elif "tell me a joke" in query:
             joke = pyjokes.get_joke()
             speak(joke)
            