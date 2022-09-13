import win32con
import win32api
import time

def change_volume(volume):
    i = 0
    while i < volume / 2:
        win32api.keybd_event(win32con.VK_VOLUME_UP, 0)
        win32api.keybd_event(win32con.VK_VOLUME_UP, 0, win32con.KEYEVENTF_KEYUP)
        time.sleep(0.1)
        i = i + 1

# time.sleep(1) #sleep is just to see the effect, it's not required here

# win32api.keybd_event(win32con.VK_VOLUME_DOWN, 0)
# win32api.keybd_event(win32con.VK_VOLUME_DOWN, 0, win32con.KEYEVENTF_KEYUP)
# time.sleep(1)