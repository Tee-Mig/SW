import pyautogui
from pynput.mouse import Button, Controller
import time
from random import *
from auto_combat_arene import lance_sorts_en_arene

mouse = Controller()

def check_team_and_run_interserver():
    if (pyautogui.locateOnScreen('../img/arena_team.png', region=(218, 172, 569, 434), confidence=0.95) == None):
        while (pyautogui.locateOnScreen('../img/team_shortcut.png', region=(233, 270, 504, 163), confidence=0.95) == None):
            x_click = randint(110,170)
            y_click = randint(515,567)
            mouse.position = (x_click, y_click)
            duree = uniform(0.06,0.1)
            time.sleep(duree)
            mouse.press(Button.left)
            mouse.release(Button.left)

            time_sleep = uniform(0.42,0.45)
            time.sleep(time_sleep)

        # while (pyautogui.locateOnScreen('../img/team_shortcut.png', region=(233, 270, 504, 163), confidence=0.95) == None):
        #     time_sleep = uniform(0.22,0.31)
        #     time.sleep(time_sleep)

        x_click = randint(260,708)
        y_click = randint(306,398)
        mouse.position = (x_click, y_click)
        duree = uniform(0.06,0.1)
        time.sleep(duree)
        mouse.press(Button.left)
        mouse.release(Button.left)

        time_sleep = uniform(0.34,0.36)
        time.sleep(time_sleep)

        while (pyautogui.locateOnScreen('../img/arena_team.png', region=(218, 172, 569, 434), confidence=0.95) == None):
            if (pyautogui.locateOnScreen('../img/team_shortcut.png', region=(233, 270, 504, 163), confidence=0.95)):
                x_click = randint(260,708)
                y_click = randint(306,398)
                mouse.position = (x_click, y_click)
                duree = uniform(0.06,0.1)
                time.sleep(duree)
                mouse.press(Button.left)
                mouse.release(Button.left)
            time_sleep = uniform(0.27,0.29)
            time.sleep(time_sleep)

    while (pyautogui.locateOnScreen('../img/in_arena_interserver2.png', region=(1307, 589, 470, 275), confidence=0.95) == None):
        time_sleep = uniform(0.03,0.06)
        time.sleep(time_sleep)

    while (pyautogui.locateOnScreen('../img/in_arena_interserver2.png', region=(1307, 589, 470, 275), confidence=0.95)):
        x_click = randint(1392,1693)
        y_click = randint(674,800)
        mouse.position = (x_click, y_click)
        duree = uniform(0.06,0.1)
        time.sleep(duree)
        mouse.press(Button.left)
        mouse.release(Button.left)

        time_sleep = uniform(0.42,0.45)
        time.sleep(time_sleep)

def descend_liste_interserver():
    x_pos = randint(671, 1186)
    y_pos = randint(446, 759)

    x_drag_and_drop_range = randint(44, 65)
    y_drag_and_drop_range = randint(140, 208)
    plus_ou_moins = randint(1,2)
    if plus_ou_moins == 1:
        x_fin = x_pos-x_drag_and_drop_range
    else:
        x_fin = x_pos+x_drag_and_drop_range
    y_fin = y_pos-y_drag_and_drop_range


    duree = uniform(0.16,0.19)
    pyautogui.moveTo(x_pos, y_pos, duration = duree)
    duree = uniform(0.16,0.19)
    pyautogui.dragTo(x_fin, y_fin, duration = duree)

def do_interserver_arena():
    while (pyautogui.locateOnScreen('../img/in_arena_interserver.png', region=(586, 83, 448, 191), confidence=0.9) == None):
            time_sleep = uniform(0.22,0.31)
            time.sleep(time_sleep)
    end = 0
    while (1):
        combat_pos = list(pyautogui.locateAllOnScreen('../img/fight_icon_interserver.png', region=(1284, 202, 240, 742), confidence=0.98))
        for i in combat_pos:
            x_click_add = randint(26, 114)
            y_click_add = randint(32, 80)
            mouse.position = (i[0] + x_click_add, i[1] + y_click_add)
            duree = uniform(0.06,0.1)
            time.sleep(duree)
            mouse.press(Button.left)
            mouse.release(Button.left)

            # A REMETTRE SI BESOIN !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            time_sleep = uniform(0.39,0.41)
            time.sleep(time_sleep)


            while (pyautogui.locateOnScreen('../img/in_arena_interserver2.png', region=(1293, 588, 484, 269), confidence=0.9) == None
                    and pyautogui.locateOnScreen('../img/deja_battu_interserver.png', region=(453, 635, 477, 165), confidence=0.95) == None):
                x_click_add = randint(26, 114)
                y_click_add = randint(32, 80)
                mouse.position = (i[0] + x_click_add, i[1] + y_click_add)
                duree = uniform(0.06,0.1)
                time.sleep(duree)
                mouse.press(Button.left)
                mouse.release(Button.left)

                time_sleep = uniform(0.63,0.65)
                time.sleep(time_sleep)

            if (pyautogui.locateOnScreen('../img/deja_battu_interserver.png', region=(453, 635, 477, 165), confidence=0.95)):
                x_click = randint(1398,1459)
                y_click = randint(246,300)
                mouse.position = (x_click, y_click)
                duree = uniform(0.06,0.1)
                time.sleep(duree)
                mouse.press(Button.left)
                mouse.release(Button.left)
                # time_sleep = uniform(0.45,0.48)
                # time.sleep(time_sleep)
                continue
            
            # time_sleep = uniform(0.82,0.93)
            # time.sleep(time_sleep)

            # changer team
            check_team_and_run_interserver()

            nb_mob = 4 - len(list(pyautogui.locateAllOnScreen('../img/empty_slot_arena.png', region=(1097, 204, 550, 379), confidence=0.98)))
            lance_sorts_en_arene(nb_mob)

            while (pyautogui.locateOnScreen('../img/in_arena_interserver.png', region=(586, 83, 448, 191), confidence=0.9) == None):
                time_sleep = uniform(0.22,0.31)
                time.sleep(time_sleep)
            
            time_sleep = uniform(0.66,0.69)
            time.sleep(time_sleep)

        if (end == 1):
            break

        while (len(list(pyautogui.locateAllOnScreen('../img/fight_icon_interserver.png', region=(1284, 202, 240, 742), confidence=0.98))) < 1):
            tmp_interserver = pyautogui.screenshot(region=(390, 273, 1100, 612))
            descend_liste_interserver()

            time_sleep = uniform(0.75, 0.78)
            time.sleep(time_sleep)

            if (pyautogui.locateOnScreen(tmp_interserver, region=(390, 273, 1100, 612), confidence=0.97)):
                end = 1
                break
