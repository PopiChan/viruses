from time import sleep
import playsound
import os

def play_music():
    print("you messed up")
    outro_path = str(f'{os.path.dirname(__file__)}\Outro-Music.mp3')
    playsound.playsound(outro_path)

