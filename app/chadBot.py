import speech_recognition as sr
import pyttsx3
import pyttsx3.engine
import webbrowser
import time
import datetime
import subprocess
import sys
import threading


class chad_noob_bot:
    def __init__(self) -> None:
        self.engine = pyttsx3.init('sapi5')
        self.voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', self.voices[0].id)
        self.commands = {
            "time": lambda: self.__get_time(),
            "youtube": lambda: self.__open_youtube(),
            "gmail": lambda: self.__open_gmail(),
            "shut down": lambda: self.__shutting_off_with_outro(),
            "who are you": lambda: self.__self_describe()
        }

    def speak(self, text):
        def __say(text):
            self.engine.say(text)
            self.engine.runAndWait()
        speak_thread = threading.Thread(target=__say, args=(text,))
        speak_thread.start()

    def greeting(self):
        hour = datetime.datetime.now().hour
        self.return_wish = ''
        if hour >= 0 and hour < 12:
            self.speak("Hello, Good Morning")
            self.return_wish = "Hello, Good Morning"
            # add morning gif here
        elif hour >= 12 and hour < 18:
            self.speak("Hello, Good Afternoon")
            self.return_wish = "Hello, Good Afternoon"

            # add afternoon gif here
        else:
            self.speak("Hello, Good Evening")
            self.return_wish = "Hello, Good Evening"
        return self.return_wish
        # add evening gif here

    def take_command(self) -> str:
        r = sr.Recognizer()
        try:
            with sr.Microphone() as source:
                audio = r.listen(source)
                statement = r.recognize_google(audio, language='en-in')
                self.speak(
                    "Yes, the bot seems to be working... Its in the try block of take command now ")
                print(f"You said:{statement}\n")
        except Exception as e:
            self.speak("Pardon me, can you say that again?...\n")
            print(f"\nException occured in take_command function : {e}\n")
        return statement

    def __get_time(self):
        return datetime.datetime.now().strftime("%H : %M")

    def __shutting_off_with_outro(self) -> None:
        for i in range(5):
            print(f"Destroying SYSTEM32 in {6-i} seconds..\n")
            time.sleep(1)
        self.speak('ok your personal assistant is shutting down')
        self.text = 'ok your personal assistant is shutting down'

        subprocess.call(["shutdown", "/s"])

    def __open_youtube(self):
        webbrowser.open_new_tab("https://www.youtube.com/")
        self.speak("opening youtube")
        time.sleep(3)

    def __open_gmail(self):
        webbrowser.open_new_tab("https://mail.google.com/")
        self.speak("opening g mail")
        time.sleep(3)

    def __self_describe(self):
        self.speak(
            '''I am a noob A I . I am programmed to perform simplest shitty tasks such 
            as opening youtube or opening g mail and telling you the time. Thats all i can do for now, 
            but ill be upgraded later in the future, which is pretty doubtfull, to be honest. 
            I was built by a dude named Abhi, further details about my guy here are confidential for no reason.
            '''
        )
