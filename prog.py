from pynput.keyboard import Key, Listener
from sys import exit
import pyautogui as pag

pressed = []
good = 1

def isdown(yy):
    if len(pressed) > 1:
        for i in range(len(pressed)-1):
            if yy != pressed[i]:
                del pressed[i]
    elif len(pressed) == 1:
        if yy != pressed[0]:
            del pressed[0]

def dblprs(k):
    pressed.append(k)
    if k == 'q' or k == 'Q':
        listener.stop()
    pag.press(k)

def on_press(key):
    try:
        if len(pressed) > 0:
            good = 1
            for i in pressed:
                if i == key.char:
                    good = 0
        else:
            good = 1

        if good == 1:
            pressed.append(key.char)
            dblprs(key.char)
    except:
        pass

def on_release(key):
    isdown(key)

with Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()
