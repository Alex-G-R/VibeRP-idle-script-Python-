import pyautogui
import time
import random
import keyboard

pyautogui.FAILSAFE = False
delay = 0.2

screen_width, screen_height = pyautogui.size()
center_x = screen_width // 2
center_y = screen_height // 2

while True:
    pyautogui.moveTo(center_x + random.randint(-50, 50), center_y + random.randint(-50, 50), duration=0.25)

    if keyboard.is_pressed('pagedown'):
        break

    pyautogui.keyDown('altleft')
    pyautogui.keyUp('altleft')

    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()

    time.sleep(delay)
