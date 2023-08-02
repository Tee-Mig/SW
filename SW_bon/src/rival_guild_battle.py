import pyautogui
import time
from random import *
from pynput.mouse import Button, Controller
from slides import *

mouse = Controller()

def take_energy_guild():
    if (pyautogui.pixelMatchesColor(1202, 654, (100, 78, 33))):
        while (pyautogui.pixelMatchesColor(1202, 654, (100, 78, 33))):
            x_click = randint(1331,1393)
            y_click = randint(287,340)
            duree = uniform(0.06,0.1)
            pyautogui.click(x_click,y_click,duration=duree)

            print("Je vois attendre enculé")
            time_sleep = uniform(121.0,123.0)
            time.sleep(time_sleep)

            while (pyautogui.locateOnScreen('../img/rival_guild_go.png', region=(1360, 632, 374, 199), confidence=0.95)):
                x_click = randint(1395,1693)
                y_click = randint(677,798)
                mouse.position = (x_click, y_click)
                duree = uniform(0.06,0.1)
                time.sleep(duree)
                mouse.press(Button.left)
                mouse.release(Button.left)

                time_sleep = uniform(0.44,0.48)
                time.sleep(time_sleep)

                if (pyautogui.pixelMatchesColor(1202, 654, (100, 78, 33))
                    or pyautogui.pixelMatchesColor(1197, 649, (202, 161, 71))):
                    break

            # while (pyautogui.locateOnScreen('../img/9x10_combat_repet.png', region=(1366, 635, 367, 201), confidence=0.95) == None
            #     and pyautogui.locateOnScreen('../img/8x10_combat_repet.png', region=(1366, 635, 367, 201), confidence=0.95) == None
            #     and pyautogui.pixelMatchesColor(1202, 654, (100, 78, 33)) == False
            #     and pyautogui.pixelMatchesColor(1197, 649, (202, 161, 71)) == False):
            #     time_sleep = uniform(0.31,0.33)
            #     time.sleep(time_sleep)
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


