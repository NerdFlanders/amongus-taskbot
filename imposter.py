#!/usr/bin/python3

from pyautogui import *
import pyautogui
import keyboard
import time

def close():
    pyautogui.click(x=145, y=140)

def doReactor():
    pyautogui.hotkey('space')
    pyautogui.click(x=175, y=525)
    close()

def doO2():
    pyautogui.hotkey('space')
    pyautogui.click(x=1310, y=480)
    close()

def doLights():
    pyautogui.hotkey('space')
    pyautogui.click(x=780, y=700)
    close()

def doComs():
    pyautogui.hotkey('space')
    pyautogui.click(x=1220, y=970)
    close()

def closeDoor(num):
    #       1 upper engine    2. security      3 lower engine   4. medbay        5. electrical    6. storage       7. caf
    doors = [Point(360, 300), Point(500, 520), Point(360, 810), Point(680, 430), Point(650, 700), Point(980, 810), Point(1030, 260)]
    pyautogui.hotkey('space')
    pyautogui.click(x=doors[num-1].x, y=doors[num-1].y)
    close()

def is_integer(n):
    try:
        int(n)
    except ValueError:
        return 0
    else:
        return int(n)

while keyboard.is_pressed('q') == False:
    input = keyboard.read_key()
    key = is_integer(input)

    if (key >= 1 and key <= 7):
        closeDoor(key)

    if keyboard.is_pressed('capslock'):
        print('Sabotage reactor')
        doReactor()

    if keyboard.is_pressed('left ctrl'):
        print('Sabotage Lights')
        doLights()

    if keyboard.is_pressed('left shift'):
        print('Sabotage O2')
        doO2()    

    if keyboard.is_pressed('left alt'):
        print('Sabotage Coms')
        doComs()

#   r reactor
#   ctrl lights
#   shift O2
#   alt coms
#       1. upper engine    
#       2. security      
#       3. lower engine   
#       4. medbay        
#       5. electrical    
#       6. storage       
#       7. caf