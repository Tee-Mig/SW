import pyautogui
import time
from random import *
from pynput.mouse import Button, Controller
from enum import Enum
from pynput.mouse import Button, Controller

mouse = Controller()

class Toa_team(Enum):
        TEAM1 = 1
        TEAM2 = 2
        TEAM3 = 3
        TEAM4 = 5

default_toa_team = Toa_team.TEAM1.value

def take_energy():
    img = pyautogui.screenshot()
    if (pyautogui.pixelMatchesColor(1197, 649, (202, 161, 71))):
        if (pyautogui.pixelMatchesColor(1202, 654, (100, 78, 33))):
            exit(0)
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

            while (pyautogui.locateOnScreen('../img/go_toa.png', region=(1317, 614, 456, 249), confidence=0.9) == None
                    and pyautogui.locateOnScreen('../img/annuler_toa.png', region=(1328, 797, 443, 217), confidence=0.9) == None):
                time_sleep = uniform(0.04,0.08)
                time.sleep(time_sleep)

            if (pyautogui.locateOnScreen('../img/annuler_toa.png', region=(1328, 797, 443, 217), confidence=0.9) == None):
                x_click = randint(1403,1676)
                y_click = randint(872,955)
                duree = uniform(0.06,0.1)
                pyautogui.click(x_click,y_click,duration=duree)
            else:
                x_click = randint(1409,1672)
                y_click = randint(691,784)
                duree = uniform(0.06,0.1)
                pyautogui.click(x_click,y_click,duration=duree)

def toa_check_team_and_run(team_status):
    if (team_status == 1):
        if (pyautogui.locateOnScreen('../img/toa_team1.jpg', region=(143, 167, 747, 469), confidence=0.95) == None):
            x_click = randint(110,170)
            y_click = randint(515,567)
            mouse.position = (x_click, y_click)
            duree = uniform(0.06,0.1)
            time.sleep(duree)
            mouse.press(Button.left)
            mouse.release(Button.left)

            while (pyautogui.locateOnScreen('../img/toa_shortcut1.jpg', region=(230, 273, 642, 611), confidence=0.95) == None):
                time_sleep = uniform(0.22,0.31)
                time.sleep(time_sleep)

            x_click = randint(261,820)
            y_click = randint(310,395)
            mouse.position = (x_click, y_click)
            duree = uniform(0.06,0.1)
            time.sleep(duree)
            mouse.press(Button.left)
            mouse.release(Button.left)

            while (pyautogui.locateOnScreen('../img/toa_team1.jpg', region=(143, 167, 747, 469), confidence=0.95) == None):
                time_sleep = uniform(0.22,0.31)
                time.sleep(time_sleep)
    if (team_status == 2):
        if (pyautogui.locateOnScreen('../img/toa_team2.jpg', region=(143, 167, 747, 469), confidence=0.95) == None):
            x_click = randint(110,170)
            y_click = randint(515,567)
            mouse.position = (x_click, y_click)
            duree = uniform(0.06,0.1)
            time.sleep(duree)
            mouse.press(Button.left)
            mouse.release(Button.left)

            while (pyautogui.locateOnScreen('../img/toa_shortcut2.jpg', region=(230, 273, 642, 611), confidence=0.95) == None):
                time_sleep = uniform(0.22,0.31)
                time.sleep(time_sleep)

            x_click = randint(261,820)
            y_click = randint(453,540)
            mouse.position = (x_click, y_click)
            duree = uniform(0.06,0.1)
            time.sleep(duree)
            mouse.press(Button.left)
            mouse.release(Button.left)

            while (pyautogui.locateOnScreen('../img/toa_team2.jpg', region=(143, 167, 747, 469), confidence=0.95) == None):
                time_sleep = uniform(0.22,0.31)
                time.sleep(time_sleep)

    if (team_status == 3 or team_status == 4):
        if (pyautogui.locateOnScreen('../img/toa_team3.jpg', region=(143, 167, 747, 469), confidence=0.95) == None):
            x_click = randint(110,170)
            y_click = randint(515,567)
            mouse.position = (x_click, y_click)
            duree = uniform(0.06,0.1)
            time.sleep(duree)
            mouse.press(Button.left)
            mouse.release(Button.left)

            while (pyautogui.locateOnScreen('../img/toa_shortcut3.jpg', region=(230, 273, 642, 611), confidence=0.95) == None):
                time_sleep = uniform(0.22,0.31)
                time.sleep(time_sleep)

            x_click = randint(261,820)
            y_click = randint(599,688)
            mouse.position = (x_click, y_click)
            duree = uniform(0.06,0.1)
            time.sleep(duree)
            mouse.press(Button.left)
            mouse.release(Button.left)

            while (pyautogui.locateOnScreen('../img/toa_team3.jpg', region=(143, 167, 747, 469), confidence=0.95) == None):
                time_sleep = uniform(0.22,0.31)
                time.sleep(time_sleep)

    if (team_status >= 5):
        if (pyautogui.locateOnScreen('../img/toa_team4.jpg', region=(143, 167, 747, 469), confidence=0.95) == None):
            x_click = randint(110,170)
            y_click = randint(515,567)
            mouse.position = (x_click, y_click)
            duree = uniform(0.06,0.1)
            time.sleep(duree)
            mouse.press(Button.left)
            mouse.release(Button.left)

            while (pyautogui.locateOnScreen('../img/toa_shortcut4.jpg', region=(230, 273, 642, 611), confidence=0.95) == None):
                time_sleep = uniform(0.22,0.31)
                time.sleep(time_sleep)

            x_click = randint(261,820)
            y_click = randint(746,834)
            mouse.position = (x_click, y_click)
            duree = uniform(0.06,0.1)
            time.sleep(duree)
            mouse.press(Button.left)
            mouse.release(Button.left)

            while (pyautogui.locateOnScreen('../img/toa_team4.jpg', region=(143, 167, 747, 469), confidence=0.95) == None):
                time_sleep = uniform(0.22,0.31)
                time.sleep(time_sleep)


