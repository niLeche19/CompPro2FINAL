from pynput.keyboard import Key, Listener#, Controller
#from sys import exit
import pyautogui as pag

quit = []
pressed = []
good = 1

def lmtof(ee):
    for i in quit:
        if i == ee:
            return(False)
            break
    return(True)

# is called when key is released and removes said key from Pressed
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
    pressed.append(k)
    pag.press(k.char)

def on_press(key):
    # press both shifts to quit program
    if key == Key.shift_r:
        if len(quit) != 0 and lmtof(key):
            listener.stop()
        else:
            quit.append(Key.shift_r)

    if key == Key.shift_l:
        if len(quit) != 0 and lmtof(key):
            listener.stop()
        else:
            quit.append(Key.shift_l)

    # checks if key is pressed from list, dblprs adds keys to avoid infinte loops.
    try:
        if len(pressed) > 0:
            good = 1
            for i in pressed:
                if i == key:
                    good = 0
        else:
            good = 1
    # makes sure the coast is clear and presses.
        if good == 1:
            pressed.append(key)
            dblprs(key)
    except:
        pass

def on_release(key):
    if key == Key.shift_l or key == Key.shift_r:
        del quit[:]
    isdown(key)

# Defines and starts Pynput's built in Listener function.
with Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()
