# commands.py
import datetime
import wikipedia
import pywhatkit
import webbrowser
from sp import speak

def run_command(command):
    if 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        speak(f"The time is {time}")

    elif 'who is' in command or 'what is' in command:
        person = command.replace('who is', '').replace('what is', '')
        info = wikipedia.summary(person, sentences=2)
        speak(info)

    elif 'play' in command:
        song = command.replace('play', '')
        speak(f"Playing {song}")
        pywhatkit.playonyt(song)
        return True  # <-- Exit after playing

    elif 'open' in command:
        site = command.replace('open', '').strip()
        if 'youtube' in site:
            webbrowser.open("https://youtube.com")
        elif 'google' in site:
            webbrowser.open("https://google.com")
        else:
            webbrowser.open(f"https://{site}.com")
        speak(f"Opening {site}")
        return True  # <-- Exit after opening

    elif 'hello' in command or 'hi' in command:
        speak("Hello! I am always here to assist you.")

    elif 'your name' in command:
        speak("My name is Jarvis.")

    elif 'how are you' in command:
        speak("I'm doing well! Thanks for asking.")

    elif 'exit' in command or 'stop' in command:
        speak("Goodbye!")
        return True  # <-- Exit if user says exit

    else:
        speak("Sorry, I don't understand that yet.")

    return False  # Don't exit by default
