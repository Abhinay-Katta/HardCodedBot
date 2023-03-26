import pyttsx3

engine = pyttsx3.init()

# start the event loop


def speak(text):
    engine.startLoop()

    # speak some text
    engine.say(text)

    # do some other work while the text is being spoken
    print("The text is being spoken...")
    for i in range(10):
        print(i)

    # end the event loop
    engine.endLoop()


speak("hello motherfucker")
