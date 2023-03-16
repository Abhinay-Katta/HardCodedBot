import speech_recognition as sr
import pyttsx3
import webbrowser
import time
import datetime
import subprocess

engine = pyttsx3.init('sapi5')
# sapi5 is a microsoft text to speech converter for voice recognition
voices = engine.getProperty('voices')
engine.setProperty('voice', 'voices[0].id')

# function to make the bot speak the text


def speak(text):
    engine.say(text)
    engine.runAndWait()

# function to make the bot say shit


def wish_me():
    hour = datetime.datetime.now().hour
    if hour >= 0 and hour < 12:
        speak("Hello, Good Morning")
        print("^    ^")
        print(" \__/ ")
    elif hour >= 12 and hour < 18:
        speak("Hello, Good Afternoon")
        print("^    ^")
        print(" \__/ ")
    else:
        speak("Hello, Good Evening")
        print("^    ^")
        print(" \__/ ")

# function to make the bot listen to your command


def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

        try:
            statement = r.recognize_google(audio, language='en-in')
            print(f"You said: {statement}\n")

        except Exception:
            speak("Pardon me, please say that again")
            return None
        return statement


def logging_off_with_outro():
    for i in range(6):
        print(f"Destroying System32 in {6-i}\n")
        time.sleep(1)


speak("Loading your assistant ")
print("Loading your assistant ")
wish_me()
# driver code

if __name__ == '__main__':
    speak("Tell me, How can I help you... ?")
    strTime = datetime.datetime.now().strftime("%H:%M")
    ins = {
        "time": [lambda:print(strTime), lambda:speak(f"the time is {strTime}")],
        "bye": [lambda:speak('ok your personal assistant is shutting down'), lambda: print('ok your personal assistant is shutting down')],
        "stop": [lambda:speak('ok your personal assistant is shutting down'), lambda: print('ok your personal assistant is shutting down')],
        "open youtube": [lambda:webbrowser.open_new_tab("https://www.youtube.com/"), lambda: speak("opening youtube"), lambda:time.sleep(3)],
        "youtube": [lambda:webbrowser.open_new_tab("https://www.youtube.com/"), lambda:speak("opening youtube"), lambda: time.sleep(3)],
        "open gmail": [lambda:webbrowser.open_new_tab("https://mail.google.com/"), lambda: speak("opening g mail"), lambda: time.sleep(3)],
        "gmail": [lambda:webbrowser.open_new_tab("https://mail.google.com/"), lambda: speak("opening g mail"), lambda: time.sleep(3)],
        "what can you do": [lambda:speak("I am a noob A I . I am programmed to perform simplest shitty tasks such as opening youtube or opening g mail and telling you the time. Thats all i can do for now, but ill be upgraded later in the future, which is pretty doubtfull, to be honest."),
                            lambda:speak("I was built by a dude named Abhi, further details about my guy here are confidential for no reason ")],
        "who are you": [lambda:speak("I am a noob A I . I am programmed to perform simplest shitty tasks such as opening youtube or opening g mail and telling you the time. Thats all i can do for now, but ill be upgraded later in the future, which is pretty doubtfull, to be honest."),
                        lambda:speak("I was built by a dude named Abhi, further details about my guy here are confidential for no reason ")],
        "log off": [lambda:speak("Ok signing off your pc, Have a good day...."), lambda:logging_off_with_outro(),
                    lambda:subprocess.call(["shutdown", "/l"])],
        "spotify": [lambda:webbrowser.open_new_tab("https://open.spotify.com/"), lambda:speak("opening spotify in browser")],
        "open spotify": [lambda:webbrowser.open_new_tab("https://open.spotify.com/"), lambda: speak("opening spotify in browser")]
    }
    while True:
        try:
            statement = take_command()
<<<<<<< HEAD
            print(statement[1])

            if statement == 0:
                continue

            for key in ins.keys():
                if key in statement:
                    for func in ins[key]:
                        func()
        except:
            # statement = input("How can I help you?:\n")
            # print(type(statement))
            statement = take_command()

=======
            if statement == 0:
                statement = input("What do you want?:\n")
                continue
            if "bye" in statement or "stop" in statement:
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
                strTime = datetime.datetime.now().strftime("%H:%M")
                speak(f"the time is {strTime}")
            elif 'who are you' in statement or 'what can you do' in statement:
                speak("I am a noob A I . I am programmed to perform simplest shitty tasks such as opening youtube or opening g mail and telling you the time. Thats all i can do for now, but ill be upgraded later in the future, which is pretty doubtfull, to be honest.")
                speak(
                    "I was built by a dude named Abhi, further details about my guy here are confidential for no reason ")
            elif 'log off' in statement or 'sign out' in statement:
                speak("Ok signing off your pc, Have a good day....")
                subprocess.call(["shutdown", "/l"])
                break
            elif 'open spotify' in statement or 'spotify' in statement:
                webbrowser.open_new_tab("https://open.spotify.com/")
                speak("opening spotify in browser")
            speak("you want anything else...?")
        except:
            statement = take_command()
>>>>>>> aca56ddc5e137fcc99ee472682f6e61ae435cbe6
time.sleep(3)
