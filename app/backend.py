import datetime
import speech_recognition as sr
import pyttsx3
import webbrowser as wb
import threading


class HardCodedBot:
    def __init__(self) -> None:
        self.engine = pyttsx3.init('sapi5')
        self.voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', self.voices[0].id)

    def speak(self, text):
        thread_function = threading.Thread(
            target=self.speak_thread, args=(text,))
        thread_function.start()
        thread_function.is_alive()

    def speak_thread(self, text):
        self.engine.say(text=text)
        self.engine.runAndWait()
        self.engine.stop()

    def take_input(self):
        try:
            r = sr.Recognizer()
            with sr.Microphone() as source:
                audio = r.listen(source)
                self.statement = r.recognize_google(
                    audio_data=audio, language='en-in')
                return self.statement
        except Exception as e:
            raise Exception(e)

    def get_time(self) -> str:
        return datetime.datetime().now().strftime("%H:%M")

    def open_from_web(self, tab):
        tabs = {
            'gmail': 'mail.google.com',
            'youtube': 'www.youtube.com',
            'spotify': 'open.spotify.com',

        }
        return wb.open_new_tab(tabs[tab])
