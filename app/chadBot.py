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
        # self.engine.setProperty('voice', self.voices[0].id)
        self.engine.setProperty('rate', 150)
        self.commands = {
            "time": lambda: self.__get_time(),
            "youtube": lambda: self.__open_youtube(),
            "gmail": lambda: self.__open_gmail(),
            "shut down": lambda: self.__shutting_off_with_outro(),
            "who are you": lambda: self.__self_describe(),

        }

    def speak(self, text) -> None:
        def __say(text):
            self.engine.say(text)
            self.engine.runAndWait()
        speak_thread = threading.Thread(target=__say, args=(text,))
        speak_thread.start()

    def wish_me(self):
        self.hour = self.time
        if self.hour >= 0 and self.hour < 12:
            self.speak("Hello, Good Morning")
            # add morning gif here
        elif self.hour >= 12 and self.hour < 18:
            self.speak("Hello, Good Afternoon")
            # add afternoon gif here
        else:
            self.speak("Hello, Good Evening")
            # add evening gif here

    def take_command(self) -> str:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            audio = r.listen(source)
        try:
            statement = r.recognize_google(audio, language='en-in')
            self.speak(
                "Yes, the bot seems to be working... Its in the try block of take command now ")
            print(f"You said:{statement}\n")
        except:
            self.speak("Pardon me, can you say that again?...\n")
            self.speak("except block")
            statement = r.recognize_google(audio, language='en-in')
        return statement

    def __get_time(self):
        return datetime.datetime().now().hour

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
                   I was built by a dude named Abhi, further details about my guy here are confidential for no reason.'''
        )
    # def run(self):

    #     ins = {
    #         "time": [lambda:print()), lambda:self.speak(f"the time is {strTime}")],
    #         "bye": [lambda:self.speak('ok your personal assistant is shutting down'), lambda: print('ok your personal assistant is shutting down')],
    #         "stop": [lambda:self.speak('ok your personal assistant is shutting down'), lambda: print('ok your personal assistant is shutting down')],
    #         "open youtube": [lambda:webbrowser.open_new_tab("https://www.youtube.com/"), lambda:self.speak("opening youtube"), lambda:time.sleep(3)],
    #         "youtube": [lambda:webbrowser.open_new_tab("https://www.youtube.com/"), lambda:self.speak("opening youtube"), lambda: time.sleep(3)],
    #         "open gmail": [lambda:webbrowser.open_new_tab("https://mail.google.com/"), lambda: self.speak("opening g mail"), lambda: time.sleep(3)],
    #         "gmail": [lambda:webbrowser.open_new_tab("https://mail.google.com/"), lambda: self.speak("opening g mail"), lambda: time.sleep(3)],
    #         "what can you do": [lambda:self.speak("I am a noob A I . I am programmed to perform simplest shitty tasks such as opening youtube or opening g mail and telling you the time. Thats all i can do for now, but ill be upgraded later in the future, which is pretty doubtfull, to be honest."),
    #                             lambda:self.speak("I was built by a dude named Abhi, further details about my guy here are confidential for no reason ")],
    #         "who are you": [lambda:self.speak("I am a noob A I . I am programmed to perform simplest shitty tasks such as opening youtube or opening g mail and telling you the time
