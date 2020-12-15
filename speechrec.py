import pyttsx3 #text-to-speach
import speech_recognition as sr #speech to text
import datetime 
import wikipedia
import webbrowser 
import os
import smtplib #mail (smtp)
import pyaudio #microphone and speaker


print("initializing Sara ...")

MASTER = "Adi"

engine = pyttsx3.init('espeak') #sAPI (espeak mutiplatform)
voices = engine.getProperty('voices') #list pyttsx.voice.Voice descriptor object
engine.setProperty("voices", voices[0].id)

# try:
#     engine = pyttsx3.init('espeak')
#     voices = engine.getProperty('voices')
#     for voice in voices:
#         print(voices.name)
#     print(voices)
#     engine.setProperty('voice'.voices[0].id)
#     engine.say('This is just a test.')
#     engine.runAndWait()
#     input('Press enter to exit.')
# except:
#     print('error')

#speak
def speak(text):
    engine.say(text)
    engine.runAndWait() #

#function Wish
def wishMe():
    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour < 12:
        speak("Good morning" + MASTER)
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon" + MASTER)
    else:
        speak("Good Evening" + MASTER)
        speak("")

#microphone
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening ...")
        audio = r.listen(source)
    
    try:
        print("Recognizing ...")
        query = r.recognize_google(audio, language="en-us")
        print(f"User Said:", (query))

    except Exception :
        query = r
        speak("Say that again please")
    return query

#Main start here
wishMe()
speak("Hello my name is Sara, can i help you?")
query = takeCommand()

#logic for task as per query

if 'wikipedia' in query.lower():
    speak("searching wikipedia...")
    query = query.replace("wikipedia", "")
    results = wikipedia.summary(query, sentences=2)
    speak("According to wikipedia")
    print(results)
    speak(results)
elif "open youtube" in query.lower():
    speak("Opening Youtube")
    url = "youtube.com"
    chrome_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
    webbrowser.get(chrome_path).open(url)
        
elif "open google" in query.lower():
    speak("Opening Google")
    url = "google.com"
    chrome_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
    webbrowser.get(chrome_path).open(url)
else:
    speak("thank you, have a nice day")
# except:
#     query