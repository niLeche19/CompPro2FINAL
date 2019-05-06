from pynput.keyboard import Key, Listener
from sys import exit
import pyautogui as pag

pressed = []
good = 1

def prlst():
    while True:
        print(pressed)

# is called when key is released and removes key from Pressed
def isdown(kiki):
    try:
        for i in range(len(pressed)):
            if kiki == pressed[i]:
                del pressed[i]
    except:
        if pressed[0] == kiki:
            del pressed[0]

# press the key again
def dblprs(k):
    if k.char == 'q' or k.char == 'Q':
        listener.stop()
    pressed.append(k)
    pag.press(k.char)

def on_press(key):
    # checks if key is pressed from list, dblprs adds keys to avoid infinte loops.
    try:
        if len(pressed) > 0:
            good = 1
            for i in pressed:
                if i == key:
                    good = 0
        else:
            good = 1
    # makes sure that a doublepress is not occurring and presses accordingly.
        if good == 1:
            print('pressing!!')
            pressed.append(key)
            dblprs(key)
    except:
        pass

def on_release(key):
    isdown(key)

# defines and starts the built in Listener with Pynput
with Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()
