import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

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
        song = command.replace('play', '')
        talk('playing'+song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I %M %p')  # I is 12 hour format of time
        talk('current time is'+time)
    elif 'who' in command:
        query = command.replace('who', '')
        result = wikipedia.summary(query, 1)
        print(result)
        talk(result)
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'name' in command:
        talk('i am jarvis your personal assistant')
    else:
        talk('please say again')


while True:
    run_jarvis()
