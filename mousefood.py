# imports
import pyautogui as pag
from sys import exit
import time

# midpoint and screen bevels
smid = int(pag.size().width/2)
widthh = pag.size().width - 30
heightt = pag.size().height -30

# returns mouse posistion
def mpos():
    return(pag.position())

# program failsafe (top center screen)
def endprog():
    if mpos().x < smid + 20 and mpos().x > smid - 20 and mpos().y == 0:
        exit()

# keeps mouse off the sides of the screen to prevent getting stuck
def checkbounds(x, y):
    if x > 30 and x < widthh:
        if y > 30 and y < heightt:
            return(True)
        elif y < 30:
            pag.move(0,30)
        else:
            pag.move(0, -30)
    elif x < 30:
        pag.move(30)
    else:
        pag.move(-30)


pag.FAILSAFE = True # other failsafe (top left corner)
pag.PAUSE = 0.01 # pause between PAG functions


# main function
while True:
    x1 = mpos().x
    y1 = mpos().y
    time.sleep(0.008) # delay to track mouse movement
    x2 = mpos().x
    y2 = mpos().y
    print(mpos().x,x1,x2,x1 == x2, x2-x1)
    if checkbounds(mpos().x, mpos().y):
        pag.move((x2-x1)* -3, (y2-y1) * -3)
    else:
        pag.move((x2-x1)* 3, (y2-y1) * 3)
    endprog()
