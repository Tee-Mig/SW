import pyautogui
from random import *
from pynput.mouse import Button, Controller
import time

mouse = Controller()

def do_world_boss():
    while (pyautogui.locateOnScreen('../img/world_boss_icon.png', region=(866, 396, 772, 366), confidence=0.9) == None):
        time_sleep = uniform(0.22,0.31)
        time.sleep(time_sleep)

    pos_lead = pyautogui.locateOnScreen('../img/world_boss_icon.png', region=(866, 396, 772, 366), confidence=0.9)
    x_click, y_click = pyautogui.center(pos_lead)
    x_click_add = randint(-30,30)
    y_click_add = randint(-30,30)
    x_click += x_click_add
    y_click += y_click_add
    mouse.position = (x_click, y_click)
    duree = uniform(0.06,0.1)
    time.sleep(duree)
    mouse.press(Button.left)
    mouse.release(Button.left)

    compute = 0
    while (pyautogui.locateOnScreen('../img/world_boss_welcome.png', region=(756, 200, 509, 528), confidence=0.9) == None):
        if (pyautogui.locateOnScreen('../img/world_boss_computing.png', region=(461, 290, 972, 192), confidence=0.9)):
            compute = 1
            x_click = randint(830,1047)
            y_click = randint(599,675)
            mouse.position = (x_click, y_click)
            duree = uniform(0.06,0.1)
            time.sleep(duree)
            mouse.press(Button.left)
            mouse.release(Button.left)
            break
        time_sleep = uniform(0.22,0.31)
        time.sleep(time_sleep)

    if (pyautogui.pixelMatchesColor(1499, 715, (213, 174, 81))):
        for i in range(3):
            # while (pyautogui.locateOnScreen('../img/launch_world_boss.png', region=(1219, 632, 390, 226), confidence=0.9) == None):
            #     time_sleep = uniform(0.22,0.31)
            #     time.sleep(time_sleep)
            # A CHANGER SI PROBLEME !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            if (pyautogui.pixelMatchesColor(1499, 715, (213, 174, 81)) == False):
                break
            while (pyautogui.locateOnScreen('../img/launch_world_boss.png', region=(1219, 632, 390, 226), confidence=0.9)):
                x_click = randint(1276,1536)
                y_click = randint(704,797)
                mouse.position = (x_click, y_click)
                duree = uniform(0.06,0.1)
                time.sleep(duree)
                mouse.press(Button.left)
                mouse.release(Button.left)

                time_sleep = uniform(0.49,0.51)
                time.sleep(time_sleep)
            
            while (pyautogui.locateOnScreen('../img/launch_world_boss_10_go.png', region=(1416, 602, 408, 233), confidence=0.95) == None
                   and pyautogui.pixelMatchesColor(1202, 654, (100, 78, 33)) == False
                   and pyautogui.pixelMatchesColor(1197, 649, (202, 161, 71)) == False):
                time_sleep = uniform(0.31,0.33)
                time.sleep(time_sleep)

            if (pyautogui.pixelMatchesColor(1202, 654, (100, 78, 33))):
                while (pyautogui.pixelMatchesColor(1202, 654, (100, 78, 33))):
                    x_click = randint(1331,1393)
                    y_click = randint(287,340)
                    duree = uniform(0.06,0.1)
                    pyautogui.click(x_click,y_click,duration=duree)

                    time_sleep = uniform(121.0,123.0)
                    time.sleep(time_sleep)

                    while (pyautogui.locateOnScreen('../img/launch_world_boss.png', region=(1219, 632, 390, 226), confidence=0.9)):
                        x_click = randint(1276,1536)
                        y_click = randint(704,797)
                        mouse.position = (x_click, y_click)
                        duree = uniform(0.06,0.1)
                        time.sleep(duree)
                        mouse.press(Button.left)
                        mouse.release(Button.left)

                        time_sleep = uniform(0.49,0.51)
                        time.sleep(time_sleep)

                    while (pyautogui.locateOnScreen('../img/launch_world_boss_10_go.png', region=(1416, 602, 408, 233), confidence=0.9) == None
                   and pyautogui.pixelMatchesColor(1202, 654, (100, 78, 33)) == False
                   and pyautogui.pixelMatchesColor(1197, 649, (202, 161, 71)) == False):
                        time_sleep = uniform(0.31,0.33)
                        time.sleep(time_sleep)

            if (pyautogui.pixelMatchesColor(1197, 649, (202, 161, 71))):
                x_click = randint(975,1232)
                y_click = randint(608,695)
                duree = uniform(0.06,0.1)
                pyautogui.click(x_click,y_click,duration=duree)

                # time_sleep = uniform(0.28,0.31)
                # time.sleep(time_sleep)

                while(pyautogui.locateOnScreen('../img/in_coffre.png', region=(692, 146, 480, 134), confidence=0.9) == None):
                    time_sleep = uniform(0.06,0.09)
                    time.sleep(time_sleep)

                for i in range(4):
                    while (pyautogui.locateOnScreen('../img/recevoir_energie.png', region=(1050, 320, 246, 139), confidence=0.9) == None
                            and pyautogui.pixelMatchesColor(1172, 396, (63, 43, 26)) == False):
                        time_sleep = uniform(0.06,0.09)
                        time.sleep(time_sleep)
                        
                    if (pyautogui.locateOnScreen('../img/recevoir_energie.png', region=(1050, 320, 246, 139), confidence=0.9)):
                        x_click = randint(1092,1257)
                        y_click = randint(359,425)
                        duree = uniform(0.06,0.1)
                        pyautogui.click(x_click,y_click,duration=duree)

                        time_sleep = uniform(0.23,0.26)
                        time.sleep(time_sleep)

                while(pyautogui.locateOnScreen('../img/in_coffre.png', region=(692, 146, 480, 134), confidence=0.9)):
                    x_click = randint(1293,1356)
                    y_click = randint(202,258)
                    duree = uniform(0.06,0.1)
                    pyautogui.click(x_click,y_click,duration=duree)

                    time_sleep = uniform(0.46,0.49)
                    time.sleep(time_sleep)
                
                while (pyautogui.locateOnScreen('../img/launch_world_boss.png', region=(1219, 632, 390, 226), confidence=0.9)):
                    x_click = randint(1276,1536)
                    y_click = randint(704,797)
                    mouse.position = (x_click, y_click)
                    duree = uniform(0.06,0.1)
                    time.sleep(duree)
                    mouse.press(Button.left)
                    mouse.release(Button.left)

                    time_sleep = uniform(0.49,0.51)
                    time.sleep(time_sleep)

            while (pyautogui.locateOnScreen('../img/launch_world_boss_10_go.png', region=(1416, 602, 408, 233), confidence=0.9) == None):
                time_sleep = uniform(0.31,0.33)
                time.sleep(time_sleep)

            time_sleep = uniform(0.41,0.44)
            time.sleep(time_sleep)

            # click sur automatique
            x_click = randint(1434,1680)
            y_click = randint(178,224)
            mouse.position = (x_click, y_click)
            duree = uniform(0.06,0.1)
            time.sleep(duree)
            mouse.press(Button.left)
            mouse.release(Button.left)

            time_sleep = uniform(0.39,0.42)
            time.sleep(time_sleep)

            x_click = randint(1470,1770)
            y_click = randint(666,795)
            mouse.position = (x_click, y_click)
            duree = uniform(0.06,0.1)
            time.sleep(duree)
            mouse.press(Button.left)
            mouse.release(Button.left)

            time_sleep = uniform(0.41,0.44)
            time.sleep(time_sleep)

            while (pyautogui.locateOnScreen('../img/au_moins_10_monstres.jpg', region=(438, 303, 1005, 246), confidence=0.9)):
                x_click = randint(828,1049)
                y_click = randint(596,678)
                mouse.position = (x_click, y_click)
                duree = uniform(0.06,0.1)
                time.sleep(duree)
                mouse.press(Button.left)
                mouse.release(Button.left)

                time_sleep = uniform(0.39,0.42)
                time.sleep(time_sleep)

                # click sur automatique
                x_click = randint(1434,1680)
                y_click = randint(178,224)
                mouse.position = (x_click, y_click)
                duree = uniform(0.06,0.1)
                time.sleep(duree)
                mouse.press(Button.left)
                mouse.release(Button.left)

                time_sleep = uniform(0.39,0.42)
                time.sleep(time_sleep)

                x_click = randint(1470,1770)
                y_click = randint(666,795)
                mouse.position = (x_click, y_click)
                duree = uniform(0.06,0.1)
                time.sleep(duree)
                mouse.press(Button.left)
                mouse.release(Button.left)

                time_sleep = uniform(0.41,0.44)
                time.sleep(time_sleep)

            while (pyautogui.locateOnScreen('../img/world_boss_result.png', region=(726, 115, 452, 173), confidence=0.9) == None):
                if (pyautogui.locateOnScreen('../img/skip_world_boss.png', region=(1614, 940, 170, 96), confidence=0.7)):
                    x_click = randint(1667,1731)
                    y_click = randint(988,1010)
                    mouse.position = (x_click, y_click)
                    duree = uniform(0.06,0.1)
                    time.sleep(duree)
                    mouse.press(Button.left)
                    mouse.release(Button.left)

                if (pyautogui.locateOnScreen('../img/no_energy_world_boss.png', region=(561, 266, 769, 300), confidence=0.9)):
                    x_click = randint(829,1046)
                    y_click = randint(597,674)
                    mouse.position = (x_click, y_click)
                    duree = uniform(0.06,0.1)
                    time.sleep(duree)
                    mouse.press(Button.left)
                    mouse.release(Button.left)
                    do_world_boss()

                time_sleep = uniform(0.22,0.31)
                time.sleep(time_sleep)

            while (pyautogui.locateOnScreen('../img/world_boss_result.png', region=(726, 115, 452, 173), confidence=0.9)):
                x_click = randint(151,635)
                y_click = randint(415,914)
                mouse.position = (x_click, y_click)
                duree = uniform(0.06,0.1)
                time.sleep(duree)
                mouse.press(Button.left)
                mouse.release(Button.left)

                time_sleep = uniform(0.33,0.36)
                time.sleep(time_sleep)

            # att ok pour les recompenses
            while (pyautogui.locateOnScreen('../img/launch_world_boss_ok_reward.png', region=(779, 858, 326, 162), confidence=0.9) == None):
                time_sleep = uniform(0.22,0.31)
                time.sleep(time_sleep)

            while (pyautogui.locateOnScreen('../img/world_boss_result.png', region=(726, 115, 452, 173), confidence=0.9) == None):
                x_click = randint(816,1056)
                y_click = randint(908,981)
                mouse.position = (x_click, y_click)
                duree = uniform(0.06,0.1)
                time.sleep(duree)
                mouse.press(Button.left)
                mouse.release(Button.left)

                time_sleep = uniform(0.43,0.46)
                time.sleep(time_sleep)

            # while (pyautogui.locateOnScreen('../img/world_boss_result.png', region=(726, 115, 452, 173), confidence=0.9) == None):
            #     time_sleep = uniform(0.22,0.31)
            #     time.sleep(time_sleep)

            while (pyautogui.locateOnScreen('../img/world_boss_result.png', region=(726, 115, 452, 173), confidence=0.9)):
                x_click = randint(516,1216)
                y_click = randint(335,813)
                mouse.position = (x_click, y_click)
                duree = uniform(0.06,0.1)
                time.sleep(duree)
                mouse.press(Button.left)
                mouse.release(Button.left)

                time_sleep = uniform(0.33,0.36)
                time.sleep(time_sleep)

            while (pyautogui.locateOnScreen('../img/world_boss_welcome.png', region=(756, 200, 509, 528), confidence=0.9) == None):
                time_sleep = uniform(0.22,0.31)
                time.sleep(time_sleep)
            
    if (compute == 0):
        while (pyautogui.locateOnScreen('../img/world_boss_icon.png', region=(866, 396, 772, 366), confidence=0.9) == None):
            x_click = randint(1574,1635)
            y_click = randint(92,148)
            mouse.position = (x_click, y_click)
            duree = uniform(0.06,0.1)
            time.sleep(duree)
            mouse.press(Button.left)
            mouse.release(Button.left)

            time_sleep = uniform(0.45,0.48)
            time.sleep(time_sleep)