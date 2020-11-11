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

def dragIt(x, y, time):
    pyautogui.mouseDown(button='left')
    pyautogui.moveTo(x, y, time)
    pyautogui.mouseUp(button='left')

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
                dragIt(rightCable.x, rightCable.y, 0.01)
                break
    print('done connecting wires')

# check the yellow color from the left bar
def isDivertOpen():
    point = pyautogui.pixel(620, 510)
    return point[0] == 253 and point[1] == 255 and point[2] == 92

# check all levers if one has the right color and mpve it up
def doDivert():
    levers = [Point(653, 790), Point(747, 790), Point(841, 790), Point(943, 790), Point(1037, 790), Point(1133, 790), Point(1230, 790), Point(1326, 790)]

    for lever in levers:
        color = getDivertColor(pyautogui.pixel(lever.x, lever.y)[0], pyautogui.pixel(lever.x, lever.y)[1], pyautogui.pixel(lever.x, lever.y)[2])

        if color == 0:
            pyautogui.moveTo(lever.x, lever.y)
            pyautogui.dragTo(lever.x, lever.y - 130, 0.3, button='left')

# check the yellow color from the left triangle
def isDivert2Open():
    point = pyautogui.pixel(515, 525)
    return point[0] == 161 and point[1] == 129 and point[2] == 24

# just click in the middle do do the task
def doDivert2():
    pyautogui.click(x=960, y=540)
    time.sleep(2)

def isAlignEngineOpen():
    point1 = pyautogui.pixel(515, 525)

def isAdminCardOpen():
    point = pyautogui.pixel(847, 834)
    return point[0] == 189 and point[1] == 211 and point[2] == 181

def doAdminCard():
    pyautogui.click(x=847, y=834)
    time.sleep(0.7)
    pyautogui.moveTo(520, 420)
    dragIt(1500, 420, 0.6)
    time.sleep(0.1)
    red = pyautogui.pixel(1270, 320)
    if red[0] == 255 and red[1] == 0 and red[2] == 0:
        doAdminCard()
    
    # wait a few seconds, because card will go back down and it would do the task again
    time.sleep(3)  

def isDownloadOpen():
    point = pyautogui.pixel(700, 480)
    point2 = pyautogui.pixel(1200, 480)
    return point[0] == 241 and point[1] == 212 and point[2] == 161 and \
    point2[0] == 241 and point2[1] == 212 and point2[2] == 161

def doDownload():
    pyautogui.click(x=950, y=660)
    time.sleep(10)

def isStabilization():
    point = pyautogui.pixel(920, 580)
    return point[0] == 54 and point[1] == 152 and point[2] == 218

def doStabilization():
    pyautogui.click(x=960, y=540)
    time.sleep(2)

def isFuelOpen():
    point = pyautogui.pixel(1305, 840)
    return point[0] == 173 and point[1] == 46 and point[2] == 0

def doFuel():
    pyautogui.moveTo(1450, 888)
    pyautogui.mouseDown()
    time.sleep(3.3)
    pyautogui.mouseUp()
    time.sleep(1)

def isSieldsOpen():
    point = pyautogui.pixel(825, 150)
    point2 = pyautogui.pixel(880, 940)
    return point[0] == 30 and point[1] == 73 and point[2] == 145 and \
        point2[0] == 30 and point2[1] == 73 and point2[2] == 145

def doShields():
    shields = [Point(830, 390), Point(960, 390), Point(1140, 390), Point(950, 530), Point(790, 750), Point(930, 750), Point(1170, 750)]

    # check all shields and click if its red
    for shield in shields:
        print(shield.x, shield.y)
        if pyautogui.pixel(shield.x, shield.y)[0] == 202 and \
            pyautogui.pixel(shield.x, shield.y)[1] > 81 and pyautogui.pixel(shield.x, shield.y)[1] < 107 and \
            pyautogui.pixel(shield.x, shield.y)[2] > 99 and pyautogui.pixel(shield.x, shield.y)[2] < 125:
           pyautogui.click(shield.x, shield.y)
    print('done doing shields')

def isGarbageOpen():
    point = pyautogui.pixel(1190, 405)
    point2 = pyautogui.pixel(1355, 405)
    
    return point[0] == 145 and point[1] == 175 and point[2] == 187 and \
        point2[0] == 145 and point2[1] == 175 and point2[2] == 187

def doGarbage():
    print('doing garbage')
    time.sleep(0.5)
    pyautogui.moveTo(1265, 420)
    pyautogui.mouseDown(button='left')
    pyautogui.moveTo(1265, 850, 0.5)
    time.sleep(1.2)
    pyautogui.mouseUp(button='left')

