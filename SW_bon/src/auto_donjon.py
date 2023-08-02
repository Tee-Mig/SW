import pyautogui
import time
from random import *
from pynput.mouse import Button, Controller
import msvcrt
from utils import launch_dungeon, sell_stuffs, rejouer_dj
import keyboard
import rivaux

mouse = Controller()

def click_windows():
    x_pos_mob = pyautogui.locateOnScreen('../img/bluestacks_icon.png', region=(606, 1018, 860, 61), confidence=0.9)
    x_click, y_click = pyautogui.center(x_pos_mob)
    x_click_add = randint(-15,15)
    y_click_add = randint(-15,15)
    x_click += x_click_add
    y_click += y_click_add
    mouse.position = (x_click, y_click)
    duree = uniform(0.06,0.1)
    time.sleep(duree)
    mouse.press(Button.left)
    mouse.release(Button.left)

        