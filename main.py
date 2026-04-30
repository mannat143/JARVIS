# main.py
from sp import speak
from lisn import listen
from commands import run_command

speak("Hello! I am Jarvis. How can I help you today?")

while True:
    command = listen()
    should_exit = run_command(command)
    if should_exit:
        speak("Goodbye!")
        break
