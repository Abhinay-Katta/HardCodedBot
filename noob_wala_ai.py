from audioop import tomono
import speech_recognition as sr
import pyttsx3
import webbrowser
import os
import time 
import datetime 
import subprocess


engine =pyttsx3.init('sapi5') 
#sapi5 is a microsoft text to speech converter for voice recognition
voices =engine.getProperty('voices')
engine.setProperty('voice', 'voices[0].id')
def speak(text):
    engine.say(text)
    engine.runAndWait()


def wishMe():
    hour=datetime.datetime.now().hour
    if hour>=0 and hour<12:
        speak("Hello, Good Morning")
        print("^    ^")
        print(" \__/ ")
    elif hour>=12 and hour <18:
        speak("Hello, Good Afternoon")
        print("^    ^")
        print(" \__/ ")
    else :
        speak("Hello, Good Evening")
        print("^    ^")
        print(" \__/ ")
    from os import startfile
    startfile("(path to )giphy.gif")
def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio=r.listen(source)
        
        try:
            statement=r.recognize_google(audio,language='en-in')
            print(f"You said: {statement}\n")

        except Exception :
            speak("Pardon me, please say that again")
            return "None"
        return statement

print("Loading your assistant ")
speak("Loading your assistant ")
wishMe()


if __name__=='__main__':
    speak("Tell me, How can I help you... ?")
    while True:
        statement=takeCommand().lower()
        if statement==0:
            continue
        if "bye" in statement or "fuck off" in statement or "stop" in statement:
            speak('ok your personal assistant is shutting down')
            print('ok your personal assistant is shutting down')
            break
        elif 'open youtube' in statement or 'youtube' in statement:
            webbrowser.open_new_tab("https://www.youtube.com/")
            speak("opening youtube")
            time.sleep(3)
        elif 'open gmail' in statement or 'gmail' in statement:
            webbrowser.open_new_tab("https://mail.google.com/")
            speak("opening g mail")
            time.sleep(3)
        elif 'open kaggle' in statement or 'kaggle' in statement:
            webbrowser.open_new_tab("https://www.kaggle.com/")
            speak("opening kaggle")
        elif 'time' in statement or 'whats the time?' in statement:
            strTime=datetime.datetime.now().strftime("%H:%M")
            speak(f"the time is {strTime}")
        elif 'who are you' in statement or 'what can you do'in statement:
            speak("I am a noob A I . I am programmed to perform simplest shitty tasks such as opening youtube or opening g mail and telling you the time. Thats all i can do for now, but ill be upgraded later in the future, which is pretty doubtfull, to be honest.")
            speak("I was built by a dude named Abhi, further details about my guy here are confidential for no reason ")
        elif 'log off' in statement or 'sign out' in statement:
            speak("Ok signing off your pc, Have a good day....")
            subprocess.call(["shutdown","/l"])
        elif 'open spotify' in statement or 'spotify' in statement:
            webbrowser.open_new_tab("https://open.spotify.com/")
            speak("opening spotify in browser")
#         elif 'bf1' in statement:
#             speak("you would need to turn on the vpn first... dumbass")
#             from os import startfile
#             startfile("")
#             time.sleep(15)
#             speak("Are you done turing on the VPN?... ?" )
#             speak("Let's play some battlefield 1... ")
# SORRY THIS PART IS FOR MYSELF :)
#             from os import startfile
#             startfile(path)
#             speak("Here we go...")
#             break
        speak("you want anything else...?")
            

time.sleep(3)
