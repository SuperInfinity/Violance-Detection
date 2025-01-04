import pandas as pd
import matplotlib.pyplot as plt
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    print("   ")
    engine.say(audio)
    print("   ")
    engine.runAndWait()


speak("welcome, to ..Jarvis!!!!")


def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("good morning sir!")

    elif hour >= 12 and hour < 18:
        speak("good afternoon sir!")

    else:
        speak("good evening sir!")

    speak("hope your day is going good! ")


def takecommand():
    command = sr.Recognizer()
    with sr.Microphone() as source:
        print('listening....')
        command.pause_threshold = 0.5
        audio = command.listen(source)

        try:
            print("Recognizing....")
            query = command.recognize_google(audio, language='en-in')




        except Exception as Error:
            print("say again please...")
            return "none"

        return query.lower()


speak("hello sir")

query = takecommand()

if 'hello' in query:
    print('ask anything like..')
    print("1. wish me")
    print("2. tell me the time")
    print("3. open youtube, google, telegram, whatsapp and spotify")
    print("4. anything from wikipedia")
    print("5. states list and some other random information")
    print("6. if u want me to stop...just say 'stop listening'")
    speak("hi, so how can i help you?")
    while True:
        query = takecommand().lower()

        if 'wish me' in query:
            wishme()

        elif 'wikipedia' in query:
            speak('searching wikipedia..')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=3)
            speak("according to wikipedia")
            print(results)
            speak(results)


        elif 'open spotify' in query:
            webbrowser.open('spotify.com')



        elif 'open youtube' in query:
            webbrowser.open('youtube.com')



        elif 'open google' in query:
            webbrowser.open('google.com')



        elif 'open whatsapp' in query:
            webbrowser.open('whatsapp.com')




        elif 'open telegram' in query:
            webbrowser.open('telegram.com')



        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir,the time is {strTime}")



        elif 'stop listening' in query:
            break


else:
    speak("no command found")

print('bye sir')
speak("bye bye!!  hope you enjoyed talking!!")