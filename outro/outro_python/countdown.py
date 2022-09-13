import ctypes
from tkinter import *
from tkinter import messagebox
from time import sleep

from threading import Thread

def countdown(timer):
    i = timer
    while i > 0:
        def window1(i):
            print('Deleting system 32 in ' + str(i))
            messagebox.showerror('Error', 'Error: Deleting system 32 in ' + str(i))
            ctypes.windll.user32.MessageBoxW(0, u"Deleting system 32 in " + str(i), u"Error" + str(i), 0)
            messagebox.showerror('Error', 'Error: Deleting system 32 in ' + str(i))
            ctypes.windll.user32.MessageBoxW(0, u"Deleting system 32 in " + str(i), u"Error" + str(i), 0)
            messagebox.showerror('Error', 'Error: Deleting system 32 in ' + str(i))
            ctypes.windll.user32.MessageBoxW(0, u"Deleting system 32 in " + str(i), u"Error" + str(i), 0)

        windowThread = Thread(target = window1, args = (i, ))
        windowThread.start()


        def window2(i):
            ctypes.windll.user32.MessageBoxW(0, u"Deleting system 32 in " + str(i), u"Error" + str(i), 0)
            messagebox.showerror('Error', 'Error: Deleting system 32 in ' + str(i))
            messagebox.showerror('Error', 'Error: Deleting system 32 in ' + str(i))
            ctypes.windll.user32.MessageBoxW(0, u"Deleting system 32 in " + str(i), u"Error" + str(i), 0)
            messagebox.showerror('Error', 'Error: Deleting system 32 in ' + str(i))
            ctypes.windll.user32.MessageBoxW(0, u"Deleting system 32 in " + str(i), u"Error" + str(i), 0)

        windowThread = Thread(target = window2, args = (i, ))
        windowThread.start()


        sleep(0.9)
        i = i - 1
