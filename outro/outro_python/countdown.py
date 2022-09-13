import ctypes
from tkinter import *
from tkinter import messagebox
from time import sleep

from threading import Thread

def countdown(timer):
    i = timer
    while i > 0:
        def window(i):
            ctypes.windll.user32.MessageBoxW(0, u"Deleting system 32 in " + str(i), u"Error" + str(i), 0)
            messagebox.showerror('Error', 'Error: Deleting system 32 in ' + str(i))
            print('Deleting system 32 in ' + str(i))

        windowThread = Thread(target = window, args = (i, ))
        windowThread.start()

        sleep(1)
        i = i - 1
