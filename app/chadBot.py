import speech_recognition as sr
import pyttsx3
import pyttsx3.engine
import webbrowser
import time
import datetime
import os
import threading
import pyautogui as pag


class chad_noob_bot:
    def __init__(self) -> None:
        self.engine = pyttsx3.init('sapi5')
        self.voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', self.voices[0].id)
        self.commands = {
            "time": lambda: self. get_time(),
            "youtube": lambda: self. open_youtube(),
            "gmail": lambda: self. open_gmail(),
            "shut down": lambda: self. shutting_off_with_outro(),
            "who are you": lambda: self. self_describe()
        }

    def speak(self, text):

        def __say(text):
            self.engine.say(text)
            self.engine.runAndWait()
            self.engine.stop()
        try:
            speak_thread = threading.Thread(target=__say, args=(text,))
            speak_thread.start()
        except Exception as e:
            print(e)

    def greeting(self) -> str:
        hour = datetime.datetime.now().hour
        if hour >= 0 and hour < 12:
            self.return_greet = "Hello, Good Morning"
            self.speak(self.return_greet)
        elif hour >= 12 and hour < 18:
            self.return_greet = "Hello, Good Afternoon"
            self.speak(self.return_greet)
        else:
            self.return_greet = "Hello, Good Evening"
            self.speak(self.return_greet)
        return self.return_greet

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

    def get_time(self):
        return datetime.datetime.now().strftime("%H : %M")

    def save_and_shut_down(self):
        pag.hotkey('alt', 'tab')
        pag.hotkey('ctrl', 'shift', 'a')
        pag.hotkey('ctrl', 'shift', 's')
        pag.hotkey('ctrl', 'shift', '`')
        time.sleep(2)
        pag.typewrite('git add .')
        pag.press("enter")
        time.sleep(1)
        pag.typewrite('git commit -m "autosave"')
        pag.press("enter")
        time.sleep(3)
        pag.typewrite('git push')
        pag.press("enter")
        time.sleep(5)

        shut_down_warning = "Okay, your system is shutting down. Have a nice day."
        self.speak(shut_down_warning)
        os.system("shutdown /s /t 5")

    def open_youtube(self):
        webbrowser.open_new_tab("https://www.youtube.com/")
        self.speak("opening youtube")
        time.sleep(3)

    def open_gmail(self):
        webbrowser.open_new_tab("https://mail.google.com/")
        self.speak("opening g mail")
        time.sleep(3)

    def self_describe(self):
        self.speak(
            '''I am a noob A I . I am programmed to perform simplest shitty tasks such 
            as opening youtube or opening g mail and telling you the time. Thats all i can do for now, 
            but ill be upgraded later in the future, which is pretty doubtfull, to be honest. 
            I was built by a dude named Abhi, further details about my guy here are confidential for no reason.
            ''')
