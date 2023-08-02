import pyautogui
import time
from random import *
from pynput.mouse import Button, Controller

mouse = Controller()

def slide_to_right():
        x_pos = randint(1620, 1775)
        y_pos = randint(367, 672)

        x_drag_and_drop_range = randint(-279, -200)
        y_drag_and_drop_range = randint(-10, -2)
        plus_ou_moins = randint(1,2)
        if plus_ou_moins == 1:
                y_fin = y_pos - y_drag_and_drop_range
        else:
                y_fin = y_pos + y_drag_and_drop_range
        x_fin = x_pos + x_drag_and_drop_range


        duree = uniform(0.16,0.19)
        pyautogui.moveTo(x_pos, y_pos, duration = duree)
        duree = uniform(0.16,0.19)
        pyautogui.dragTo(x_fin, y_fin, duration = duree)

def slide_to_left():
        x_pos = randint(482, 733)
        y_pos = randint(356, 701)

        x_drag_and_drop_range = randint(-350, -237)
        y_drag_and_drop_range = randint(-9, 20)
        plus_ou_moins = randint(1,2)
        if plus_ou_moins == 1:
                y_fin = y_pos - y_drag_and_drop_range
        else:
                y_fin = y_pos + y_drag_and_drop_range
        x_fin = x_pos - x_drag_and_drop_range


        duree = uniform(0.16,0.19)
        pyautogui.moveTo(x_pos, y_pos, duration = duree)
        duree = uniform(0.16,0.19)
        pyautogui.dragTo(x_fin, y_fin, duration = duree)