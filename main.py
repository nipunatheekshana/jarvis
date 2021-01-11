import speech_recognition as sr
import pyttsx3
import pywhatkit

listner = sr.Recognizer()
engine = pyttsx3.init()


def talk(word):
    engine.say(word)
    engine.runAndWait()


def receive_command():
    try:
        with sr.Microphone() as source:
            talk("yes sir")
            voice = listner.listen(source)
            command = listner.recognize_google(voice)
            command = command.lower()
            if 'jarvis' in command:
                command = command.replace('jarvis', '')
                talk(command)

    except:
        pass
    return command


def run_jarvis():
    command = receive_command()
    print(command)
    if 'play' in command:
        song=command.replace('play','')
        talk('playing'+song )
        pywhatkit.playonyt(song)


run_jarvis()