def isAsteroidOpen():
    point = pyautogui.pixel(580, 915)
    point2 = pyautogui.pixel(1337, 915)
    
    return point[0] == 34 and point[1] == 109 and point[2] == 70 and \
        point2[0] == 34 and point2[1] == 109 and point2[2] == 70

def doAstroid():
    points = []
    for i in range(0, 23):
        points.append(Point(1270, 180 + i * 30))
        #print(points[i-1].y)
    
    # fucking slow
    counter = 500;
    while(counter < 20 and keyboard.is_pressed('q') == False):
        for point in points:
            pyautogui.moveTo(point.x, point.y)
            pixel = pyautogui.pixel(point.x, point.y)
            if pixel[0] == 55 and pixel[1] == 112 and pixel[2] == 66:
                
                print('Shot!!!')

    time.sleep(5)

def isEngineOpen():
    point = pyautogui.pixel(1060, 860)
    point2 = pyautogui.pixel(1060, 200)
    
    return point[0] == 12 and point[1] == 30 and point[2] == 22 and \
        point2[0] == 12 and point2[1] == 30 and point2[2] == 22

def doEngine():
    points = []
    for i in range(0, 23):
        points.append(Point(1270, 180 + i * 30))
        print(points[i-1].y)

def isNavOpen():
    point = pyautogui.pixel(620, 800)
    point2 = pyautogui.pixel(1200, 800)
    
    return point[0] == 55 and point[1] == 153 and point[2] == 220 and \
        point2[0] == 55 and point2[1] == 153 and point2[2] == 220

def doNav():
    xCoordinates = [555, 750, 950, 1145, 1340]
    for x in xCoordinates:
        print(x)
        for i in range(0, 218):
            point = Point(x, 320 + i*2)
            pixel = pyautogui.pixel(point.x, point.y)
            if x == 555:
                if pixel[0] != 55 and pixel[1] != 153 and pixel[2] != 220:
                    print('found ship', point.x, point.y)
                    pyautogui.moveTo(point.x, point.y + 30)
                    pyautogui.mouseDown(button='left')
                    break
            else:
                if pixel[0] < 55 and pixel[1] < 153 and pixel[2] < 200:
                    print('found new Point', point.x, point.y)
                    pyautogui.moveTo(point.x + 20, point.y + 10, 0.2)
                    break
    pyautogui.mouseUp(button='left')
    time.sleep(2)

def isCalibrationOpen():
    point = pyautogui.pixel(1125, 230)
    point2 = pyautogui.pixel(810, 800)
    
    return point[0] == 255 and point[1] == 227 and point[2] == 0 and \
        point2[0] == 165 and point2[1] == 255 and point2[2] == 255

def doCalibration():
    points = [Point(820, 270), Point(820, 540), Point(820, 815)]
    buttons = [Point(1230, 310), Point(1230, 580), Point(1230, 840)]

    for i, point in enumerate(points):
        pressed = False
        while(not pressed and keyboard.is_pressed('q') == False):
            pixel = pyautogui.pixel(point.x, point.y)
            if (pixel[0] == 71 and pixel[1] == 73 and pixel[2] == 71):
                pyautogui.click(buttons[i].x, buttons[i].y)
                pressed = True
    time.sleep(2)

#############################
#           Tasks           #
#############################


def close():
    pass

# repeatedly check if a game is open
while keyboard.is_pressed('q') == False:
    if isElectricOpen():
        print('Connecting wires super FAAAST!!')
        doElectric()

    if isDivertOpen():
        print('Divert power (Swipe it baby)')
        doDivert()

    if isDivert2Open():
        print('Click divert stage 2... Easy AF')
        doDivert2()
    
    if isAdminCardOpen():
        print('Swipe admin card gently')
        doAdminCard()
        
    if isDownloadOpen():
        print('Download / Upload data. Please no interruptions!')
        doDownload()

    if isStabilization():
        print('Stabilze... (most easiest task ever)')
        doStabilization()

    if isFuelOpen():
        print('Fill fuel')
        doFuel()

    if isSieldsOpen():
        print('Shields UP!!!')
        doShields()
    
    if isGarbageOpen():
        print('Karen, bring the garbage out!')
        doGarbage()

    # if isAsteroidOpen():
    #     doAstroid()

    if isNavOpen():
        print('Slowly but steady')
        doNav()

    if isCalibrationOpen():
        print('Calibrating all the stuff')
        doCalibration()
