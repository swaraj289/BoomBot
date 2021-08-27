import pyaudio
import wave
import speech_recognition as sr
import subprocess
import os
import pyttsx3
from commands import Commander


running = True


def say(text):
    subprocess.call("PowerShell -Command Add-Type –AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('"+ text +"')", shell=True)


def play_audio(filename):
    chunk = 1024
    wf = wave.open(filename, 'rb')
    pa = pyaudio.PyAudio()
    stream = pa.open(
        format=pa.get_format_from_width(wf.getsampwidth()),
        channels=wf.getnchannels(),
        rate=wf.getframerate(),
        output=True
    )
    data_stream = wf.readframes(chunk)
    while data_stream:
        stream.write(data_stream)
        data_stream = wf.readframes(chunk)
    stream.close()
    pa.terminate()


r = sr.Recognizer()
cmd = Commander()


def initSpeech():
    print("Talk after the beeep....")
    play_audio("./audio/notification.wav")
    with sr.Microphone() as source:
        print("Say now...")
        audio = r.listen(source)
    play_audio("./audio/notification.wav")
    command = ""
    try:
        command = r.recognize_google(audio)
        cmd.discover(command)
    except:
        print("I dont understand")
    print("You said:")
    print(command)
    if command in ["quit", "exit", "bye", "nikal", "tata", "stop", "stop it"]:
        global running
        running = False
    cmd.discover(command)


while running == True:
    initSpeech()

