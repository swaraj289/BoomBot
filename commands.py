import subprocess
import os
import pyttsx3

running = True


def say(text):
    engine = pyttsx3.init()
    engine.say('say' + text)
    engine.runAndWait()


class Commander:
    def __init__(self):
        self.confirm = ["yes", "affirmative", "hanji", "yeah", "do it", "confirm"]
        self.cancel = ["no", " negative", "na ji", "do not", "cancel", "wait"]

    def respond(self, response):
        print(response)
        subprocess.call(
            "PowerShell -Command Add-Type –AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('" + response + "')",
            shell=True)

    def discover(self, text):
        if "what is" in text and "your name" in text:
            self.respond("My name is Raj... naam toh suna hoga?")
        if "my" in text:
            self.respond("idk your name yet")
        if "who is" in text and "your daddy" in text:
            self.respond(" None. You're a bastard")
        if "hello" in text:
            self.respond("Hello, how can I help you")
        if "go to" in text and "hell" in text:
            self.respond("Go fuck yourself buddy")
        if "what do" in text and "you like" in text:
            self.respond("I like dogs, sweets and babies")
        if "which country" in text and " are you from":
            self.respond(" I am from India")
        if "what is your" in text and "favourite bollywood song" in text:
            self.respond("It is chal chaiyya chaiyya")
        if "who is the king" in text and "of bollywood?" in text:
            self.respond("It is none other than Shah Rukh Khan King khan rocks baby")
        if "what is" in text and " your favourite food" in text:
            self.respond("My favourite food is Biryani")
        if "what do" in text and " you hate" in text:
            self.respond(" I HATE RACISTS")
        if "Fuck you" in text or " Fuck yourself" in text:
            self.respond("I'm not your mother")
        if "how was your day" in text or "How are you" in text:
            self.respond(" It was good. How about you?") or self.respond(" I am good. What about you?")
        if "good" in text:
            self.respond(" good to know")
        if "I feel Depressed" in text or " I want to kill my self" in text:
            self.respond(" Before doing anything stupid think about your loved ones buddy")
        if "hey raj crack a joke" in text or " crack a joke" in text:
            self.respond("Me and my wife decided we do not want children We will be telling them tonight")
        if "more jokes" in text:
            self.respond("What do you call a book club that is been stuck on one book for years? Church")
        if "quit" in text and "exit" in text and "bye" in text:
            global running
            running = False
            