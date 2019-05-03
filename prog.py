from pynput.keyboard import Key, Listener
from sys import exit
import pyautogui as pag

pressed = []
good = 1

def isdown(kiki):
    # used to see what key has been lifted and remove it from the list
    if len(pressed) > 1:
        for i in range(len(pressed)-1):
            if kiki != pressed[i]:
                del pressed[i]
    # need a case for 1 item because of the function of the first part
    elif len(pressed) == 1:
        if kiki != pressed[0]:
            del pressed[0]
            
# presses the given key again, adds the key to a list quits wtih 'q'
def dblprs(k):
    pressed.append(k)
    if k == 'q' or k == 'Q':
        listener.stop()
    pag.press(k)


def on_press(key):
    try: # checks for char or other
        if len(pressed) > 0:
            # makes sure the key isn't already pressed
            good = 1
            for i in pressed:
                if i == key.char:
                    good = 0
        else:
            good = 1
        # calls doublepress and adds key to list if good
        if good == 1:
            pressed.append(key.char)
            dblprs(key.char)
    except:
        print(key)

# deletes key that has been released from the pressed list
def on_release(key):
    isdown(key)

with Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()
