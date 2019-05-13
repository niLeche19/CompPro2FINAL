import pyautogui as pag
from sys import exit

def mpos():
    return(pag.position())

x1 = 0
x2 = 0
y1 = 0
y2 = 0

pag.FAILSAFE = True

while True:
    smid = int(pag.size().width/2)
    x1 = mpos().x
    y1 = mpos().y
    x2 = mpos().x
    y2 = mpos().y
    if mpos().x < smid + 20 and mpos().x > smid - 20 and mpos().y == 0:
        exit()
