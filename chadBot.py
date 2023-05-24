import speech_recognition as sr
import pyttsx3
import pyttsx3.engine
import webbrowser
import time
import datetime
import threading

# TODO:
# 1. Re-Write whole app


class chad_noob_bot:
    def __init__(self) -> None:
        self.engine = pyttsx3.init('sapi5')
        self.voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', self.voices[0].id)
        self.commands = {
            "time": lambda: self.get_time(),
            "youtube": lambda: self.open_youtube(),
            "gmail": lambda: self.open_gmail(),
            "who are you": lambda: self.self_describe()
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
        elif hour >= 12 and hour < 18:
            self.return_greet = "Hello, Good Afternoon"
        else:
            self.return_greet = "Hello, Good Evening"
        self.speak(self.return_greet)
        return self.return_greet

    def take_command(self):
        self.speak("How can I help you?")

        def tc(self):
            try:
                r = sr.Recognizer()
                with sr.Microphone() as source:
                    audio = r.listen(source)
                    print('Speak now: ')
                    self.statement = r.recognize_google(
                        audio, language='en-in')
                    print(f"You said: {self.statement}\n")
                    self.commands[str(self.statement)]()
                    if self.statement == 'exit':
                        return self.statement

            except Exception as e:
                print(e)

        take_command_thread = threading.Thread(target=tc, args=(self,))
        take_command_thread.start()

    def get_time(self):
        self.speak(datetime.datetime.now().strftime("%H : %M"))

    def open_youtube(self):
        webbrowser.open_new_tab("https://www.youtube.com/")
        self.speak("opening youtube")
        time.sleep(3)

    def open_gmail(self):
        webbrowser.open_new_tab("https://mail.google.com/")
        self.speak("opening g mail")
        time.sleep(3)

    def self_describe(self):
        return self.speak(
            '''I am a noob A I . I am programmed to perform simplest shitty tasks such
            as opening youtube or opening g mail and telling you the time. Thats all i can do for now,
            but ill be upgraded later in the future, which is pretty doubtfull, to be honest.
            I was built by a dude named Abhi, further details about my guy here are confidential for no reason.
            ''')
