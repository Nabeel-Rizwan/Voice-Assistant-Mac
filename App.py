import pyttsx3
import datetime
import speech_recognition as sr
import pyaudio
import wikipedia
import webbrowser
import os
import subprocess
import time



engine=pyttsx3.init('nsss')                 # nsss voice for mac, for windows use sapi5
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

# if voice [0] then male voice else voice [1] then female voice

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >=0 and hour<12:
        speak('Good Morning!')

    elif hour >=12 and hour <18:
        speak('Good Afternoon!')

    else:
        speak('Good Evening!')        

    speak('Hello, I am Nabeel Made voice assistant and can perform various tasks')    

def takeCommand():
    
    # It takes microphone commands from user then returns string

    r=sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 1
        audio=r.listen(source)

    try:
        print('Recognizing')
        query=r.recognize_google(audio, language='en-US')    
        print(f'User Said: {query}\n')

    except Exception as e:
        print('Say that again Please...')
        speak("Say that again Please")
        return 'None'
    return query
 

if __name__=="__main__":

    wishme()    

    while True:

        query=takeCommand().lower()

        if ('wikipedia' or 'search' or 'information') in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=1) 
            speak("According to Wikipedia")
            speak(results)

        elif 'open youtube' in query:
            speak('Opening Youtube')
            webbrowser.open("https://www.youtube.com/")

        elif 'open google' in query:
            speak('Opening Google')
            webbrowser.open("https://www.google.com/")

        elif 'news' in query:
            speak('Todays news')
            webbrowser.open("https://www.ndtv.com/latest#pfrom=home-ndtv_mainnavgation")    

        elif 'open netflix' in query:
            speak('Opening Netflix')
            webbrowser.open("https://www.netflix.com/in/")

        elif 'open youtube music'  in query:
            speak('Opening Youtube Music')
            webbrowser.open('https://music.youtube.com/')

        elif ('hello' or 'hi' or 'sup' or 'whatsup' or 'hey') in query:
            speak('Hi, how are you')    

        elif 'good' in query:
            speak('Happy to hear that')    

        elif ('bye' or 'quit' or 'exit') in query:
            speak('Bye')
            quit()

        elif 'spotify' in query:
            webbrowser.open('https://open.spotify.com/')    

        elif 'time' in query:
            Time = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {Time}")         

        elif ('about' or 'intro' or 'introduction') in query:
            speak("I'm Nabeel made voice assistant and can perform various tasks. The tasks which can be performed are opening popular webpages like google, youtube, youtube music, etc, Get information from wikipedia and ask me the date and time. This voice assistant script can only work on mac. However, Nabeel has created another version of me which can run on windows too with same functionality.")           

        elif 'date' in query:
            date=datetime.datetime.now()
            speak(f"Sir, the year is {date.year} and the month is {date.month} and the day is {date.day}")

        elif 'wait' in query:
            speak('Sorry')
            time.sleep(1)

        elif ('Hollywood song' or 'Hollywood songs' or 'Hollywood music' or 'music' or 'songs'):
            speak('Playing Songs')
            webbrowser.open('https://music.youtube.com/watch?v=H3yKzgY2J0Q&list=RDCLAK5uy_nTbyVypdXPQd00z15bTWjZr7pG-26yyQ4')

        elif ('bollywood songs' or 'bollywood music') in query:
            speak("Playing Bollywood music")
            webbrowser.open('https://music.youtube.com/watch?v=jpYkoa-uE_c&list=RDCLAK5uy_n9Fbdw7e6ap-98_A-8JYBmPv64v-Uaq1g')



