import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import smtplib
from googletrans import Translator
import time


engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
translator = Translator()


MASTER = "J"
VI = "my name is Sofia"


def talk(text):
    engine.say(text)
    engine.runAndWait()


# SMTP
def send_email(to, content):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login("email", "password")
    server.sendmail("email", to, content)
    server.close()


# This function will wish you as per the current time
def wish_me():
    hour = int(datetime.datetime.now().hour)
    print("\n")
    time = datetime.datetime.now()
    print(time)

    if hour >= 0 and hour < 12:
        talk("Good morning" + MASTER + VI)

    elif hour >= 12 and hour < 18:
        talk("Good afternoon" + MASTER + VI)

    else:
        talk("Good evening" + MASTER + VI)

# Speech recognition
def take_command():
    while True:
        try:
            recognizer = sr.Recognizer()
            microphone = sr.Microphone()
            with microphone as source:
                print("I'm listening...")
                recognizer.adjust_for_ambient_noise(source)
                audio = recognizer.listen(source)
                command = recognizer.recognize_google(audio, language="en-US")
                return command

        except KeyboardInterrupt:
            print("Keyboard Interrupt")
            break

            
def run():
    command = take_command()
    print(command)

    if "play" in command:
        song = command.replace("play", "")
        talk("playing " + song)
        pywhatkit.playonyt(song)

    elif "time" in command:
        _time = datetime.datetime.now().strftime("%I:%M %p")
        talk("Current time is " + _time)

    elif "who's" in command or "what's" in command or "tell me about" in command:
        person = command.replace("what's", "")
        info = wikipedia.summary(person, 3)
        print(info)
        talk(info)

    elif "search" in command:
        intel = command.replace("search", "")
        talk("searching for" + intel)
        pywhatkit.search(intel)
    
    # Very simple translation
    elif "Translate" in command:
        talk("What do you want to translate?")
        text=take_command()
        #time.sleep(3)

        talk("from what language?")
        from_lng = take_command()
        #time.sleep(1)

        talk("to what language")
        to_lng = take_command()
        #time.sleep(1)

        translated = translator.translate(text, dest=to_lng, src=from_lng)
        talk("translating " + text)
        print(translated.text)
        talk(translated.text)

    elif "are you single" in command:
        talk('I am in a relationship with philosophy')

    elif "joke" in command:
        talk(pyjokes.get_joke())

    elif "you are best" in command:
        talk("I know...")

    elif "send email" in command:
        try:
            talk("what should i send")
            content = take_command()

            talk("to who?")
            to = "example@email.com"

            send_email(to, content)
            talk("Email has been sent")

        except Exception as e:
            print(e)        

    else:
        talk("I don't know what are you talking about")
    