def toa_auto(default_team):
    while (1):
        take_energy()
        if (pyautogui.locateOnScreen('../img/defeated_toa_palier.jpg', region=(548, 112, 781, 195), confidence=0.6)):
            default_team = default_team + 1
            if (default_team == 8):
                exit(1)
            while (pyautogui.locateOnScreen('../img/preparation_toa.jpg', region=(245, 425, 686, 297), confidence=0.8) == None
                and pyautogui.locateOnScreen('../img/recompenses_obtenues_toa.png', region=(667, 167, 534, 155), confidence=0.9) == None):
                x_click = randint(456,1365)
                y_click = randint(256,338)
                duree = uniform(0.06,0.1)
                pyautogui.click(x_click,y_click,duration=duree)

                time_sleep = uniform(0.44,0.48)
                time.sleep(time_sleep)

            if (pyautogui.locateOnScreen('../img/recompenses_obtenues_toa.png', region=(667, 167, 534, 155), confidence=0.9)):
                while (pyautogui.locateOnScreen('../img/recompenses_obtenues_toa.png', region=(667, 167, 534, 155), confidence=0.9)):
                    x_click = randint(815,1058)
                    y_click = randint(802,871)
                    duree = uniform(0.06,0.1)
                    pyautogui.click(x_click,y_click,duration=duree)

                    time_sleep = uniform(0.44,0.48)
                    time.sleep(time_sleep)

            while (pyautogui.locateOnScreen('../img/preparation_toa.jpg', region=(245, 425, 686, 297), confidence=0.8)):
                x_pos_mob = pyautogui.locateOnScreen('../img/preparation_toa.jpg', region=(245, 425, 686, 297), confidence=0.8)
                x_click, y_click = pyautogui.center(x_pos_mob)
                x_click_add = randint(-130,300)
                y_click_add = randint(-30,30)
                x_click += x_click_add
                y_click += y_click_add
                duree = uniform(0.06,0.1)
                pyautogui.click(x_click,y_click,duration=duree)

                time_sleep = uniform(0.44,0.48)
                time.sleep(time_sleep)


            while (pyautogui.locateOnScreen('../img/go_toa.png', region=(1317, 614, 456, 249), confidence=0.9) == None
                    and pyautogui.locateOnScreen('../img/annuler_toa.png', region=(1328, 797, 443, 217), confidence=0.9) == None):
                time_sleep = uniform(0.04,0.08)
                time.sleep(time_sleep)

            toa_check_team_and_run(default_team)

            while (pyautogui.locateOnScreen('../img/go_toa.png', region=(1317, 614, 456, 249), confidence=0.9) == None
                    and pyautogui.locateOnScreen('../img/annuler_toa.png', region=(1328, 797, 443, 217), confidence=0.9) == None):
                x_click = randint(362,876)
                y_click = randint(524,628)
                duree = uniform(0.06,0.1)
                pyautogui.click(x_click,y_click,duration=duree)

                time_sleep = uniform(0.44,0.48)
                time.sleep(time_sleep)

            if (pyautogui.locateOnScreen('../img/annuler_toa.png', region=(1328, 797, 443, 217), confidence=0.9) == None):
                x_click = randint(1403,1676)
                y_click = randint(872,955)
                duree = uniform(0.06,0.1)
                pyautogui.click(x_click,y_click,duration=duree)
            else:
                x_click = randint(1409,1672)
                y_click = randint(691,784)
                duree = uniform(0.06,0.1)
                pyautogui.click(x_click,y_click,duration=duree)
            
            
            
        if (pyautogui.locateOnScreen('../img/play_button_toa.png', region=(296, 867, 162, 160), confidence=0.7)):
            x_click = randint(349,420)
            y_click = randint(929,996)
            duree = uniform(0.06,0.1)
            pyautogui.click(x_click,y_click,duration=duree)

        if (pyautogui.locateOnScreen('../img/victory_toa_palier.png', region=(630, 117, 615, 165), confidence=0.6)):
            time_sleep = uniform(4.18,4.26)
            time.sleep(time_sleep)

            if (pyautogui.locateOnScreen('../img/victory_toa_palier.png', region=(630, 117, 615, 165), confidence=0.6)):

                while (pyautogui.locateOnScreen('../img/recompenses_obtenues_toa.png', region=(667, 167, 534, 155), confidence=0.9) == None
                    and pyautogui.locateOnScreen('../img/ok_toa.png', region=(569, 585, 742, 313), confidence=0.8) == None):
                        x_click = randint(191,1345)
                        y_click = randint(181,353)
                        duree = uniform(0.06,0.1)
                        pyautogui.click(x_click,y_click,duration=duree)

                        time_sleep = uniform(0.44,0.48)
                        time.sleep(time_sleep)

                if (pyautogui.locateOnScreen('../img/recompenses_obtenues_toa.png', region=(667, 167, 534, 155), confidence=0.9)):
                    while (pyautogui.locateOnScreen('../img/recompenses_obtenues_toa.png', region=(667, 167, 534, 155), confidence=0.9)):
                        x_click = randint(815,1058)
                        y_click = randint(802,871)
                        duree = uniform(0.06,0.1)
                        pyautogui.click(x_click,y_click,duration=duree)

                        time_sleep = uniform(0.44,0.48)
                        time.sleep(time_sleep)
                else:
                    while (pyautogui.locateOnScreen('../img/ok_toa.png', region=(569, 585, 742, 313), confidence=0.8)):
                        x_pos_mob = pyautogui.locateOnScreen('../img/ok_toa.png', region=(569, 585, 742, 313), confidence=0.8)
                        x_click, y_click = pyautogui.center(x_pos_mob)
                        x_click_add = randint(-100,100)
                        y_click_add = randint(-35,35)
                        x_click += x_click_add
                        y_click += y_click_add
                        duree = uniform(0.06,0.1)
                        pyautogui.click(x_click,y_click,duration=duree)

                        time_sleep = uniform(0.44,0.48)
                        time.sleep(time_sleep)

                while (pyautogui.locateOnScreen('../img/go_toa.png', region=(1317, 614, 456, 249), confidence=0.9) == None
                        and pyautogui.locateOnScreen('../img/annuler_toa.png', region=(1328, 797, 443, 217), confidence=0.9) == None):
                    x_click = randint(362,876)
                    y_click = randint(524,628)
                    duree = uniform(0.06,0.1)
                    pyautogui.click(x_click,y_click,duration=duree)

                    time_sleep = uniform(0.44,0.48)
                    time.sleep(time_sleep)

                if (pyautogui.locateOnScreen('../img/annuler_toa.png', region=(1328, 797, 443, 217), confidence=0.9) == None):
                    x_click = randint(1403,1676)
                    y_click = randint(872,955)
                    duree = uniform(0.06,0.1)
                    pyautogui.click(x_click,y_click,duration=duree)
                else:
                    x_click = randint(1409,1672)
                    y_click = randint(691,784)
                    duree = uniform(0.06,0.1)
                    pyautogui.click(x_click,y_click,duration=duree)

        