def auto_rival_guild_battle():

    while (pyautogui.locateOnScreen('../img/rival_in_gvg_guild.png', region=(1458, 848, 189, 182), confidence=0.95) == None):
        time_sleep = uniform(0.22,0.31)
        time.sleep(time_sleep)
    nb_atq = 3 - len(list(pyautogui.locateAllOnScreen('../img/atq_gvg.png', region=(815, 91, 251, 118), confidence=0.95)))

    time_sleep = uniform(1.42,1.46)
    time.sleep(time_sleep)

    while (1):
        while(len(list(pyautogui.locateAllOnScreen('../img/rival_guild_battle_tower.png', region=(262, 201, 1351, 726), confidence=0.95))) > 0
                and nb_atq != 3):
            if (pyautogui.locateOnScreen('../img/rival_guild_battle_tower.png', region=(262, 201, 1351, 726), confidence=0.95)):
                nb_atq = nb_atq + 1
                while (pyautogui.locateOnScreen('../img/rival_guild_battle_tower.png', region=(262, 201, 1351, 726), confidence=0.95)):
                    pos_lead = pyautogui.locateOnScreen('../img/rival_guild_battle_tower.png', region=(262, 201, 1351, 726), confidence=0.95)
                    x_click, y_click = pyautogui.center(pos_lead)
                    x_click_add = randint(-20,20)
                    y_click_add = randint(-20,20)
                    x_click += x_click_add
                    y_click += y_click_add
                    mouse.position = (x_click, y_click)
                    duree = uniform(0.06,0.1)
                    time.sleep(duree)
                    mouse.press(Button.left)
                    mouse.release(Button.left)

                    time_sleep = uniform(0.44,0.48)
                    time.sleep(time_sleep)

                while (pyautogui.locateOnScreen('../img/rival_attaque_guild.png', region=(791, 855, 297, 136), confidence=0.95) == None):
                    time_sleep = uniform(0.22,0.31)
                    time.sleep(time_sleep)

                while (pyautogui.locateOnScreen('../img/rival_attaque_guild.png', region=(791, 855, 297, 136), confidence=0.95)):
                    x_click = randint(818,1058)
                    y_click = randint(891,964)
                    mouse.position = (x_click, y_click)
                    duree = uniform(0.06,0.1)
                    time.sleep(duree)
                    mouse.press(Button.left)
                    mouse.release(Button.left)

                    time_sleep = uniform(0.44,0.48)
                    time.sleep(time_sleep)

                while (pyautogui.locateOnScreen('../img/rival_guild_go.png', region=(1360, 632, 374, 199), confidence=0.95) == None):
                    time_sleep = uniform(0.22,0.31)
                    time.sleep(time_sleep)

                while (pyautogui.locateOnScreen('../img/rival_guild_go.png', region=(1360, 632, 374, 199), confidence=0.95)
                        or pyautogui.pixelMatchesColor(1202, 654, (100, 78, 33))
                        or pyautogui.pixelMatchesColor(1197, 649, (202, 161, 71))
                        or pyautogui.locateOnScreen('../img/deja_attaque_gvg.png', region=(464, 292, 968, 234), confidence=0.9)):
                    x_click = randint(1395,1693)
                    y_click = randint(677,798)
                    mouse.position = (x_click, y_click)
                    duree = uniform(0.06,0.1)
                    time.sleep(duree)
                    mouse.press(Button.left)
                    mouse.release(Button.left)

                    time_sleep = uniform(0.44,0.48)
                    time.sleep(time_sleep)

                    take_energy_guild()

                    if (pyautogui.locateOnScreen('../img/deja_attaque_gvg.png', region=(464, 292, 968, 234), confidence=0.9)):
                        x_click = randint(675,889)
                        y_click = randint(597,675)
                        mouse.position = (x_click, y_click)
                        duree = uniform(0.06,0.1)
                        time.sleep(duree)
                        mouse.press(Button.left)
                        mouse.release(Button.left)

                while (pyautogui.locateOnScreen('../img/rival_guild_victory.png', region=(643, 122, 597, 146), confidence=0.8) == None):
                    if (pyautogui.locateOnScreen('../img/rival_guild_play_button.png', region=(323, 886, 129, 141), confidence=0.95)):
                        x_click = randint(348,422)
                        y_click = randint(924,996)
                        mouse.position = (x_click, y_click)
                        duree = uniform(0.06,0.1)
                        time.sleep(duree)
                        mouse.press(Button.left)
                        mouse.release(Button.left)

                    time_sleep = uniform(0.22,0.31)
                    time.sleep(time_sleep)
                
                while (pyautogui.locateOnScreen('../img/rival_guild_victory.png', region=(643, 122, 597, 146), confidence=0.8)):
                    x_click = randint(531,1538)
                    y_click = randint(309,830)
                    mouse.position = (x_click, y_click)
                    duree = uniform(0.06,0.1)
                    time.sleep(duree)
                    mouse.press(Button.left)
                    mouse.release(Button.left)

                    time_sleep = uniform(0.42,0.45)
                    time.sleep(time_sleep)

            while (pyautogui.locateOnScreen('../img/rival_in_gvg_guild.png', region=(1458, 848, 189, 182), confidence=0.95) == None):
                time_sleep = uniform(0.22,0.31)
                time.sleep(time_sleep)

        if (nb_atq == 3):
            break

        tmp_gvg = pyautogui.screenshot(region=(857, 373, 283, 480))
        slide_to_right()

        time_sleep = uniform(0.75, 0.78)
        time.sleep(time_sleep)

        if (pyautogui.locateOnScreen(tmp_gvg, region=(857, 373, 283, 480), confidence=0.97)):
                break

    while (pyautogui.locateOnScreen('../img/rival_in_gvg_guild.png', region=(1458, 848, 189, 182), confidence=0.95) == None):
        time_sleep = uniform(0.22,0.31)
        time.sleep(time_sleep)

    # attaque les bases jaunes
    if (nb_atq != 3):
        while (1):
            while(len(list(pyautogui.locateAllOnScreen('../img/rival_guild_battle_tower_jaune.png', region=(262, 201, 1351, 726), confidence=0.95))) > 0
                    and nb_atq != 3):
                if (pyautogui.locateOnScreen('../img/rival_guild_battle_tower_jaune.png', region=(262, 201, 1351, 726), confidence=0.95)):
                    nb_atq = nb_atq + 1
                    while (pyautogui.locateOnScreen('../img/rival_guild_battle_tower_jaune.png', region=(262, 201, 1351, 726), confidence=0.95)):
                        pos_lead = pyautogui.locateOnScreen('../img/rival_guild_battle_tower_jaune.png', region=(262, 201, 1351, 726), confidence=0.95)
                        x_click, y_click = pyautogui.center(pos_lead)
                        x_click_add = randint(-20,20)
                        y_click_add = randint(-20,20)
                        x_click += x_click_add
                        y_click += y_click_add
                        mouse.position = (x_click, y_click)
                        duree = uniform(0.06,0.1)
                        time.sleep(duree)
                        mouse.press(Button.left)
                        mouse.release(Button.left)

                        time_sleep = uniform(0.57,0.59)
                        time.sleep(time_sleep)

                    while (pyautogui.locateOnScreen('../img/rival_attaque_guild.png', region=(791, 855, 297, 136), confidence=0.95) == None):
                        time_sleep = uniform(0.22,0.31)
                        time.sleep(time_sleep)

                    while (pyautogui.locateOnScreen('../img/rival_attaque_guild.png', region=(791, 855, 297, 136), confidence=0.95)):
                        x_click = randint(818,1058)
                        y_click = randint(891,964)
                        mouse.position = (x_click, y_click)
                        duree = uniform(0.06,0.1)
                        time.sleep(duree)
                        mouse.press(Button.left)
                        mouse.release(Button.left)

                        time_sleep = uniform(0.57,0.59)
                        time.sleep(time_sleep)

                    while (pyautogui.locateOnScreen('../img/rival_guild_go.png', region=(1360, 632, 374, 199), confidence=0.95) == None):
                        time_sleep = uniform(0.22,0.31)
                        time.sleep(time_sleep)

                    while (pyautogui.locateOnScreen('../img/rival_guild_go.png', region=(1360, 632, 374, 199), confidence=0.95)
                            or pyautogui.pixelMatchesColor(1202, 654, (100, 78, 33))
                            or pyautogui.pixelMatchesColor(1197, 649, (202, 161, 71))):
                        x_click = randint(1395,1693)
                        y_click = randint(677,798)
                        mouse.position = (x_click, y_click)
                        duree = uniform(0.06,0.1)
                        time.sleep(duree)
                        mouse.press(Button.left)
                        mouse.release(Button.left)

                        time_sleep = uniform(0.57,0.59)
                        time.sleep(time_sleep)

                        take_energy_guild()

                    while (pyautogui.locateOnScreen('../img/rival_guild_victory.png', region=(643, 122, 597, 146), confidence=0.8) == None):
                        if (pyautogui.locateOnScreen('../img/rival_guild_play_button.png', region=(323, 886, 129, 141), confidence=0.95)):
                            x_click = randint(348,422)
                            y_click = randint(924,996)
                            mouse.position = (x_click, y_click)
                            duree = uniform(0.06,0.1)
                            time.sleep(duree)
                            mouse.press(Button.left)
                            mouse.release(Button.left)

                        time_sleep = uniform(0.22,0.31)
                        time.sleep(time_sleep)
                    
                    while (pyautogui.locateOnScreen('../img/rival_guild_victory.png', region=(643, 122, 597, 146), confidence=0.8)):
                        x_click = randint(531,1538)
                        y_click = randint(309,830)
                        mouse.position = (x_click, y_click)
                        duree = uniform(0.06,0.1)
                        time.sleep(duree)
                        mouse.press(Button.left)
                        mouse.release(Button.left)

                        time_sleep = uniform(0.42,0.45)
                        time.sleep(time_sleep)

                while (pyautogui.locateOnScreen('../img/rival_in_gvg_guild.png', region=(1458, 848, 189, 182), confidence=0.95) == None):
                    time_sleep = uniform(0.22,0.31)
                    time.sleep(time_sleep)

            if (nb_atq == 3):
                break

            tmp_gvg = pyautogui.screenshot(region=(857, 373, 283, 480))
            slide_to_left()

            time_sleep = uniform(0.75, 0.78)
            time.sleep(time_sleep)

            if (pyautogui.locateOnScreen(tmp_gvg, region=(857, 373, 283, 480), confidence=0.97)):
                    break

    # while (pyautogui.locateOnScreen('../img/ile_de_combat.png', region=(606, 57, 1194, 322), confidence=0.9) == None):

    time_sleep = uniform(0.45, 0.48)
    time.sleep(time_sleep)

    x_click = randint(1674, 1782)
    y_click = randint(901, 986)
    mouse.position = (x_click, y_click)
    duree = uniform(0.06,0.1)
    time.sleep(duree)
    mouse.press(Button.left)
    mouse.release(Button.left)

    # time_sleep = uniform(0.84,0.88)
    # time.sleep(time_sleep)
    
    # while (pyautogui.locateOnScreen('../img/ile_de_combat.png', region=(606, 57, 1194, 322), confidence=0.9) == None):
    #     x_click = randint(1674, 1782)
    #     y_click = randint(901, 986)
    #     mouse.position = (x_click, y_click)
    #     duree = uniform(0.06,0.1)
    #     time.sleep(duree)
    #     mouse.press(Button.left)
    #     mouse.release(Button.left)

    #     time_sleep = uniform(0.44,0.49)
    #     time.sleep(time_sleep)
