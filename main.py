from pyautogui import *
import pyautogui
import keyboard
import time

# method to find coordinate and color of the pixel which the mouse hovers 
#pyautogui.displayMousePosition()

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def getElecColor(r, g, b):
    if (r == 255 and g == 0 and b == 0):
        return 0 # red
    if (r == 255 and g == 235 and b == 4):
        return 1 # yellow
    if (r == 0 and g == 0 and b == 255):
        return 2 # blue
    if (r == 255 and g == 0 and b == 255):
        return 3 # pink

def getDivertColor(r, g, b):
    if (r == 255 and g == 98 and b == 0):
        return 0 # active
    if (r == 128 and g == 49 and b == 0):
        return 1 # inactive

def isElectricOpen():
    isElec = Point(965, 130) # blue
    isElec2 = Point(950, 130)

    # check the left cable in the top and the middle one
    if (pyautogui.pixel(isElec.x, isElec.y)[0] == 16 and pyautogui.pixel(isElec.x, isElec.y)[1] == 28 and pyautogui.pixel(isElec.x, isElec.y)[2] == 115) \
    and (pyautogui.pixel(isElec2.x, isElec2.y)[0] == 115 and pyautogui.pixel(isElec2.x, isElec2.y)[1] == 0 and pyautogui.pixel(isElec2.x, isElec2.y)[2] == 0):
        return True
    return False

# check the yellow color from the left bar
def isDivertOpen():
    point = pyautogui.pixel(620, 510)
    return point[0] == 253 and point[1] == 255 and point[2] == 92

# check the yellow color from the left triangle
def isDivert2Open():
    point = pyautogui.pixel(515, 525)
    return point[0] == 161 and point[1] == 129 and point[2] == 24

def doElectric():
    leftCables = [Point(568, 273), Point(568, 461), Point(568, 646), Point(568, 830)]

    rightCables = [Point(1310, 273), Point(1310, 461), Point(1310, 646), Point(1310, 830)]

    # for each cable on the left side check the cable on the right side and connect them
    for cable in leftCables:
        leftColor = getElecColor(pyautogui.pixel(cable.x, cable.y)[0], pyautogui.pixel(cable.x, cable.y)[1], pyautogui.pixel(cable.x, cable.y)[2])
        for rightCable in rightCables:
            if not isElectricOpen():
                return
            
            rightColor = getElecColor(pyautogui.pixel(rightCable.x, rightCable.y)[0], pyautogui.pixel(rightCable.x, rightCable.y)[1], pyautogui.pixel(rightCable.x, rightCable.y)[2])
            if leftColor == rightColor:
                pyautogui.moveTo(cable.x, cable.y)
                pyautogui.dragTo(rightCable.x, rightCable.y, 0.6, button='left')
                continue
    print('done connecting wires')

# check all levers if one has the right color and mpve it up
def doDivert():
    levers = [Point(653, 790), Point(747, 790), Point(841, 790), Point(943, 790), Point(1037, 790), Point(1133, 790), Point(1230, 790), Point(1326, 790)]

    for lever in levers:
        color = getDivertColor(pyautogui.pixel(lever.x, lever.y)[0], pyautogui.pixel(lever.x, lever.y)[1], pyautogui.pixel(lever.x, lever.y)[2])

        if color == 0:
            pyautogui.moveTo(lever.x, lever.y)
            pyautogui.dragTo(lever.x, lever.y - 130, 0.3, button='left')

# just click in the middle do do the task
def doDivert2():
    pyautogui.click(x=960, y=540)

# repeatedly check if a game is open
while keyboard.is_pressed('q') == False:
    
    if isElectricOpen():
        doElectric()

    if isDivertOpen():
        doDivert()

    if isDivert2Open():
        doDivert2()
    

