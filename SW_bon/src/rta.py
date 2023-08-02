import pyautogui
import time
from random import *
from pynput.mouse import Button, Controller
from auto_combat_arene import ou_est_la_cible_emplacement_deux_ou_quatre
from auto_combat_arene import ou_est_la_cible_emplacement_deux_ou_quatre_allies_team
import numbers
import msvcrt
import combat_arene
import default_dungeon_variables
from auto_combat_arene import lance_sorts_en_arene
from rivaux import descend_liste
from default_dungeon_variables import default_donjon
import rivaux
from utils import descend_liste_dj, launch_dungeon
import keyboard
from utils import sell_stuffs, rejouer_dj, descend_liste_dj2
from dimension import *
from enums import Dungeon_type, default_donjon, Dimension_type
import pytesseract as pyt
import cv2
import numpy as np
import re

mouse = Controller()

def do_arena_dimension(data):
    do_arena = data["arena_status"]
    if (do_arena == 1 or data["rta_status"] == 1):
        while (pyautogui.locateOnScreen('../img/close_window_combat_repet.png', region=(1598, 95, 164, 134), confidence=0.95) == None
            and pyautogui.locateOnScreen('../img/combat_arena2.png', region=(1351, 330, 437, 213), confidence=0.9) == None):
            time_sleep = uniform(0.22,0.31)
            time.sleep(time_sleep)

        # time_sleep = uniform(0.22,0.31)
        # time.sleep(time_sleep)

        if (pyautogui.locateOnScreen('../img/close_window_combat_repet.png', region=(1598, 95, 164, 134), confidence=0.95)):
            while (pyautogui.locateOnScreen('../img/close_window_combat_repet.png', region=(1598, 95, 164, 134), confidence=0.95)):
                x_click = randint(1669,1717)
                y_click = randint(154,198)
                mouse.position = (x_click, y_click)
                duree = uniform(0.06,0.1)
                time.sleep(duree)
                mouse.press(Button.left)
                mouse.release(Button.left)

                time_sleep = uniform(0.44,0.48)
                time.sleep(time_sleep)

        while (pyautogui.locateOnScreen('../img/combat_arena2.png', region=(1351, 330, 437, 213), confidence=0.9) == None):
            if (pyautogui.locateOnScreen('../img/resultats_arena.png', region=(760, 150, 1079, 211), confidence=0.9)):
                    x_click = randint(1369, 1782)
                    y_click = randint(80, 152)
                    mouse.position = (x_click, y_click)
                    duree = uniform(0.06,0.1)
                    time.sleep(duree)
                    mouse.press(Button.left)
                    mouse.release(Button.left)

                    time_sleep = uniform(0.18,0.21)
                    time.sleep(time_sleep)

            if (pyautogui.locateOnScreen('../img/calculs_arene.png', region=(1351, 330, 437, 213), confidence=0.9)):
                    do_arena = 0
                    break

            time_sleep = uniform(0.04,0.08)
            time.sleep(time_sleep)

        if (pyautogui.locateOnScreen('../img/no_wing_arena.jpg', region=(65, 928, 236, 94), confidence=0.95)):
            do_arena = 0

    if (do_arena == 1):
        auto_arena(data) # good
    else:
        if (data["rta_status"] == 1):
            while (pyautogui.locateOnScreen('../img/combat_amical.png', region=(1332, 540, 476, 245), confidence=0.9) == None):
                x_click = randint(488,801)
                y_click = randint(85,150)
                mouse.position = (x_click, y_click)
                duree = uniform(0.06,0.1)
                time.sleep(duree)
                mouse.press(Button.left)
                mouse.release(Button.left)

                time_sleep = uniform(0.45,0.48)
                time.sleep(time_sleep)

            rta_boucle(data)

        continue_routine(data)

def print_msg_dimension(data):
    print("\nDimension dungeon ongoing...")
    print(f'Press \'s\' to stop dimension, \'c\' to change arena status({data["arena_status"]}) or \'a\' to do arena')
    

def auto_dj_dimension(data):
    print_msg_dimension(data)
    while (1):
        end_run = 0
        while (pyautogui.locateOnScreen('../img/rejouer_button.png', region=(846, 828, 302, 125)) == None):
            if (pyautogui.locateOnScreen('../img/waiting_for_repet_battle2.png', region=(62, 97, 127, 356), confidence=0.8)):
                x_click = randint(103,140)
                y_click = randint(312,342)
                duree = uniform(0.06,0.1)
                pyautogui.click(x_click,y_click,duration=duree)

            if (keyboard.is_pressed('c')):
                tmp_arena_status = 9999
                while (tmp_arena_status != 0 and tmp_arena_status != 1):
                        try:
                                tmp_arena_status = int(input("enter arena status (0 or 1): "))
                        except ValueError:
                                pass
                data["arena_status"] = tmp_arena_status
                print_msg_dimension(data)

            if (keyboard.is_pressed('a')):
                if (pyautogui.locateOnScreen('../img/rejouer_button.png', region=(846, 828, 302, 125))):
                    continue
                click_windows()
                if (data["arena_status"] == 1):
                    do_arena_dimension(data)

            if (pyautogui.locateOnScreen('../img/9_wings.png', region=(72, 931, 219, 90), confidence=0.95)
                or pyautogui.locateOnScreen('../img/10_wings.png', region=(72, 931, 219, 90), confidence=0.95)):
                # click sur le bouton pour fermer la fenetre combat a repet
                if (pyautogui.locateOnScreen('../img/rejouer_button.png', region=(846, 828, 302, 125))):
                    continue
                if (data["arena_status"] == 1):
                    do_arena_dimension(data)

            if (keyboard.is_pressed('s')):
                end_run = 1
                # tmp_launch_dungeon_status = 9999
                # while (tmp_launch_dungeon_status < 0 or tmp_launch_dungeon_status > 11):
                #         try:
                #                 tmp_launch_dungeon_status = int(input("enter the dungeon to launch:\n0: None| 1: giant | 2: dragon | 3: necro | 4: fortress | 5: crypt |\n6: r5 | 7: fire rift  | 8: water rift  | 9: wind rift  | 10: light rift  | 11: dark rift : "))
                #         except ValueError:
                #                 pass
                # if (launch_dungeon_status == tmp_launch_dungeon_status):
                #     print("\nDungeon already ongoing")
                #     print("Dungeon ongoing...")
                #     print("Press 'd' to change dungeon")
                #     continue
                # launch_dungeon_status = tmp_launch_dungeon_status
                click_windows()
                while (pyautogui.locateOnScreen('../img/waiting_for_repet_battle2.png', region=(62, 97, 127, 356), confidence=0.8) == None
                        and pyautogui.locateOnScreen('../img/selection_donjon.png', region=(124, 806, 339, 168)) == None
                        and pyautogui.locateOnScreen('../img/fin_des_combats.png', region=(716, 802, 467, 176)) == None):
                    time_sleep = uniform(0.22,0.29)
                    time.sleep(time_sleep)

                if (pyautogui.locateOnScreen('../img/waiting_for_repet_battle2.png', region=(62, 97, 127, 356), confidence=0.8)):
                    x_click = randint(103,140)
                    y_click = randint(312,342)
                    duree = uniform(0.06,0.1)
                    pyautogui.click(x_click,y_click,duration=duree)
                    # x_pos_mob = pyautogui.locateOnScreen('../img/waiting_for_repet_battle2.png', region=(62, 97, 127, 356), confidence=0.8)
                    # x_click, y_click = pyautogui.center(x_pos_mob)
                    # x_click_add = randint(-15,15)
                    # y_click_add = randint(-15,15)
                    # x_click += x_click_add
                    # y_click += y_click_add
                    # duree = uniform(0.06,0.1)
                    # pyautogui.click(x_click,y_click,duration=duree)

                    while (pyautogui.locateOnScreen('../img/vente_selective.png', region=(1406, 831, 356, 135)) == None):
                        time_sleep = uniform(0.22,0.29)
                        time.sleep(time_sleep)

                # stop la run
                if (pyautogui.locateOnScreen('../img/fin_des_combats.png', region=(716, 802, 467, 176))):
                    while (pyautogui.locateOnScreen('../img/fin_des_combats.png', region=(716, 802, 467, 176))):
                        x_click = randint(769,1125)
                        y_click = randint(860,928)
                        duree = uniform(0.06,0.1)
                        pyautogui.click(x_click,y_click,duration=duree)

                        time_sleep = uniform(0.44,0.48)
                        time.sleep(time_sleep)

                    time_sleep = uniform(0.27,0.31)
                    time.sleep(time_sleep)

                    while (pyautogui.locateOnScreen('../img/finir_dj.png', region=(357, 230, 1138, 589)) == None):
                        time_sleep = uniform(0.22,0.29)
                        time.sleep(time_sleep)

                    x_click = randint(675,892)
                    y_click = randint(596,676)
                    duree = uniform(0.06,0.1)
                    pyautogui.click(x_click,y_click,duration=duree)

                    # while (pyautogui.locateOnScreen('../img/rejouer_button.png', region=(846, 828, 302, 125)) == None):
                    #     time_sleep = uniform(0.22,0.29)
                    #     time.sleep(time_sleep)

                    while (pyautogui.locateOnScreen('../img/selection_donjon.png', region=(124, 806, 339, 168)) == None):
                        time_sleep = uniform(0.22,0.29)
                        time.sleep(time_sleep)


                # lance le nouveau donjon
                # if (pyautogui.locateOnScreen('../img/selection_donjon.png', region=(124, 806, 339, 168))):
                #     sell_stuffs(status_dungeon)

                #     while (pyautogui.locateOnScreen('../img/selection_donjon.png', region=(124, 806, 339, 168)) == None):
                #         time_sleep = uniform(0.22,0.29)
                #         time.sleep(time_sleep)

                #     while (pyautogui.locateOnScreen('../img/selection_donjon.png', region=(124, 806, 339, 168))):
                #         x_click = randint(165,420)
                #         y_click = randint(861,926)
                #         duree = uniform(0.06,0.1)
                #         pyautogui.click(x_click,y_click,duration=duree)

                #         time_sleep = uniform(0.44,0.48)
                #         time.sleep(time_sleep)

                #     launch_dungeon(data["launch_dungeon_status"], 0, 0)
                    
                # print("\nDungeon ongoing...")
                # print("Press 'd' to change dungeon")

            time_sleep = uniform(0.22,0.29)
            time.sleep(time_sleep)
        
        # time_sleep = uniform(0.22,0.27)
        # time.sleep(time_sleep)

        sell_stuffs(data["dimension_status"], data)
        if (end_run == 1):
            break
        rejouer_dj(1)
        if (pyautogui.locateOnScreen('../img/no_dimension_energy.jpg', region=(351, 230, 1155, 456), confidence=0.95)):
            break


def launch_dungeon_dimension(data):
    while (pyautogui.locateOnScreen('../img/passage_des_dimensions.png', region=(1426, 197, 353, 148), confidence=0.95) == None):
        time_sleep = uniform(0.16,0.19)
        time.sleep(time_sleep)

    while (pyautogui.locateOnScreen('../img/passage_des_dimensions.png', region=(1426, 197, 353, 148), confidence=0.95)):
        x_click = randint(1476,1717)
        y_click = randint(241,303)
        mouse.position = (x_click, y_click)
        duree = uniform(0.06,0.1)
        time.sleep(duree)
        mouse.press(Button.left)
        mouse.release(Button.left)

        time_sleep = uniform(0.39,0.42)
        time.sleep(time_sleep)
        
    # DE 1 A X POUR LANCER LES AUTRES DONJONS PLUS TARD
    if (data["dimension_status"] == Dimension_type.KARZHAN.value):
        while (pyautogui.locateOnScreen('../img/karzhan.png', region=(1141, 284, 642, 208), confidence=0.95) == None):
            time_sleep = uniform(0.16,0.19)
            time.sleep(time_sleep)
        while (pyautogui.locateOnScreen('../img/karzhan.png', region=(1141, 284, 642, 208), confidence=0.95)):
            x_click = randint(1191,1721)
            y_click = randint(334,445)
            mouse.position = (x_click, y_click)
            duree = uniform(0.06,0.1)
            time.sleep(duree)
            mouse.press(Button.left)
            mouse.release(Button.left)

            time_sleep = uniform(0.44,0.47)
            time.sleep(time_sleep)

# and pyautogui.locateOnScreen('../img/no_dimension_energy.jpg', region=(351, 230, 1155, 456), confidence=0.95) == None

    # time_sleep = uniform(7.44,7.47)
    # time.sleep(time_sleep)

    while (pyautogui.locateOnScreen('../img/niveau_5_dimension.jpg', region=(898, 782, 340, 146), confidence=0.9) == None):
        if (pyautogui.locateOnScreen('../img/niveau_1_dimension.jpg', region=(891, 273, 381, 168), confidence=0.9)):
            while (pyautogui.locateOnScreen('../img/niveau_5_dimension.jpg', region=(898, 782, 340, 146), confidence=0.9) == None):
                descend_liste_dj2()
        time_sleep = uniform(0.16,0.19)
        time.sleep(time_sleep)
    while (pyautogui.locateOnScreen('../img/1_GO.png', region=(1408, 788, 218, 182), confidence=0.95)):
        x_click = randint(1449,1585)
        y_click = randint(843,933)
        mouse.position = (x_click, y_click)
        duree = uniform(0.06,0.1)
        time.sleep(duree)
        mouse.press(Button.left)
        mouse.release(Button.left)

        time_sleep = uniform(0.44,0.47)
        time.sleep(time_sleep)

        if (pyautogui.locateOnScreen('../img/no_dimension_energy.jpg', region=(351, 230, 1155, 456), confidence=0.95)):
            break

    if (pyautogui.locateOnScreen('../img/no_dimension_energy.jpg', region=(351, 230, 1155, 456), confidence=0.95) == None):
        while (pyautogui.locateOnScreen('../img/rejouer_combat_repet_dimension.png', region=(1347, 620, 394, 392), confidence=0.9) == None):
            time_sleep = uniform(0.16,0.19)
            time.sleep(time_sleep)
        
        while (pyautogui.locateOnScreen('../img/rejouer_combat_repet_dimension.png', region=(1347, 620, 394, 392), confidence=0.9)):
            x_pos_mob = pyautogui.locateOnScreen('../img/rejouer_combat_repet_dimension.png', region=(1347, 620, 394, 392), confidence=0.9)
            x_click, y_click = pyautogui.center(x_pos_mob)
            x_click_add = randint(-130,126)
            y_click_add = randint(-47,44)
            x_click += x_click_add
            y_click += y_click_add
            duree = uniform(0.06,0.1)
            pyautogui.click(x_click,y_click,duration=duree)

            time_sleep = uniform(0.41,0.45)
            time.sleep(time_sleep)

        auto_dj_dimension(data)

    time_sleep = uniform(0.45, 0.48)
    time.sleep(time_sleep)

    while (pyautogui.locateOnScreen('../img/no_dimension_energy.jpg', region=(351, 230, 1155, 456), confidence=0.9) == None
           and pyautogui.locateOnScreen('../img/selection_donjon.png', region=(124, 806, 339, 168)) == None):
        time_sleep = uniform(0.36,0.39)
        time.sleep(time_sleep)

    # time_sleep = uniform(0.34,0.37)
    # time.sleep(time_sleep)

    if (pyautogui.locateOnScreen('../img/no_dimension_energy.jpg', region=(351, 230, 1155, 456), confidence=0.9)):
        while (pyautogui.locateOnScreen('../img/no_dimension_energy.jpg', region=(351, 230, 1155, 456), confidence=0.9)):
            x_click = randint(984,1197)
            y_click = randint(597,672)
            mouse.position = (x_click, y_click)
            duree = uniform(0.06,0.1)
            time.sleep(duree)
            mouse.press(Button.left)
            mouse.release(Button.left)

            time_sleep = uniform(0.44,0.47)
            time.sleep(time_sleep)

        while (pyautogui.locateOnScreen('../img/close_launch_run_dj.png', region=(1714, 20, 122, 120), confidence=0.95) == None
               and pyautogui.locateOnScreen('../img/close_cairos_dj.png', region=(1508, 45, 243, 172), confidence=0.9) == None):
                time_sleep = uniform(0.36,0.39)
                time.sleep(time_sleep)

        # time_sleep = uniform(0.34,0.37)
        # time.sleep(time_sleep)

        if (pyautogui.locateOnScreen('../img/close_launch_run_dj.png', region=(1714, 20, 122, 120), confidence=0.95)):
            while (pyautogui.locateOnScreen('../img/close_launch_run_dj.png', region=(1714, 20, 122, 120), confidence=0.95)):
                x_click = randint(1745,1784)
                y_click = randint(53,100)
                mouse.position = (x_click, y_click)
                duree = uniform(0.06,0.1)
                time.sleep(duree)
                mouse.press(Button.left)
                mouse.release(Button.left)

                time_sleep = uniform(0.44,0.47)
                time.sleep(time_sleep)

            while (pyautogui.locateOnScreen('../img/close_cairos_dj.png', region=(1508, 45, 243, 172), confidence=0.9) == None):
                    time_sleep = uniform(0.36,0.39)
                    time.sleep(time_sleep)

        # time_sleep = uniform(0.34,0.37)
        # time.sleep(time_sleep)

        while (pyautogui.locateOnScreen('../img/close_cairos_dj.png', region=(1508, 45, 243, 172), confidence=0.9)):
            x_pos_mob = pyautogui.locateOnScreen('../img/close_cairos_dj.png', region=(1508, 45, 243, 172), confidence=0.9)
            x_click, y_click = pyautogui.center(x_pos_mob)
            x_click_add = randint(-25,25)
            y_click_add = randint(-25,25)
            x_click += x_click_add
            y_click += y_click_add
            mouse.position = (x_click, y_click)
            duree = uniform(0.06,0.1)
            time.sleep(duree)
            mouse.press(Button.left)
            mouse.release(Button.left)

            time_sleep = uniform(0.44,0.47)
            time.sleep(time_sleep)
    else:
        while(pyautogui.locateOnScreen('../img/selection_donjon.png', region=(124, 806, 339, 168))):
            x_click = randint(165,420)
            y_click = randint(861,926)
            mouse.position = (x_click, y_click)
            duree = uniform(0.06,0.1)
            time.sleep(duree)
            mouse.press(Button.left)
            mouse.release(Button.left)

            time_sleep = uniform(0.43,0.46)
            time.sleep(time_sleep)

    while (pyautogui.locateOnScreen('../img/carte_du_monde.jpg', region=(1127, 185, 376, 174), confidence=0.95) == None):
        time_sleep = uniform(0.36,0.39)
        time.sleep(time_sleep)

    # time_sleep = uniform(0.34,0.37)
    # time.sleep(time_sleep)

    while (pyautogui.locateOnScreen('../img/carte_du_monde.jpg', region=(1127, 185, 376, 174), confidence=0.95)):
        x_click = randint(1196,1440)
        y_click = randint(246,302)
        mouse.position = (x_click, y_click)
        duree = uniform(0.06,0.1)
        time.sleep(duree)
        mouse.press(Button.left)
        mouse.release(Button.left)

        time_sleep = uniform(0.39,0.42)
        time.sleep(time_sleep)

def do_dimension(data):
    launch_dungeon_dimension(data)

def do_arena(data):
    do_arena = data["arena_status"]
    if (do_arena == 1 or data["rta_status"]):
        while (pyautogui.locateOnScreen('../img/close_window_combat_repet.png', region=(1598, 95, 164, 134), confidence=0.95) == None
            and pyautogui.locateOnScreen('../img/combat_arena2.png', region=(1351, 330, 437, 213), confidence=0.9) == None):
            time_sleep = uniform(0.22,0.31)
            time.sleep(time_sleep)

        # time_sleep = uniform(0.22,0.31)
        # time.sleep(time_sleep)

        if (pyautogui.locateOnScreen('../img/close_window_combat_repet.png', region=(1598, 95, 164, 134), confidence=0.95)):
            while (pyautogui.locateOnScreen('../img/close_window_combat_repet.png', region=(1598, 95, 164, 134), confidence=0.95)):
                x_click = randint(1669,1717)
                y_click = randint(154,198)
                mouse.position = (x_click, y_click)
                duree = uniform(0.06,0.1)
                time.sleep(duree)
                mouse.press(Button.left)
                mouse.release(Button.left)

                time_sleep = uniform(0.44,0.48)
                time.sleep(time_sleep)

        while (pyautogui.locateOnScreen('../img/combat_arena2.png', region=(1351, 330, 437, 213), confidence=0.9) == None):
            if (pyautogui.locateOnScreen('../img/resultats_arena.png', region=(760, 150, 1079, 211), confidence=0.9)):
                    x_click = randint(1369, 1782)
                    y_click = randint(80, 152)
                    mouse.position = (x_click, y_click)
                    duree = uniform(0.06,0.1)
                    time.sleep(duree)
                    mouse.press(Button.left)
                    mouse.release(Button.left)

                    time_sleep = uniform(0.18,0.21)
                    time.sleep(time_sleep)

            if (pyautogui.locateOnScreen('../img/calculs_arene.png', region=(1351, 330, 437, 213), confidence=0.9)):
                    do_arena = 0
                    break

            time_sleep = uniform(0.04,0.08)
            time.sleep(time_sleep)

        if (pyautogui.locateOnScreen('../img/no_wing_arena.jpg', region=(65, 928, 236, 94), confidence=0.95)):
            do_arena = 0

    if (do_arena == 1):
        auto_arena(data) # good
    else:
        if (data["rta_status"] == 1):
            while (pyautogui.locateOnScreen('../img/combat_amical.png', region=(1332, 540, 476, 245), confidence=0.9) == None):
                x_click = randint(488,801)
                y_click = randint(85,150)
                mouse.position = (x_click, y_click)
                duree = uniform(0.06,0.1)
                time.sleep(duree)
                mouse.press(Button.left)
                mouse.release(Button.left)

                time_sleep = uniform(0.45,0.48)
                time.sleep(time_sleep)

            rta_boucle(data)

        continue_routine(data)

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

def print_msg_auto_dj(data):
    print(f'\nArena_status({data["arena_status"]}) and dungeon ongoing({Dungeon_type(data["launch_dungeon_status"]).name})...')
    print("Press 'd' to change dungeon, press 'a' to do arena, press 'c' to change arena status or 'e' to stop regular dungeon")

def auto_dj(data):
    print_msg_auto_dj(data)
    end = 0
    while (1):
        while (pyautogui.locateOnScreen('../img/rejouer_button.png', region=(846, 828, 302, 125)) == None):
            if (pyautogui.locateOnScreen('../img/waiting_for_repet_battle2.png', region=(62, 97, 127, 356), confidence=0.8)):
                x_click = randint(103,140)
                y_click = randint(312,342)
                duree = uniform(0.06,0.1)
                pyautogui.click(x_click,y_click,duration=duree)
            if (keyboard.is_pressed('c')):
                tmp_arena_status = 9999
                while (tmp_arena_status != 0 and tmp_arena_status != 1):
                        try:
                                tmp_arena_status = int(input("enter arena status (0 or 1): "))
                        except ValueError:
                                pass
                data["arena_status"] = tmp_arena_status
                print_msg_auto_dj(data)
            if (keyboard.is_pressed('e')):
                end = 1
                click_windows()
                while (pyautogui.locateOnScreen('../img/waiting_for_repet_battle2.png', region=(62, 97, 127, 356), confidence=0.8) == None
                        and pyautogui.locateOnScreen('../img/selection_donjon.png', region=(124, 806, 339, 168)) == None
                        and pyautogui.locateOnScreen('../img/fin_des_combats.png', region=(716, 802, 467, 176)) == None):
                    time_sleep = uniform(0.22,0.29)
                    time.sleep(time_sleep)

                if (pyautogui.locateOnScreen('../img/waiting_for_repet_battle2.png', region=(62, 97, 127, 356), confidence=0.8)):
                    x_click = randint(103,140)
                    y_click = randint(312,342)
                    duree = uniform(0.06,0.1)
                    pyautogui.click(x_click,y_click,duration=duree)

                    while (pyautogui.locateOnScreen('../img/vente_selective.png', region=(1406, 831, 356, 135)) == None):
                        time_sleep = uniform(0.22,0.29)
                        time.sleep(time_sleep)

                # stop la run
                if (pyautogui.locateOnScreen('../img/fin_des_combats.png', region=(716, 802, 467, 176))):
                    while (pyautogui.locateOnScreen('../img/fin_des_combats.png', region=(716, 802, 467, 176))):
                        x_click = randint(769,1125)
                        y_click = randint(860,928)
                        duree = uniform(0.06,0.1)
                        pyautogui.click(x_click,y_click,duration=duree)

                        time_sleep = uniform(0.44,0.48)
                        time.sleep(time_sleep)

                    time_sleep = uniform(0.27,0.31)
                    time.sleep(time_sleep)

                    while (pyautogui.locateOnScreen('../img/finir_dj.png', region=(357, 230, 1138, 589)) == None):
                        time_sleep = uniform(0.22,0.29)
                        time.sleep(time_sleep)
                    x_click = randint(675,892)
                    y_click = randint(596,676)
                    duree = uniform(0.06,0.1)
                    pyautogui.click(x_click,y_click,duration=duree)

                    while (pyautogui.locateOnScreen('../img/rejouer_button.png', region=(846, 828, 302, 125)) == None):
                        time_sleep = uniform(0.22,0.29)
                        time.sleep(time_sleep)

                    while (pyautogui.locateOnScreen('../img/selection_donjon.png', region=(124, 806, 339, 168)) == None):
                        time_sleep = uniform(0.22,0.29)
                        time.sleep(time_sleep)

            if (keyboard.is_pressed('a')):
                if (pyautogui.locateOnScreen('../img/rejouer_button.png', region=(846, 828, 302, 125))):
                    continue
                click_windows()
                if (data["arena_status"] == 1):
                    do_arena(data)

            if (pyautogui.locateOnScreen('../img/9_wings.png', region=(72, 931, 219, 90), confidence=0.95)
                or pyautogui.locateOnScreen('../img/10_wings.png', region=(72, 931, 219, 90), confidence=0.95)):
                # click sur le bouton pour fermer la fenetre combat a repet
                if (pyautogui.locateOnScreen('../img/rejouer_button.png', region=(846, 828, 302, 125))):
                    continue
                if (data["arena_status"] == 1):
                    do_arena(data)
                            
            if (keyboard.is_pressed('d')):
                tmp_launch_dungeon_status = 9999
                while (tmp_launch_dungeon_status < 0 or tmp_launch_dungeon_status > 11):
                        try:
                                tmp_launch_dungeon_status = int(input("enter the dungeon to launch:\n0: None| 1: giant | 2: dragon | 3: spiritual realm | 4: necro | 5: fortress | 6: crypt |\n7: r5 | 8: fire rift  | 9: water rift  | 10: wind rift  | 11: light rift  | 12: dark rift : "))
                        except ValueError:
                                pass
                if (data["launch_dungeon_status"] == tmp_launch_dungeon_status):
                    print("\nDungeon already ongoing")
                    print(f'\nDungeon ongoing({Dungeon_type(data["launch_dungeon_status"]).name})...')
                    print("Press 'd' to change dungeon,  press 'a' to do arena or 'e' to stop regular dungeon")
                    continue
                old_dungeon_status = data["launch_dungeon_status"]
                data["launch_dungeon_status"] = tmp_launch_dungeon_status
                click_windows()
                while (pyautogui.locateOnScreen('../img/waiting_for_repet_battle2.png', region=(62, 97, 127, 356), confidence=0.8) == None
                        and pyautogui.locateOnScreen('../img/selection_donjon.png', region=(124, 806, 339, 168)) == None
                        and pyautogui.locateOnScreen('../img/fin_des_combats.png', region=(716, 802, 467, 176)) == None):
                    time_sleep = uniform(0.22,0.29)
                    time.sleep(time_sleep)

                if (pyautogui.locateOnScreen('../img/waiting_for_repet_battle2.png', region=(62, 97, 127, 356), confidence=0.8)):
                    x_click = randint(103,140)
                    y_click = randint(312,342)
                    duree = uniform(0.06,0.1)
                    pyautogui.click(x_click,y_click,duration=duree)
                    # x_pos_mob = pyautogui.locateOnScreen('../img/waiting_for_repet_battle2.png', region=(62, 97, 127, 356), confidence=0.8)
                    # x_click, y_click = pyautogui.center(x_pos_mob)
                    # x_click_add = randint(-15,15)
                    # y_click_add = randint(-15,15)
                    # x_click += x_click_add
                    # y_click += y_click_add
                    # duree = uniform(0.06,0.1)
                    # pyautogui.click(x_click,y_click,duration=duree)

                    while (pyautogui.locateOnScreen('../img/vente_selective.png', region=(1406, 831, 356, 135)) == None):
                        time_sleep = uniform(0.22,0.29)
                        time.sleep(time_sleep)

                # stop la run
                if (pyautogui.locateOnScreen('../img/fin_des_combats.png', region=(716, 802, 467, 176))):
                    while (pyautogui.locateOnScreen('../img/fin_des_combats.png', region=(716, 802, 467, 176))):
                        x_click = randint(769,1125)
                        y_click = randint(860,928)
                        duree = uniform(0.06,0.1)
                        pyautogui.click(x_click,y_click,duration=duree)

                        time_sleep = uniform(0.44,0.48)
                        time.sleep(time_sleep)

                    time_sleep = uniform(0.27,0.31)
                    time.sleep(time_sleep)

                    while (pyautogui.locateOnScreen('../img/finir_dj.png', region=(357, 230, 1138, 589)) == None):
                        time_sleep = uniform(0.22,0.29)
                        time.sleep(time_sleep)
                    x_click = randint(675,892)
                    y_click = randint(596,676)
                    duree = uniform(0.06,0.1)
                    pyautogui.click(x_click,y_click,duration=duree)

                    while (pyautogui.locateOnScreen('../img/rejouer_button.png', region=(846, 828, 302, 125)) == None):
                        time_sleep = uniform(0.22,0.29)
                        time.sleep(time_sleep)

                    while (pyautogui.locateOnScreen('../img/selection_donjon.png', region=(124, 806, 339, 168)) == None):
                        time_sleep = uniform(0.22,0.29)
                        time.sleep(time_sleep)


                # lance le nouveau donjon
                if (pyautogui.locateOnScreen('../img/selection_donjon.png', region=(124, 806, 339, 168))):
                    sell_stuffs(old_dungeon_status, data)

                    while (pyautogui.locateOnScreen('../img/selection_donjon.png', region=(124, 806, 339, 168)) == None):
                        time_sleep = uniform(0.22,0.29)
                        time.sleep(time_sleep)

                    while (pyautogui.locateOnScreen('../img/selection_donjon.png', region=(124, 806, 339, 168))):
                        x_click = randint(165,420)
                        y_click = randint(861,926)
                        duree = uniform(0.06,0.1)
                        pyautogui.click(x_click,y_click,duration=duree)

                        time_sleep = uniform(0.44,0.48)
                        time.sleep(time_sleep)

                    launch_dungeon(data["launch_dungeon_status"], 0, 0, data)
                    
                print_msg_auto_dj(data)

            time_sleep = uniform(0.22,0.29)
            time.sleep(time_sleep)
        
        # time_sleep = uniform(0.22,0.27)
        # time.sleep(time_sleep)
        
        sell_stuffs(data["launch_dungeon_status"], data)
        if (end == 1):
            while (pyautogui.locateOnScreen('../img/selection_donjon.png', region=(124, 806, 339, 168)) == None):
                time_sleep = uniform(0.36,0.39)
                time.sleep(time_sleep)

            x_click = randint(165,420)
            y_click = randint(861,926)
            duree = uniform(0.06,0.1)
            pyautogui.click(x_click,y_click,duration=duree)

            while (pyautogui.locateOnScreen('../img/donjon_cairos_button.png', region=(1160, 445, 605, 187), confidence=0.95) == None):
                time_sleep = uniform(0.36,0.39)
                time.sleep(time_sleep)
            break
        rejouer_dj(1)

        # if (pyautogui.pixelMatchesColor(1197, 649, (202, 161, 71))):
        if (pyautogui.pixelMatchesColor(1202, 654, (100, 78, 33))):
            break

def auto_arena(data):
    while (pyautogui.locateOnScreen('../img/arena.png', region=(718, 107, 508, 127), confidence=0.9) == None):
        if (pyautogui.locateOnScreen('../img/journal_arena.png', region=(1131, 842, 178, 186), confidence=0.9)):
            x_click = randint(1160,1270)
            y_click = randint(903,993)
            mouse.position = (x_click, y_click)
            duree = uniform(0.06,0.1)
            time.sleep(duree)
            mouse.press(Button.left)
            mouse.release(Button.left)
        time_sleep = uniform(0.02,0.09)
        time.sleep(time_sleep)

    # if (pyautogui.locateOnScreen('../img/onglet_rival_selected.png', region=(237, 333, 227, 113), confidence=0.85) == None
    #     or pyautogui.locateOnScreen('../img/onglet_rival_no_selected.png', region=(237, 333, 227, 113), confidence=0.85) == None):

    do_arena_status = rivaux.auto_rivaux()
    # rivaux.auto_rivaux_collab()

    if (do_arena_status == 1):
        auto_combat(data)
    else:
        while (pyautogui.locateOnScreen('../img/combat_arena2.png', region=(1351, 330, 437, 213), confidence=0.9) == None):
            x_click = randint(1579,1638)
            y_click = randint(165,217)
            mouse.position = (x_click, y_click)
            duree = uniform(0.06,0.1)
            time.sleep(duree)
            mouse.press(Button.left)
            mouse.release(Button.left)

            time_sleep = uniform(0.45,0.48)
            time.sleep(time_sleep)

        if (data["rta_status"] == 1):
            while (pyautogui.locateOnScreen('../img/combat_amical.png', region=(1332, 540, 476, 245), confidence=0.9) == None):
                x_click = randint(488,801)
                y_click = randint(85,150)
                mouse.position = (x_click, y_click)
                duree = uniform(0.06,0.1)
                time.sleep(duree)
                mouse.press(Button.left)
                mouse.release(Button.left)

                time_sleep = uniform(0.45,0.48)
                time.sleep(time_sleep)

            rta_boucle(data)

        continue_routine(data)

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

def print_msg_routine(data):
    print("\nWaiting for another routine...")
    print(f'Press \'enter\' to change parameters (change dungeon({Dungeon_type(data["launch_dungeon_status"]).name}), do rta({data["rta_status"]}), dimension status({Dimension_type(data["dimension_status"]).name}), do arena({data["arena_status"]}))')
    print("Press 'r' to do a routine")

def get_current_energy():
    pyt.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract"

    img = pyautogui.screenshot(region=(861, 230, 230, 81))

    img2 = np.array(img)
    
    img2 = cv2.resize(img2, (0, 0), fx=2, fy=2)

    # Convert to HSV color-space
    hsv = cv2.cvtColor(img2, cv2.COLOR_BGR2HSV)

    # Get the binary mask
    msk = cv2.inRange(hsv, np.array([0, 0, 123]), np.array([179, 255, 255]))

    text = pyt.image_to_string(msk)

    for charr in range(0, len(text)):
        if (text[charr] == '/'):
            text = text[:charr]
            break
    return text
    

def continue_routine(data):

    auto_dj(data) # ------------------------------------------ FIN DJ ------------------------------------------

    if (pyautogui.locateOnScreen('../img/donjon_cairos_button.png', region=(1160, 445, 605, 187), confidence=0.95) == None):
        while (pyautogui.locateOnScreen('../img/close_energy_box.png', region=(1302, 251, 125, 120), confidence=0.95) == None):
                time_sleep = uniform(0.36,0.39)
                time.sleep(time_sleep)

    # time_sleep = uniform(0.34,0.37)
    # time.sleep(time_sleep)


        while (pyautogui.locateOnScreen('../img/close_energy_box.png', region=(1302, 251, 125, 120), confidence=0.95)):
            x_click = randint(1332,1393)
            y_click = randint(287,343)
            mouse.position = (x_click, y_click)
            duree = uniform(0.06,0.1)
            time.sleep(duree)
            mouse.press(Button.left)
            mouse.release(Button.left)

            time_sleep = uniform(0.44,0.47)
            time.sleep(time_sleep)

        while (pyautogui.locateOnScreen('../img/close_launch_run_dj.png', region=(1714, 20, 122, 120), confidence=0.95) == None):
                time_sleep = uniform(0.36,0.39)
                time.sleep(time_sleep)

        # time_sleep = uniform(0.34,0.37)
        # time.sleep(time_sleep)

        while (pyautogui.locateOnScreen('../img/close_launch_run_dj.png', region=(1714, 20, 122, 120), confidence=0.95)):
            x_click = randint(1745,1784)
            y_click = randint(53,100)
            mouse.position = (x_click, y_click)
            duree = uniform(0.06,0.1)
            time.sleep(duree)
            mouse.press(Button.left)
            mouse.release(Button.left)

            time_sleep = uniform(0.44,0.47)
            time.sleep(time_sleep)

        while (pyautogui.locateOnScreen('../img/close_cairos_dj.png', region=(1508, 45, 243, 172), confidence=0.9) == None):
                time_sleep = uniform(0.36,0.39)
                time.sleep(time_sleep)

        # time_sleep = uniform(0.34,0.37)
        # time.sleep(time_sleep)

        while (pyautogui.locateOnScreen('../img/close_cairos_dj.png', region=(1508, 45, 243, 172), confidence=0.9)):
            x_pos_mob = pyautogui.locateOnScreen('../img/close_cairos_dj.png', region=(1508, 45, 243, 172), confidence=0.9)
            x_click, y_click = pyautogui.center(x_pos_mob)
            x_click_add = randint(-25,25)
            y_click_add = randint(-25,25)
            x_click += x_click_add
            y_click += y_click_add
            mouse.position = (x_click, y_click)
            duree = uniform(0.06,0.1)
            time.sleep(duree)
            mouse.press(Button.left)
            mouse.release(Button.left)

            time_sleep = uniform(0.44,0.47)
            time.sleep(time_sleep)

    # ------------------------------------------ dimension ------------------------------------------

    # de 1 a X plus tard !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    if (data["dimension_status"] > Dimension_type.NONE.value and data["dimension_status"] <= Dimension_type.KARZHAN.value):
        do_dimension(data)

    # ------------------------------------------ dimension ------------------------------------------

    # ------------------------------------------ FIN ------------------------------------------
    if (data["launch_dungeon_status"] == Dungeon_type.NONE.value):
        data["launch_dungeon_status"] = default_donjon
    data["dimension_status"] = Dimension_type.NONE.value
    data["rta_status"] = 0
    data["world_boss_status"] = 0
    data["gvg_status"] = 0
    print_msg_routine(data)
    current_energy = re.findall("\d++", get_current_energy())
    while (pyautogui.locateOnScreen('../img/9_wings.png', region=(72, 931, 219, 90), confidence=0.95) == None
                and pyautogui.locateOnScreen('../img/10_wings.png', region=(72, 931, 219, 90), confidence=0.95) == None
                and len(current_energy) == 1 and int(current_energy[0]) < data["min_energy_launch_dungeon"]):
        if (keyboard.is_pressed('r')):
            click_windows()
            break
        if (keyboard.is_pressed('enter')):
            tmp_launch_dungeon_status = 9999
            while (tmp_launch_dungeon_status < Dungeon_type.NONE.value or tmp_launch_dungeon_status > Dungeon_type.DARK_RIFT.value):
                    try:
                            tmp_launch_dungeon_status = int(input("enter the dungeon to launch:\n0: None| 1: giant | 2: dragon | 3: spiritual realm | 4: necro | 5: fortress | 6: crypt |\n7: r5 | 8: fire rift  | 9: water rift  | 10: wind rift  | 11: light rift  | 12: dark rift : "))
                    except ValueError:
                            pass
            data["launch_dungeon_status"] = tmp_launch_dungeon_status

            tmp_dimension_status = 9999
            while (tmp_dimension_status < Dimension_type.NONE.value or tmp_dimension_status > Dimension_type.KARZHAN.value):
                    try:
                            tmp_dimension_status = int(input(f'enter dimension status (12: None 13: karzhan (only karzhan for now)): '))
                    except ValueError:
                            pass
            data["dimension_status"] = tmp_dimension_status

            tmp_rta_status = 9999
            while (tmp_rta_status != 0 and tmp_rta_status != 1):
                    try:
                            tmp_rta_status = int(input("enter rta status (0 or 1): "))
                    except ValueError:
                            pass
            data["rta_status"] = tmp_rta_status

            tmp_arena_status = 9999
            while (tmp_arena_status != 0 and tmp_arena_status != 1):
                    try:
                            tmp_arena_status = int(input("enter arena status (0 or 1): "))
                    except ValueError:
                            pass
            data["arena_status"] = tmp_arena_status

            # click_windows()
            print_msg_routine(data)

        time_sleep = uniform(0.52,0.56)
        time.sleep(time_sleep)

        current_energy = re.findall("\d++", get_current_energy())

    do_arena = data["arena_status"]
    launch_dungeon(data["launch_dungeon_status"], 0, 1, data)

    # do_arena = data["arena_status"]
    # if (do_arena == 1):
    #     while (pyautogui.locateOnScreen('../img/close_window_combat_repet.png', region=(1598, 95, 164, 134), confidence=0.95) == None
    #         and pyautogui.locateOnScreen('../img/combat_arena2.png', region=(1351, 330, 437, 213), confidence=0.9) == None):
    #         time_sleep = uniform(0.22,0.31)
    #         time.sleep(time_sleep)

    if (do_arena == 1 or data["rta_status"] == 1):
        while (pyautogui.locateOnScreen('../img/combat_arena2.png', region=(1351, 330, 437, 213), confidence=0.9) == None):
            if (pyautogui.locateOnScreen('../img/resultats_arena.png', region=(760, 150, 1079, 211), confidence=0.9)):
                    x_click = randint(1369, 1782)
                    y_click = randint(80, 152)
                    mouse.position = (x_click, y_click)
                    duree = uniform(0.06,0.1)
                    time.sleep(duree)
                    mouse.press(Button.left)
                    mouse.release(Button.left)

                    time_sleep = uniform(0.18,0.21)
                    time.sleep(time_sleep)

            if (pyautogui.locateOnScreen('../img/calculs_arene.png', region=(1351, 330, 437, 213), confidence=0.9)):
                    do_arena = 0
                    break

            time_sleep = uniform(0.04,0.08)
            time.sleep(time_sleep)

        if (pyautogui.locateOnScreen('../img/no_wing_arena.jpg', region=(65, 928, 236, 94), confidence=0.95)):
            do_arena = 0

    # click sur combat en arene
    # x_click = randint(1401,1749)
    # y_click = randint(392,505)
    # mouse.position = (x_click, y_click)
    # duree = uniform(0.06,0.1)
    # time.sleep(duree)
    # mouse.press(Button.left)
    # mouse.release(Button.left)

    if (do_arena == 1):
        auto_arena(data) # good
    else:
        if (data["rta_status"] == 1):
            while (pyautogui.locateOnScreen('../img/combat_amical.png', region=(1332, 540, 476, 245), confidence=0.9) == None):
                x_click = randint(488,801)
                y_click = randint(85,150)
                mouse.position = (x_click, y_click)
                duree = uniform(0.06,0.1)
                time.sleep(duree)
                mouse.press(Button.left)
                mouse.release(Button.left)

                time_sleep = uniform(0.45,0.48)
                time.sleep(time_sleep)

            rta_boucle(data)

        continue_routine(data)

def check_team_and_run():
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
            time_sleep = uniform(0.42,0.45)
            time.sleep(time_sleep)

    while (pyautogui.locateOnScreen('../img/go_arena.jpg', region=(1307, 589, 470, 275), confidence=0.95) == None):
        time_sleep = uniform(0.03,0.06)
        time.sleep(time_sleep)

    while (pyautogui.locateOnScreen('../img/go_arena.jpg', region=(1307, 589, 470, 275), confidence=0.95)):
        x_click = randint(1392,1693)
        y_click = randint(674,800)
        mouse.position = (x_click, y_click)
        duree = uniform(0.06,0.1)
        time.sleep(duree)
        mouse.press(Button.left)
        mouse.release(Button.left)

        time_sleep = uniform(0.42,0.45)
        time.sleep(time_sleep)

def auto_combat(data):
    while (pyautogui.locateOnScreen('../img/rafraichir_liste.png', region=(1250, 224, 328, 108), confidence=0.95) == None):
        # click sur l'onglet des joueurs
        x_click = randint(255,442)
        y_click = randint(241,302)
        duree = uniform(0.06,0.1)
        pyautogui.click(x_click,y_click,duration=duree)

        time_sleep = uniform(0.42,0.48)
        time.sleep(time_sleep)

    # click sur rafraichir la liste
    x_click = randint(1273,1552)
    y_click = randint(249,304)
    duree = uniform(0.06,0.1)
    pyautogui.click(x_click,y_click,duration=duree)

    time_sleep = uniform(0.2,0.25)
    time.sleep(time_sleep)

    while (pyautogui.locateOnScreen('../img/liste_arene.png', region=(1327, 321, 236, 585), confidence=0.95) == None):
        if (pyautogui.locateOnScreen('../img/rafraichir_liste_button.png', region=(606, 513, 661, 127))):
            x_click = randint(629,1246)
            y_click = randint(541,617)
            duree = uniform(0.06,0.1)
            pyautogui.click(x_click,y_click,duration=duree)
        time_sleep = uniform(0.02,0.09)
        time.sleep(time_sleep)

    while (True):
        combat_pos = list(pyautogui.locateAllOnScreen('../img/fight_icon.png', region=(1386, 331, 163, 560), confidence=0.95))
        for i in combat_pos:
            x_click_add = randint(26, 114)
            y_click_add = randint(32, 80)
            mouse.position = (i[0] + x_click_add, i[1] + y_click_add)
            duree = uniform(0.06,0.1)
            time.sleep(duree)
            mouse.press(Button.left)
            mouse.release(Button.left)

            time_sleep = uniform(0.44,0.47)
            time.sleep(time_sleep)

            while (pyautogui.locateOnScreen('../img/in_arena2.png', region=(1368, 649, 354, 179), confidence=0.9) == None
                    and pyautogui.locateOnScreen('../img/deja_battu.png', region=(407, 267, 1053, 521), confidence=0.95) == None):
                x_click_add = randint(26, 114)
                y_click_add = randint(32, 80)
                mouse.position = (i[0] + x_click_add, i[1] + y_click_add)
                duree = uniform(0.06,0.1)
                time.sleep(duree)
                mouse.press(Button.left)
                mouse.release(Button.left)
                if (pyautogui.locateOnScreen('../img/end_arena.png', region=(473, 277, 925, 271), confidence=0.95)):
                    print("T'as plus d'aile garcon")
                    # click sur les 2 croix
                    while (pyautogui.locateOnScreen('../img/end_arena.png', region=(473, 277, 925, 271), confidence=0.95)):
                        x_click = randint(1330,1396)
                        y_click = randint(285,343)
                        mouse.position = (x_click, y_click)
                        duree = uniform(0.06,0.1)
                        time.sleep(duree)
                        mouse.press(Button.left)
                        mouse.release(Button.left)

                        time_sleep = uniform(0.44,0.47)
                        time.sleep(time_sleep)

                    while (pyautogui.locateOnScreen('../img/close_list_arena.png', region=(1546, 125, 126, 128), confidence=0.95)):
                        x_click = randint(1574,1638)
                        y_click = randint(165,217)
                        mouse.position = (x_click, y_click)
                        duree = uniform(0.06,0.1)
                        time.sleep(duree)
                        mouse.press(Button.left)
                        mouse.release(Button.left)

                        time_sleep = uniform(0.44,0.47)
                        time.sleep(time_sleep)

                    while (pyautogui.locateOnScreen('../img/combat_arena.png', region=(1372, 352, 404, 184), confidence=0.9) == None):
                        time_sleep = uniform(0.22,0.31)
                        time.sleep(time_sleep)

                    # RTA ICIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII

                    if (data["rta_status"] == 1):
                        while (pyautogui.locateOnScreen('../img/combat_amical.png', region=(1332, 540, 476, 245), confidence=0.9) == None):
                            x_click = randint(488,801)
                            y_click = randint(85,150)
                            mouse.position = (x_click, y_click)
                            duree = uniform(0.06,0.1)
                            time.sleep(duree)
                            mouse.press(Button.left)
                            mouse.release(Button.left)

                            time_sleep = uniform(0.45,0.48)
                            time.sleep(time_sleep)

                        rta_boucle(data)

                    continue_routine(data)

                time_sleep = uniform(0.88,0.91)
                time.sleep(time_sleep)

            if (pyautogui.locateOnScreen('../img/deja_battu.png', region=(407, 267, 1053, 521), confidence=0.95)):
                x_click = randint(827,1048)
                y_click = randint(593,677)
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
            check_team_and_run()

            nb_mob = 4 - len(list(pyautogui.locateAllOnScreen('../img/empty_slot_arena.png', region=(1097, 204, 550, 379), confidence=0.98)))
            lance_sorts_en_arene(nb_mob)

            while (pyautogui.locateOnScreen('../img/rafraichir_liste.png', region=(1250, 224, 328, 108), confidence=0.95) == None):
                time_sleep = uniform(0.07,0.09)
                time.sleep(time_sleep)

        if (pyautogui.locateOnScreen('../img/end_arena_list.png', region=(513, 737, 1062, 172), confidence=0.9)):
            break
        while (len(list(pyautogui.locateAllOnScreen('../img/fight_icon.png', region=(1386, 331, 163, 560), confidence=0.95))) < 3
                and (pyautogui.locateOnScreen('../img/end_arena_list.png', region=(513, 737, 1062, 172), confidence=0.9) == None)):
            descend_liste()
            time_sleep = uniform(0.55,0.63)
            time.sleep(time_sleep)

        # time_sleep = uniform(0.22,0.31)
        # time.sleep(time_sleep)

    auto_combat(data)

def ou_est_la_cible_emplacement_deux_ou_quatre_rta():
    fIn = 0
    si_trois_emplacement_vide = 3*[0]
    while fIn == 0:
        empla_vide = 0
        cHoix = randint(0,2)
        if cHoix == 0 and si_trois_emplacement_vide[0] == 0:    
            if pyautogui.locateOnScreen('../img/emplacement_vide1_rta.png', region=(633, 267, 226, 268), grayscale=True, confidence=0.9) == None:
                x_cible1_arene = randint(720,796)
                y_cible1_arene = randint(407,479)
                duree = uniform(0.06,0.1)
                pyautogui.click(x_cible1_arene,y_cible1_arene,duration=duree)
                fIn = 1
            else:
                si_trois_emplacement_vide[0] = 1
                
        if cHoix == 1 and si_trois_emplacement_vide[1] == 0:               
            if pyautogui.locateOnScreen('../img/emplacement_vide2_rta.png', region=(873, 267, 246, 268), grayscale=True, confidence=0.9) == None:
                x_cible1_arene = randint(954,1030)
                y_cible1_arene = randint(395,471)
                duree = uniform(0.06,0.1)
                pyautogui.click(x_cible1_arene,y_cible1_arene,duration=duree)
                fIn = 1
            else:
                si_trois_emplacement_vide[1] = 1

        if cHoix == 2 and si_trois_emplacement_vide[2] == 0:
            if pyautogui.locateOnScreen('../img/emplacement_vide3_rta.png', region=(1100, 278, 245, 257), grayscale=True, confidence=0.9) == None:
                x_cible1_arene = randint(1171,1257)
                y_cible1_arene = randint(419,494)
                duree = uniform(0.06,0.1)
                pyautogui.click(x_cible1_arene,y_cible1_arene,duration=duree)
                fIn = 1
            else:
                si_trois_emplacement_vide[2] = 1

        for i in range(len(si_trois_emplacement_vide)):
            empla_vide = empla_vide + si_trois_emplacement_vide[i]

        if empla_vide == 3:
            x_cible1_arene = randint(1388,1468)
            y_cible1_arene = randint(451,543)
            duree = uniform(0.06,0.1)
            pyautogui.click(x_cible1_arene,y_cible1_arene,duration=duree)
            fIn = 1

def click_allies_rta():
    duree = uniform(0.06,0.1)
    x_sort2 = randint(203, 1209)
    y_sort2 = randint(661, 891)
    pyautogui.click(x_sort2, y_sort2, duration = duree)

def lance_sorts_en_rta(data):
    # time_sleep = uniform(0.28,0.49)
    # time.sleep(time_sleep)
    combat_finit = 0
    while  combat_finit == 0:
        #auto woonsa
        if pyautogui.locateOnScreen('../img/sort1_woonsa.png', region=(1273, 840, 188, 188), grayscale=True, confidence=0.8) != None:
            #sort 3 woonsa
            if pyautogui.locateOnScreen('../img/sort3_woonsa.png', region=(1640, 849, 166, 177), grayscale=True, confidence=0.8) != None:
                duree = uniform(0.06,0.1)
                x_sort3 = randint(1662, 1786)
                y_sort3 = randint(877, 1002)
                pyautogui.click(x_sort3, y_sort3, duration = duree)
                while pyautogui.locateOnScreen('../img/sort3_woonsa.png', region=(1640, 849, 166, 177), grayscale=True, confidence=0.8) != None:
                    ou_est_la_cible_emplacement_deux_ou_quatre_rta()
            #sort 2 woonsa
            if pyautogui.locateOnScreen('../img/sort2_woonsa.png', region=(1462, 850, 171, 182), grayscale=True, confidence=0.8) != None:
                duree = uniform(0.06,0.1)
                x_sort2 = randint(1487, 1612)
                y_sort2 = randint(876, 1002)
                pyautogui.click(x_sort2, y_sort2, duration = duree)
                while pyautogui.locateOnScreen('../img/sort2_woonsa.png', region=(1462, 850, 171, 182), grayscale=True, confidence=0.8) != None:
                    ou_est_la_cible_emplacement_deux_ou_quatre_rta()
            #sort 1 woonsa           
            if pyautogui.locateOnScreen('../img/sort1_woonsa.png', region=(1273, 840, 188, 188), grayscale=True, confidence=0.8) != None:
                while pyautogui.locateOnScreen('../img/sort1_woonsa.png', region=(1273, 840, 188, 188), grayscale=True, confidence=0.8) != None:
                    ou_est_la_cible_emplacement_deux_ou_quatre_rta()
        #auto moore
        elif pyautogui.locateOnScreen('../img/sort1_moore.png', region=(1273, 840, 188, 188), grayscale=True, confidence=0.8) != None:
            #sort 2 moore
            if pyautogui.locateOnScreen('../img/sort2_moore.png', region=(1462, 850, 171, 182), grayscale=True, confidence=0.8) != None:
                duree = uniform(0.06,0.1)
                x_sort2 = randint(1487, 1612)
                y_sort2 = randint(876, 1002)
                pyautogui.click(x_sort2, y_sort2, duration = duree)
                while pyautogui.locateOnScreen('../img/sort2_moore.png', region=(1462, 850, 171, 182), grayscale=True, confidence=0.8) != None:
                    ou_est_la_cible_emplacement_deux_ou_quatre_rta()
            #sort 1 moore           
            if pyautogui.locateOnScreen('../img/sort1_moore.png', region=(1273, 840, 188, 188), grayscale=True, confidence=0.8) != None:
                while pyautogui.locateOnScreen('../img/sort1_moore.png', region=(1273, 840, 188, 188), grayscale=True, confidence=0.8) != None:
                    ou_est_la_cible_emplacement_deux_ou_quatre_rta()

        #auto cheongpung
        elif pyautogui.locateOnScreen('../img/sort1_cp.png', region=(1273, 840, 188, 188), grayscale=True, confidence=0.8) != None:
            #sort 3 cheongpung
            if pyautogui.locateOnScreen('../img/sort3_cp.png', region=(1640, 849, 166, 177), grayscale=True, confidence=0.8) != None:
                duree = uniform(0.06,0.1)
                x_sort3 = randint(1662, 1786)
                y_sort3 = randint(877, 1002)
                pyautogui.click(x_sort3, y_sort3, duration = duree)
                while pyautogui.locateOnScreen('../img/sort3_cp.png', region=(1640, 849, 166, 177), grayscale=True, confidence=0.8) != None:
                    ou_est_la_cible_emplacement_deux_ou_quatre_rta()
            #sort 2 cheongpung
            if pyautogui.locateOnScreen('../img/sort2_cp.png', region=(1462, 850, 171, 182), grayscale=True, confidence=0.8) != None:
                duree = uniform(0.06,0.1)
                x_sort2 = randint(1487, 1612)
                y_sort2 = randint(876, 1002)
                pyautogui.click(x_sort2, y_sort2, duration = duree)
                while pyautogui.locateOnScreen('../img/sort2_cp.png', region=(1462, 850, 171, 182), grayscale=True, confidence=0.8) != None:
                    ou_est_la_cible_emplacement_deux_ou_quatre_rta()
            #sort 1 cheongpung           
            if pyautogui.locateOnScreen('../img/sort1_cp.png', region=(1273, 840, 188, 188), grayscale=True, confidence=0.8) != None:
                while pyautogui.locateOnScreen('../img/sort1_cp.png', region=(1273, 840, 188, 188), grayscale=True, confidence=0.8) != None:
                    ou_est_la_cible_emplacement_deux_ou_quatre_rta()

        # auto bellenus 1ere forme
        elif pyautogui.locateOnScreen('../img/sort1_bellenus.png', region=(1273, 840, 188, 188), grayscale=True, confidence=0.9) != None:
            #sort 3 bellenus
            if pyautogui.locateOnScreen('../img/sort3_bellenus.png', region=(1640, 849, 166, 177), grayscale=True, confidence=0.8) != None:
                duree = uniform(0.06,0.1)
                x_sort3 = randint(1662, 1786)
                y_sort3 = randint(877, 1002)
                pyautogui.click(x_sort3, y_sort3, duration = duree)
                while pyautogui.locateOnScreen('../img/sort3_bellenus.png', region=(1640, 849, 166, 177), grayscale=True, confidence=0.8) != None:
                    ou_est_la_cible_emplacement_deux_ou_quatre_rta()
            #sort 1 bellenus           
            if pyautogui.locateOnScreen('../img/sort1_bellenus.png', region=(1273, 840, 188, 188), grayscale=True, confidence=0.8) != None:
                while pyautogui.locateOnScreen('../img/sort1_bellenus.png', region=(1273, 840, 188, 188), grayscale=True, confidence=0.8) != None:
                    ou_est_la_cible_emplacement_deux_ou_quatre_rta()

        # auto bellenus 2e forme
        elif pyautogui.locateOnScreen('../img/sort1_bellenus2.png', region=(1273, 840, 188, 188), grayscale=True, confidence=0.9) != None:
            #sort 2 bellenus
            if pyautogui.locateOnScreen('../img/sort2_bellenus2.png', region=(1462, 850, 171, 182), grayscale=True, confidence=0.8) != None:
                duree = uniform(0.06,0.1)
                x_sort2 = randint(1487, 1612)
                y_sort2 = randint(876, 1002)
                pyautogui.click(x_sort2, y_sort2, duration = duree)
                while pyautogui.locateOnScreen('../img/sort2_bellenus2.png', region=(1462, 850, 171, 182), grayscale=True, confidence=0.8) != None:
                    ou_est_la_cible_emplacement_deux_ou_quatre_rta()
            #sort 1 bellenus           
            if pyautogui.locateOnScreen('../img/sort1_bellenus2.png', region=(1273, 840, 188, 188), grayscale=True, confidence=0.8) != None:
                while pyautogui.locateOnScreen('../img/sort1_bellenus2.png', region=(1273, 840, 188, 188), grayscale=True, confidence=0.8) != None:
                    ou_est_la_cible_emplacement_deux_ou_quatre_rta()

        # auto maximilian
        elif pyautogui.locateOnScreen('../img/sort1_maximilian.png', region=(1273, 840, 188, 188), grayscale=True, confidence=0.8) != None:
            #sort 3 maximilian
            if pyautogui.locateOnScreen('../img/sort3_maximilian.png', region=(1640, 849, 166, 177), grayscale=True, confidence=0.8) != None:
                duree = uniform(0.06,0.1)
                x_sort3 = randint(1662, 1786)
                y_sort3 = randint(877, 1002)
                pyautogui.click(x_sort3, y_sort3, duration = duree)
                while pyautogui.locateOnScreen('../img/sort3_maximilian.png', region=(1640, 849, 166, 177), grayscale=True, confidence=0.8) != None:
                    ou_est_la_cible_emplacement_deux_ou_quatre_rta()
            #sort 2 maximilian
            if pyautogui.locateOnScreen('../img/sort2_maximilian.png', region=(1462, 850, 171, 182), grayscale=True, confidence=0.8) != None:
                duree = uniform(0.06,0.1)
                x_sort2 = randint(1487, 1612)
                y_sort2 = randint(876, 1002)
                pyautogui.click(x_sort2, y_sort2, duration = duree)
                while pyautogui.locateOnScreen('../img/sort2_maximilian.png', region=(1462, 850, 171, 182), grayscale=True, confidence=0.8) != None:
                    ou_est_la_cible_emplacement_deux_ou_quatre_rta()
            #sort 1 maximilian           
            if pyautogui.locateOnScreen('../img/sort1_maximilian.png', region=(1273, 840, 188, 188), grayscale=True, confidence=0.8) != None:
                while pyautogui.locateOnScreen('../img/sort1_maximilian.png', region=(1273, 840, 188, 188), grayscale=True, confidence=0.8) != None:
                    ou_est_la_cible_emplacement_deux_ou_quatre_rta()
            
        elif pyautogui.locateOnScreen('../img/victory_rta.png', region=(556, 110, 734, 177), confidence=0.85) != None:
            while (pyautogui.locateOnScreen('../img/victory_rta.png', region=(556, 110, 734, 177), confidence=0.85)):
                x_click = randint(314,1374)
                y_click = randint(386,840)
                duree = uniform(0.06,0.1)
                pyautogui.click(x_click,y_click,duration=duree)
                time_sleep = uniform(0.28,0.49)
                time.sleep(time_sleep)
            combat_finit = 1
            
        elif pyautogui.locateOnScreen('../img/defeated_rta.png', region = (605, 106, 641, 200), confidence = 0.52) != None:
            while (pyautogui.locateOnScreen('../img/defeated_rta.png', region=(605, 106, 641, 200), confidence = 0.52)):
                x_click = randint(314,1374)
                y_click = randint(386,840)
                duree = uniform(0.06,0.1)
                pyautogui.click(x_click,y_click,duration=duree)
                time_sleep = uniform(0.28,0.49)
                time.sleep(time_sleep)
            combat_finit = 1
        check_opponent_quit(data)


def check_opponent_quit(data):
    if (pyautogui.locateOnScreen('../img/opponent_quit.png', region=(403, 255, 1070, 551),confidence=0.9)):
        while (pyautogui.locateOnScreen('../img/combat_amical.png', region=(1332, 540, 476, 245), confidence=0.9) == None):
            x_click = randint(829,1043)
            y_click = randint(595,679)
            duree = uniform(0.06,0.1)
            pyautogui.click(x_click,y_click,duration=duree)

            time_sleep = uniform(0.42,0.47)
            time.sleep(time_sleep)
        rta_boucle(data)

#ici remplacer
def rta_boucle(data):
    # Check si l'adversaire quitte le combat pendant la draft ou si l'un des 5 monstres est pris en fasse et quitter
    # nb_combat_rta = 25
    # cmp = 0
    while (1):
        while (pyautogui.locateOnScreen('../img/combat_amical.png', region=(1332, 540, 476, 245), confidence=0.9) == None):
            check_opponent_quit(data)
            if (pyautogui.locateOnScreen('../img/resultats_rta.png', region=(760, 150, 1079, 211), confidence=0.85)):
                x_click = randint(1369, 1782)
                y_click = randint(80, 152)
                mouse.position = (x_click, y_click)
                duree = uniform(0.06,0.1)
                time.sleep(duree)
                mouse.press(Button.left)
                mouse.release(Button.left)
            time_sleep = uniform(0.25,0.29)
            time.sleep(time_sleep)

        if (pyautogui.locateOnScreen('../img/waiting_for_repet_battle2.png', region=(62, 97, 127, 356), confidence=0.8)):
            while (pyautogui.locateOnScreen('../img/combat_a_repet.jpg', region=(105, 92, 638, 170), confidence=0.8) == None):
                x_click = randint(103,140)
                y_click = randint(312,342)
                duree = uniform(0.06,0.1)
                pyautogui.click(x_click,y_click,duration=duree)
                # x_pos_mob = pyautogui.locateOnScreen('../img/waiting_for_repet_battle2.png', region=(62, 97, 127, 356), confidence=0.8)
                # x_click, y_click = pyautogui.center(x_pos_mob)
                # x_click_add = randint(-15,15)
                # y_click_add = randint(-15,15)
                # x_click += x_click_add
                # y_click += y_click_add
                # duree = uniform(0.06,0.1)
                # pyautogui.click(x_click,y_click,duration=duree)

                time_sleep = uniform(0.44,0.48)
                time.sleep(time_sleep)
            sell_stuffs(data["launch_dungeon_status"], data)
            rejouer_dj(1)
            #attendre si plus d'energie dans le coffre
            while (pyautogui.pixelMatchesColor(1202, 654, (100, 78, 33))):
                while (pyautogui.locateOnScreen('../img/close_energy_box.png', region=(1302, 251, 125, 120), confidence=0.95) == None):
                    time_sleep = uniform(0.36,0.39)
                    time.sleep(time_sleep)

                time_sleep = uniform(0.34,0.37)
                time.sleep(time_sleep)

                while (pyautogui.locateOnScreen('../img/close_energy_box.png', region=(1302, 251, 125, 120), confidence=0.95)):
                    x_click = randint(1332,1393)
                    y_click = randint(287,343)
                    mouse.position = (x_click, y_click)
                    duree = uniform(0.06,0.1)
                    time.sleep(duree)
                    mouse.press(Button.left)
                    mouse.release(Button.left)

                    time_sleep = uniform(0.44,0.47)
                    time.sleep(time_sleep)
                
                print("Plus d'energie meme dans le coffre, besoin de refill l'énergie\nAttente pour récupération d'énergie avant de continuer la rta...")
                time_sleep = uniform(121.0,123.0)
                time.sleep(time_sleep)

                rejouer_dj(0)

            # click sur le bouton pour fermer la fenetre combat a repet
            while (pyautogui.locateOnScreen('../img/close_window_combat_repet.png', region=(1598, 95, 164, 134), confidence=0.95) == None):
                    time_sleep = uniform(0.22,0.31)
                    time.sleep(time_sleep)

            # time_sleep = uniform(0.22,0.31)
            # time.sleep(time_sleep)

            while (pyautogui.locateOnScreen('../img/close_window_combat_repet.png', region=(1598, 95, 164, 134), confidence=0.95)):
                x_click = randint(1669,1717)
                y_click = randint(154,198)
                mouse.position = (x_click, y_click)
                duree = uniform(0.06,0.1)
                time.sleep(duree)
                mouse.press(Button.left)
                mouse.release(Button.left)

                time_sleep = uniform(0.44,0.48)
                time.sleep(time_sleep)

        if (pyautogui.locateOnScreen('../img/end_rta.png', region=(63, 919, 226, 919), confidence=0.98)):
            break
        quit = 2
        while (quit == 2):
            if (pyautogui.locateOnScreen('../img/gold_1_rta.png', region=(1316, 36, 237, 115), confidence=0.9)):
                quit = 1
            if (pyautogui.locateOnScreen('../img/silver_3_rta.png', region=(1316, 36, 237, 115), confidence=0.9)):
                quit = 0
            if (pyautogui.locateOnScreen('../img/silver_2_rta.png', region=(1316, 36, 237, 115), confidence=0.9)):
                quit = 0
            if (pyautogui.locateOnScreen('../img/silver_1_rta.png', region=(1316, 36, 237, 115), confidence=0.9)):
                quit = 0
            if (pyautogui.locateOnScreen('../img/bronze_3_rta.png', region=(1316, 36, 237, 115), confidence=0.9)):
                quit = 0
            if (pyautogui.locateOnScreen('../img/adversaire_quitte_rta.png', region=(391, 247, 1085, 563), confidence=0.9)):
                x_click = randint(826,1047)
                y_click = randint(591,681)
                duree = uniform(0.06,0.1)
                pyautogui.click(x_click,y_click,duration=duree)

            time_sleep = uniform(0.02,0.09)
            time.sleep(time_sleep)
        
        while (pyautogui.locateOnScreen('../img/combat_de_classement.png', region=(1370, 402, 410, 180), confidence=0.9)):
            x_click = randint(1402,1749)
            y_click = randint(438,550)
            duree = uniform(0.06,0.1)
            pyautogui.click(x_click,y_click,duration=duree)

            time_sleep = uniform(0.72,0.86)
            time.sleep(time_sleep)

        while (pyautogui.locateOnScreen('../img/croix_rta.png', region=(1695, 19, 130, 107), confidence=0.95) == None
               and pyautogui.locateOnScreen('../img/fin_rta.png', region=(408, 273, 1057, 523), confidence=0.95) == None):
            if (pyautogui.locateOnScreen('../img/resultats_rta.png', region=(760, 150, 1079, 211), confidence=0.85)):
                x_click = randint(1369, 1782)
                y_click = randint(80, 152)
                mouse.position = (x_click, y_click)
                duree = uniform(0.06,0.1)
                time.sleep(duree)
                mouse.press(Button.left)
                mouse.release(Button.left)

                while (pyautogui.locateOnScreen('../img/combat_de_classement.png', region=(1370, 402, 410, 180), confidence=0.9) == None):
                    time_sleep = uniform(0.02,0.09)
                    time.sleep(time_sleep)

                while (pyautogui.locateOnScreen('../img/combat_de_classement.png', region=(1370, 402, 410, 180), confidence=0.9)):
                    x_click = randint(1402,1749)
                    y_click = randint(438,550)
                    duree = uniform(0.06,0.1)
                    pyautogui.click(x_click,y_click,duration=duree)

                    time_sleep = uniform(0.72,0.86)
                    time.sleep(time_sleep)
            time_sleep = uniform(0.25,0.29)
            time.sleep(time_sleep)

        # test enlever tabulation si probleme pour les 3 lignes
        if (pyautogui.locateOnScreen('../img/fin_rta.png', region=(408, 273, 1057, 523), confidence=0.95)):
            print("plus de rta mec")

            x_click = randint(826,1051)
            y_click = randint(595,678)
            mouse.position = (x_click, y_click)
            duree = uniform(0.06,0.1)
            time.sleep(duree)
            mouse.press(Button.left)
            mouse.release(Button.left)

            continue

        # quit = 1
        if (quit == 1):
            quitter_combat_rta(data)
        
        if (quit == 0):
            # choisis les monstres
            while (pyautogui.locateOnScreen('../img/choisis_ton_monstre.png', region=(585, 33, 468, 121), confidence=0.8) == None
                   or pyautogui.pixelMatchesColor(1173, 93, (97, 77, 45)) == False):
                check_opponent_quit(data)

                time_sleep = uniform(0.02,0.09)
                time.sleep(time_sleep)

            while (pyautogui.locateOnScreen('../img/first_pick_rta.png', region=(388, 188, 391, 388), confidence=0.8) ==  None
                   and pyautogui.locateOnScreen('../img/second_pick_rta.png', region=(215, 164, 269, 446), confidence=0.8) ==  None):
                check_opponent_quit(data)
                time_sleep = uniform(0.12,0.19)
                time.sleep(time_sleep)

            if (pyautogui.locateOnScreen('../img/first_pick_rta.png', region=(388, 188, 391, 388), confidence=0.8)):
                first_pick = 1
            else:
                first_pick = 0
            
            # first pick
            while (pyautogui.pixelMatchesColor(1173, 93, (97, 77, 45)) == True):
                # time_sleep = uniform(0.02,0.09)
                # time.sleep(time_sleep)
                check_opponent_quit(data)
                if (pyautogui.locateOnScreen('../img/monster_picked.png', region=(95, 700, 446, 308), grayscale=True,confidence=0.55)):
                    quitter_combat_rta(data)
                    rta_boucle(data)
                if (first_pick == 1):
                    if (pyautogui.locateOnScreen('../img/moore_40_icon.png', region=(95, 700, 446, 308), confidence=0.95)):
                        x_pos_mob = pyautogui.locateOnScreen('../img/moore_40_icon.png', region=(95, 700, 446, 308), confidence=0.95)
                        x_click, y_click = pyautogui.center(x_pos_mob)
                        x_click_add = randint(-40,40)
                        y_click_add = randint(-40,40)
                        x_click += x_click_add
                        y_click += y_click_add
                        duree = uniform(0.06,0.1)
                        pyautogui.click(x_click,y_click,duration=duree)

                        time_sleep = uniform(0.22,0.39)
                        time.sleep(time_sleep)
                    # if symbole mob utilisé alors quitter combat (quitter_combat_rta(data))
                else:
                    if (pyautogui.locateOnScreen('../img/moore_40_icon.png', region=(95, 700, 446, 308), confidence=0.95)):
                        x_pos_mob = pyautogui.locateOnScreen('../img/moore_40_icon.png', region=(95, 700, 446, 308), confidence=0.95)
                        x_click, y_click = pyautogui.center(x_pos_mob)
                        x_click_add = randint(-40,40)
                        y_click_add = randint(-40,40)
                        x_click += x_click_add
                        y_click += y_click_add
                        duree = uniform(0.06,0.1)
                        pyautogui.click(x_click,y_click,duration=duree)

                        time_sleep = uniform(0.22,0.39)
                        time.sleep(time_sleep)


                    if (pyautogui.locateOnScreen('../img/cp_40_icon.png', region=(95, 700, 446, 308), confidence=0.95)):
                        x_pos_mob = pyautogui.locateOnScreen('../img/cp_40_icon.png', region=(95, 700, 446, 308), confidence=0.95)
                        x_click, y_click = pyautogui.center(x_pos_mob)
                        x_click_add = randint(-40,40)
                        y_click_add = randint(-40,40)
                        x_click += x_click_add
                        y_click += y_click_add
                        duree = uniform(0.06,0.1)
                        pyautogui.click(x_click,y_click,duration=duree)

                        time_sleep = uniform(0.22,0.39)
                        time.sleep(time_sleep)

            # click sur ok
            while (pyautogui.locateOnScreen('../img/choisis_ton_monstre.png', region=(585, 33, 468, 121), confidence=0.8)):
                check_opponent_quit(data)
                x_click = randint(1050,1202)
                y_click = randint(65,122)
                duree = uniform(0.06,0.1)
                pyautogui.click(x_click,y_click,duration=duree)
                time_sleep = uniform(0.22,0.31)
                time.sleep(time_sleep)

            while (pyautogui.locateOnScreen('../img/choisis_ton_monstre.png', region=(585, 33, 468, 121), confidence=0.8) == None
                   or pyautogui.pixelMatchesColor(1173, 93, (97, 77, 45)) == False):
                check_opponent_quit(data)
                time_sleep = uniform(0.02,0.09)
                time.sleep(time_sleep)

            # second pick
            while (pyautogui.pixelMatchesColor(1173, 93, (97, 77, 45)) == True):
                check_opponent_quit(data)
                if (pyautogui.locateOnScreen('../img/monster_picked.png', region=(95, 700, 446, 308), grayscale=True,confidence=0.55)):
                    quitter_combat_rta(data)
                    rta_boucle(data)
                if (first_pick == 1):
                    if (pyautogui.locateOnScreen('../img/cp_40_icon.png', region=(95, 700, 446, 308), confidence=0.95)):
                        x_pos_mob = pyautogui.locateOnScreen('../img/cp_40_icon.png', region=(95, 700, 446, 308), confidence=0.95)
                        x_click, y_click = pyautogui.center(x_pos_mob)
                        x_click_add = randint(-40,40)
                        y_click_add = randint(-40,40)
                        x_click += x_click_add
                        y_click += y_click_add
                        duree = uniform(0.06,0.1)
                        pyautogui.click(x_click,y_click,duration=duree)

                        time_sleep = uniform(0.22,0.39)
                        time.sleep(time_sleep)

                    
                    if (pyautogui.locateOnScreen('../img/bellenus_40_icon.png', region=(95, 700, 446, 308), confidence=0.95)):
                        x_pos_mob = pyautogui.locateOnScreen('../img/bellenus_40_icon.png', region=(95, 700, 446, 308), confidence=0.95)
                        x_click, y_click = pyautogui.center(x_pos_mob)
                        x_click_add = randint(-40,40)
                        y_click_add = randint(-40,40)
                        x_click += x_click_add
                        y_click += y_click_add
                        duree = uniform(0.06,0.1)
                        pyautogui.click(x_click,y_click,duration=duree)

                        time_sleep = uniform(0.22,0.39)
                        time.sleep(time_sleep)

                    # if symbole mob utilisé alors quitter combat (quitter_combat_rta(data))
                else:
                    if (pyautogui.locateOnScreen('../img/bellenus_40_icon.png', region=(95, 700, 446, 308), confidence=0.95)):
                        x_pos_mob = pyautogui.locateOnScreen('../img/bellenus_40_icon.png', region=(95, 700, 446, 308), confidence=0.95)
                        x_click, y_click = pyautogui.center(x_pos_mob)
                        x_click_add = randint(-40,40)
                        y_click_add = randint(-40,40)
                        x_click += x_click_add
                        y_click += y_click_add
                        duree = uniform(0.06,0.1)
                        pyautogui.click(x_click,y_click,duration=duree)

                        time_sleep = uniform(0.22,0.39)
                        time.sleep(time_sleep)

                    if (pyautogui.locateOnScreen('../img/maximilian_40_icon.png', region=(95, 700, 446, 308), confidence=0.95)):
                        x_pos_mob = pyautogui.locateOnScreen('../img/maximilian_40_icon.png', region=(95, 700, 446, 308), confidence=0.95)
                        x_click, y_click = pyautogui.center(x_pos_mob)
                        x_click_add = randint(-40,40)
                        y_click_add = randint(-40,40)
                        x_click += x_click_add
                        y_click += y_click_add
                        duree = uniform(0.06,0.1)
                        pyautogui.click(x_click,y_click,duration=duree)

                        time_sleep = uniform(0.22,0.39)
                        time.sleep(time_sleep)

                # # si l'adversaire a quitté
                # if (pyautogui.locateOnScreen('../img/opponent_quit.png', region=(403, 255, 1070, 551),confidence=0.9)):
                #     while (pyautogui.locateOnScreen('../img/combat_amical.png', region=(1332, 540, 476, 245), confidence=0.9) == None):
                #         x_click = randint(829,1043)
                #         y_click = randint(595,679)
                #         duree = uniform(0.06,0.1)
                #         pyautogui.click(x_click,y_click,duration=duree)
                #         time_sleep = uniform(0.52,0.59)
                #         time.sleep(time_sleep)
                #     rta_boucle(launch_dungeon_status)


            # click sur ok
            while (pyautogui.locateOnScreen('../img/choisis_ton_monstre.png', region=(585, 33, 468, 121), confidence=0.8)):
                check_opponent_quit(data)
                x_click = randint(1050,1202)
                y_click = randint(65,122)
                duree = uniform(0.06,0.1)
                pyautogui.click(x_click,y_click,duration=duree)
                time_sleep = uniform(0.12,0.26)
                time.sleep(time_sleep)

            while (pyautogui.locateOnScreen('../img/choisis_ton_monstre.png', region=(585, 33, 468, 121), confidence=0.8) == None
                    or pyautogui.pixelMatchesColor(1173, 93, (97, 77, 45)) == False):
                check_opponent_quit(data)
                time_sleep = uniform(0.02,0.09)
                time.sleep(time_sleep)

            #last pick
            while (pyautogui.pixelMatchesColor(1173, 93, (97, 77, 45)) == True):
                check_opponent_quit(data)
                if (pyautogui.locateOnScreen('../img/monster_picked.png', region=(95, 700, 446, 308), grayscale=True,confidence=0.55)):
                    quitter_combat_rta(data)
                    rta_boucle(data)
                if (first_pick == 1):
                    if (pyautogui.locateOnScreen('../img/maximilian_40_icon.png', region=(95, 700, 446, 308), confidence=0.95)):
                        x_pos_mob = pyautogui.locateOnScreen('../img/maximilian_40_icon.png', region=(95, 700, 446, 308), confidence=0.95)
                        x_click, y_click = pyautogui.center(x_pos_mob)
                        x_click_add = randint(-40,40)
                        y_click_add = randint(-40,40)
                        x_click += x_click_add
                        y_click += y_click_add
                        duree = uniform(0.06,0.1)
                        pyautogui.click(x_click,y_click,duration=duree)

                        time_sleep = uniform(0.22,0.39)
                        time.sleep(time_sleep)
                    
                    if (pyautogui.locateOnScreen('../img/woonsa_40_icon.png', region=(95, 700, 446, 308), confidence=0.95)):
                        x_pos_mob = pyautogui.locateOnScreen('../img/woonsa_40_icon.png', region=(95, 700, 446, 308), confidence=0.95)
                        x_click, y_click = pyautogui.center(x_pos_mob)
                        x_click_add = randint(-40,40)
                        y_click_add = randint(-40,40)
                        x_click += x_click_add
                        y_click += y_click_add
                        duree = uniform(0.06,0.1)
                        pyautogui.click(x_click,y_click,duration=duree)

                        time_sleep = uniform(0.22,0.39)
                        time.sleep(time_sleep)

                    # if symbole mob utilisé alors quitter combat (quitter_combat_rta(data))
                else:
                    if (pyautogui.locateOnScreen('../img/woonsa_40_icon.png', region=(95, 700, 446, 308), confidence=0.95)):
                        x_pos_mob = pyautogui.locateOnScreen('../img/woonsa_40_icon.png', region=(95, 700, 446, 308), confidence=0.95)
                        x_click, y_click = pyautogui.center(x_pos_mob)
                        x_click_add = randint(-40,40)
                        y_click_add = randint(-40,40)
                        x_click += x_click_add
                        y_click += y_click_add
                        duree = uniform(0.06,0.1)
                        pyautogui.click(x_click,y_click,duration=duree)

                        time_sleep = uniform(0.22,0.39)
                        time.sleep(time_sleep)

                    # if symbole mob utilisé alors quitter combat (quitter_combat_rta(data))

            # click sur ok
            while (pyautogui.locateOnScreen('../img/choisis_ton_monstre.png', region=(585, 33, 468, 121), confidence=0.8)):
                check_opponent_quit(data)
                x_click = randint(1050,1202)
                y_click = randint(65,122)
                duree = uniform(0.06,0.1)
                pyautogui.click(x_click,y_click,duration=duree)
                time_sleep = uniform(0.22,0.31)
                time.sleep(time_sleep)


            # bannis le monstre

            while (pyautogui.locateOnScreen('../img/bannis_monstre.png', region=(452, 23, 744, 137), confidence=0.8) == None):
                check_opponent_quit(data)
                time_sleep = uniform(0.02,0.09)
                time.sleep(time_sleep)

            x_click = randint(1326, 1346)
            y_click = randint(322, 342)

            mouse.position = (x_click, y_click)

            time_sleep = uniform(0.42,0.48)
            time.sleep(time_sleep)

            if (pyautogui.locateOnScreen('../img/lead_atq_global.png', region=(1110, 308, 427, 247), confidence=0.9)):
                pos_lead = pyautogui.locateOnScreen('../img/lead_atq_global.png', region=(1110, 308, 427, 247), confidence=0.9)
                x_click, y_click = pyautogui.center(pos_lead)

                time_sleep = uniform(1.02,1.21)
                time.sleep(time_sleep)

            if (pyautogui.locateOnScreen('../img/lead_def_global.png', region=(1110, 308, 427, 247), confidence=0.9)):
                pos_lead = pyautogui.locateOnScreen('../img/lead_def_global.png', region=(1110, 308, 427, 247), confidence=0.9)
                x_click, y_click = pyautogui.center(pos_lead)

                time_sleep = uniform(1.02,1.21)
                time.sleep(time_sleep)

            if (pyautogui.locateOnScreen('../img/lead_pv_global.png', region=(1110, 308, 427, 247), confidence=0.9)):
                pos_lead = pyautogui.locateOnScreen('../img/lead_pv_global.png', region=(1110, 308, 427, 247), confidence=0.9)
                x_click, y_click = pyautogui.center(pos_lead)

                time_sleep = uniform(1.02,1.21)
                time.sleep(time_sleep)

            if (pyautogui.locateOnScreen('../img/lead_res_global.png', region=(1110, 308, 427, 247), confidence=0.9)):
                pos_lead = pyautogui.locateOnScreen('../img/lead_res_global.png', region=(1110, 308, 427, 247), confidence=0.9)
                x_click, y_click = pyautogui.center(pos_lead)

                time_sleep = uniform(1.02,1.21)
                time.sleep(time_sleep)

            if (pyautogui.locateOnScreen('../img/lead_speed_global.png', region=(1110, 308, 427, 247), confidence=0.9)):
                pos_lead = pyautogui.locateOnScreen('../img/lead_speed_global.png', region=(1110, 308, 427, 247), confidence=0.9)
                x_click, y_click = pyautogui.center(pos_lead)

                time_sleep = uniform(1.02,1.21)
                time.sleep(time_sleep)

            if (pyautogui.locateOnScreen('../img/lead_speed_arena.png', region=(1110, 308, 427, 247), confidence=0.9)):
                pos_lead = pyautogui.locateOnScreen('../img/lead_speed_arena.png', region=(1110, 308, 427, 247), confidence=0.9)
                x_click, y_click = pyautogui.center(pos_lead)

                time_sleep = uniform(1.02,1.21)
                time.sleep(time_sleep)

            x_click_add = randint(0,40)
            y_click_add = randint(-40,0)
            x_click += x_click_add + 20
            y_click += y_click_add - 20

            mouse.position = (x_click, y_click)

            duree = uniform(0.06,0.1)
            time.sleep(duree)
            mouse.press(Button.left)
            mouse.release(Button.left)

            # time_sleep = uniform(0.37,0.41)
            # time.sleep(time_sleep)

            while (pyautogui.locateOnScreen('../img/bannis_monstre.png', region=(453, 24, 738, 140), confidence=0.95)):
                if (pyautogui.pixelMatchesColor(1311, 97, (89, 69, 41)) == False):
                    x_click = randint(1180,1330)
                    y_click = randint(66,121)
                    duree = uniform(0.06,0.1)
                    pyautogui.click(x_click,y_click,duration=duree)
                    time_sleep = uniform(0.22,0.31)
                    time.sleep(time_sleep)
                time_sleep = uniform(0.22,0.31)
                time.sleep(time_sleep)

            # choisis le lead

            # time_sleep = uniform(0.42,0.48)
            # time.sleep(time_sleep)

            if (pyautogui.locateOnScreen('../img/maximilian_40_icon2.png', region=(255, 198, 559, 371), confidence=0.9)):
                pos_lead = pyautogui.locateOnScreen('../img/maximilian_40_icon2.png', region=(255, 198, 559, 371), confidence=0.9)
                x_click, y_click = pyautogui.center(pos_lead)

                time_sleep = uniform(1.02,1.21)
                time.sleep(time_sleep)

            if (pyautogui.locateOnScreen('../img/moore_40_icon2.png', region=(255, 198, 559, 371), confidence=0.9)):
                pos_lead = pyautogui.locateOnScreen('../img/moore_40_icon2.png', region=(255, 198, 559, 371), confidence=0.9)
                x_click, y_click = pyautogui.center(pos_lead)

                time_sleep = uniform(1.02,1.21)
                time.sleep(time_sleep)

            x_click_add = randint(-40,40)
            y_click_add = randint(-40,40)
            x_click += x_click_add
            y_click += y_click_add
            mouse.position = (x_click, y_click)
            duree = uniform(0.06,0.1)
            time.sleep(duree)
            mouse.press(Button.left)
            mouse.release(Button.left)

            while (pyautogui.locateOnScreen('../img/choisis_leader.png', region=(534, 25, 575, 141), confidence=0.95)):
                if (pyautogui.pixelMatchesColor(1217, 92, (97, 77, 45)) == False):
                    x_click = randint(1097,1246)
                    y_click = randint(69,120)
                    duree = uniform(0.06,0.1)
                    pyautogui.click(x_click,y_click,duration=duree)
                    time_sleep = uniform(0.22,0.31)
                    time.sleep(time_sleep)
                time_sleep = uniform(0.22,0.31)
                time.sleep(time_sleep)

            lance_sorts_en_rta(data)

            # time_sleep = uniform(0.82,0.93)
            # time.sleep(time_sleep)
            
    print("apres boucle")

    while (pyautogui.locateOnScreen('../img/combat_amical.png', region=(1332, 540, 476, 245), confidence=0.9) == None):
        time_sleep = uniform(0.22,0.31)
        time.sleep(time_sleep)

    while (pyautogui.locateOnScreen('../img/rival.png', region=(1350, 504, 439, 220), confidence=0.9) == None):
        x_click = randint(110,425)  
        y_click = randint(84,147)
        mouse.position = (x_click, y_click)
        duree = uniform(0.06,0.1)
        time.sleep(duree)
        mouse.press(Button.left)
        mouse.release(Button.left)

        time_sleep = uniform(0.45,0.48)
        time.sleep(time_sleep)

    continue_routine(data)

def lance_sorts_en_rta_special_league_4_stars(data):
    # time_sleep = uniform(0.28,0.49)
    # time.sleep(time_sleep)
    combat_finit = 0
    while  combat_finit == 0:
        #auto draco
        if pyautogui.locateOnScreen('../img/sort1_draco.png', region=(1273, 840, 188, 188), grayscale=True, confidence=0.8) != None:
            #sort 3 draco
            if pyautogui.locateOnScreen('../img/sort3_draco.png', region=(1640, 849, 166, 177), grayscale=True, confidence=0.8) != None:
                duree = uniform(0.06,0.1)
                x_sort3 = randint(1662, 1786)
                y_sort3 = randint(877, 1002)
                pyautogui.click(x_sort3, y_sort3, duration = duree)
                while pyautogui.locateOnScreen('../img/sort3_draco.png', region=(1640, 849, 166, 177), grayscale=True, confidence=0.8) != None:
                    ou_est_la_cible_emplacement_deux_ou_quatre_allies_team()
            #sort 2 draco
            if pyautogui.locateOnScreen('../img/sort2_draco.png', region=(1462, 850, 171, 182), grayscale=True, confidence=0.8) != None:
                duree = uniform(0.06,0.1)
                x_sort2 = randint(1487, 1612)
                y_sort2 = randint(876, 1002)
                pyautogui.click(x_sort2, y_sort2, duration = duree)
                while pyautogui.locateOnScreen('../img/sort2_draco.png', region=(1462, 850, 171, 182), grayscale=True, confidence=0.8) != None:
                    ou_est_la_cible_emplacement_deux_ou_quatre_rta()
            #sort 1 draco           
            if pyautogui.locateOnScreen('../img/sort1_draco.png', region=(1273, 840, 188, 188), grayscale=True, confidence=0.8) != None:
                while pyautogui.locateOnScreen('../img/sort1_draco.png', region=(1273, 840, 188, 188), grayscale=True, confidence=0.8) != None:
                    ou_est_la_cible_emplacement_deux_ou_quatre_rta()
        #auto hongyeon
        elif pyautogui.locateOnScreen('../img/sort1_hongyeon.png', region=(1273, 840, 188, 188), grayscale=True, confidence=0.8) != None:
            #sort 3 hongyeon
            if pyautogui.locateOnScreen('../img/sort3_hongyeon.png', region=(1640, 849, 166, 177), grayscale=True, confidence=0.8) != None:
                duree = uniform(0.06,0.1)
                x_sort3 = randint(1662, 1786)
                y_sort3 = randint(877, 1002)
                pyautogui.click(x_sort3, y_sort3, duration = duree)
                while pyautogui.locateOnScreen('../img/sort3_hongyeon.png', region=(1640, 849, 166, 177), grayscale=True, confidence=0.8) != None:
                    ou_est_la_cible_emplacement_deux_ou_quatre_allies_team()
            #sort 2 hongyeon
            if pyautogui.locateOnScreen('../img/sort2_hongyeon.png', region=(1462, 850, 171, 182), grayscale=True, confidence=0.8) != None:
                duree = uniform(0.06,0.1)
                x_sort2 = randint(1487, 1612)
                y_sort2 = randint(876, 1002)
                pyautogui.click(x_sort2, y_sort2, duration = duree)
                while pyautogui.locateOnScreen('../img/sort2_hongyeon.png', region=(1462, 850, 171, 182), grayscale=True, confidence=0.8) != None:
                    ou_est_la_cible_emplacement_deux_ou_quatre_allies_team()
            #sort 1 hongyeon           
            if pyautogui.locateOnScreen('../img/sort1_hongyeon.png', region=(1273, 840, 188, 188), grayscale=True, confidence=0.8) != None:
                while pyautogui.locateOnScreen('../img/sort1_hongyeon.png', region=(1273, 840, 188, 188), grayscale=True, confidence=0.8) != None:
                    ou_est_la_cible_emplacement_deux_ou_quatre_rta()

        #auto gemini
        elif pyautogui.locateOnScreen('../img/sort1_gemini.png', region=(1273, 840, 188, 188), grayscale=True, confidence=0.8) != None:
            #sort 2 gemini
            if pyautogui.locateOnScreen('../img/sort2_gemini.png', region=(1462, 850, 171, 182), grayscale=True, confidence=0.8) != None:
                duree = uniform(0.06,0.1)
                x_sort2 = randint(1487, 1612)
                y_sort2 = randint(876, 1002)
                pyautogui.click(x_sort2, y_sort2, duration = duree)
                while pyautogui.locateOnScreen('../img/sort2_gemini.png', region=(1462, 850, 171, 182), grayscale=True, confidence=0.8) != None:
                    ou_est_la_cible_emplacement_deux_ou_quatre_rta()
            #sort 1 gemini           
            if pyautogui.locateOnScreen('../img/sort1_gemini.png', region=(1273, 840, 188, 188), grayscale=True, confidence=0.8) != None:
                while pyautogui.locateOnScreen('../img/sort1_gemini.png', region=(1273, 840, 188, 188), grayscale=True, confidence=0.8) != None:
                    ou_est_la_cible_emplacement_deux_ou_quatre_rta()

        # auto shimitae
        elif pyautogui.locateOnScreen('../img/sort1_shimitae.png', region=(1273, 840, 188, 188), grayscale=True, confidence=0.9) != None:
            #sort 2 shimitae
            if pyautogui.locateOnScreen('../img/sort2_shimitae.png', region=(1462, 850, 171, 182), grayscale=True, confidence=0.8) != None:
                duree = uniform(0.06,0.1)
                x_sort2 = randint(1487, 1612)
                y_sort2 = randint(876, 1002)
                pyautogui.click(x_sort2, y_sort2, duration = duree)
                while pyautogui.locateOnScreen('../img/sort2_shimitae.png', region=(1462, 850, 171, 182), grayscale=True, confidence=0.8) != None:
                    ou_est_la_cible_emplacement_deux_ou_quatre_rta()
            #sort 3 shimitae
            if pyautogui.locateOnScreen('../img/sort3_shimitae.png', region=(1640, 849, 166, 177), grayscale=True, confidence=0.8) != None:
                duree = uniform(0.06,0.1)
                x_sort3 = randint(1662, 1786)
                y_sort3 = randint(877, 1002)
                pyautogui.click(x_sort3, y_sort3, duration = duree)
                while pyautogui.locateOnScreen('../img/sort3_shimitae.png', region=(1640, 849, 166, 177), grayscale=True, confidence=0.8) != None:
                    ou_est_la_cible_emplacement_deux_ou_quatre_rta()
            #sort 1 shimitae           
            if pyautogui.locateOnScreen('../img/sort1_shimitae.png', region=(1273, 840, 188, 188), grayscale=True, confidence=0.8) != None:
                while pyautogui.locateOnScreen('../img/sort1_shimitae.png', region=(1273, 840, 188, 188), grayscale=True, confidence=0.8) != None:
                    ou_est_la_cible_emplacement_deux_ou_quatre_rta()


        # auto julie
        elif pyautogui.locateOnScreen('../img/sort1_julie.png', region=(1273, 840, 188, 188), grayscale=True, confidence=0.8) != None:
            #sort 3 julie
            if pyautogui.locateOnScreen('../img/sort3_julie.png', region=(1640, 849, 166, 177), grayscale=True, confidence=0.5) != None:
                duree = uniform(0.06,0.1)
                x_sort3 = randint(1662, 1786)
                y_sort3 = randint(877, 1002)
                pyautogui.click(x_sort3, y_sort3, duration = duree)
                while pyautogui.locateOnScreen('../img/sort3_julie.png', region=(1640, 849, 166, 177), grayscale=True, confidence=0.5) != None:
                    ou_est_la_cible_emplacement_deux_ou_quatre_rta()
            #sort 2 julie
            if pyautogui.locateOnScreen('../img/sort2_julie.png', region=(1462, 850, 171, 182), grayscale=True, confidence=0.8) != None:
                duree = uniform(0.06,0.1)
                x_sort2 = randint(1487, 1612)
                y_sort2 = randint(876, 1002)
                pyautogui.click(x_sort2, y_sort2, duration = duree)
                while pyautogui.locateOnScreen('../img/sort2_julie.png', region=(1462, 850, 171, 182), grayscale=True, confidence=0.8) != None:
                    ou_est_la_cible_emplacement_deux_ou_quatre_rta()
            #sort 1 julie           
            if pyautogui.locateOnScreen('../img/sort1_julie.png', region=(1273, 840, 188, 188), grayscale=True, confidence=0.8) != None:
                while pyautogui.locateOnScreen('../img/sort1_julie.png', region=(1273, 840, 188, 188), grayscale=True, confidence=0.8) != None:
                    ou_est_la_cible_emplacement_deux_ou_quatre_rta()
            
        elif pyautogui.locateOnScreen('../img/victory_rta.png', region=(556, 110, 734, 177), confidence=0.85) != None:
            while (pyautogui.locateOnScreen('../img/victory_rta.png', region=(556, 110, 734, 177), confidence=0.85)):
                x_click = randint(314,1374)
                y_click = randint(386,840)
                duree = uniform(0.06,0.1)
                pyautogui.click(x_click,y_click,duration=duree)
                time_sleep = uniform(0.28,0.49)
                time.sleep(time_sleep)
            combat_finit = 1
            
        elif pyautogui.locateOnScreen('../img/defeated_rta.png', region = (605, 106, 641, 200), confidence = 0.52) != None:
            while (pyautogui.locateOnScreen('../img/defeated_rta.png', region=(605, 106, 641, 200), confidence = 0.52)):
                x_click = randint(314,1374)
                y_click = randint(386,840)
                duree = uniform(0.06,0.1)
                pyautogui.click(x_click,y_click,duration=duree)
                time_sleep = uniform(0.28,0.49)
                time.sleep(time_sleep)
            combat_finit = 1
        check_opponent_quit(data)

def quitter_combat_rta(data):
    while (pyautogui.locateOnScreen('../img/croix_rta.png', region=(1695, 19, 130, 107), confidence=0.95) == None):
        check_opponent_quit(data)

        # if (pyautogui.locateOnScreen('../img/resultats_rta.png', region=(760, 150, 1079, 211), confidence=0.85)):
        #     x_click = randint(1369, 1782)
        #     y_click = randint(80, 152)
        #     mouse.position = (x_click, y_click)
        #     duree = uniform(0.06,0.1)
        #     time.sleep(duree)
        #     mouse.press(Button.left)
        #     mouse.release(Button.left)

        #     while (pyautogui.locateOnScreen('../img/combat_de_classement.png', region=(1370, 402, 410, 180), confidence=0.9) == None):
        #         time_sleep = uniform(0.02,0.09)
        #         time.sleep(time_sleep)

        #     while (pyautogui.locateOnScreen('../img/combat_de_classement.png', region=(1370, 402, 410, 180), confidence=0.9)):
        #         x_click = randint(1402,1749)
        #         y_click = randint(438,550)
        #         duree = uniform(0.06,0.1)
        #         pyautogui.click(x_click,y_click,duration=duree)

        #         time_sleep = uniform(0.72,0.86)
        #         time.sleep(time_sleep)
        time_sleep = uniform(0.02,0.09)
        time.sleep(time_sleep)

    x_click = randint(1742,1786)
    y_click = randint(60,99)
    duree = uniform(0.06,0.1)
    pyautogui.click(x_click,y_click,duration=duree)

    while (pyautogui.locateOnScreen('../img/oui_quit_rta.png', region=(642, 619, 290, 150), confidence=0.95) == None):
        check_opponent_quit(data)
        time_sleep = uniform(0.02,0.09)
        time.sleep(time_sleep)

    while (pyautogui.locateOnScreen('../img/oui_quit_rta.png', region=(642, 619, 290, 150), confidence=0.95)):
        check_opponent_quit(data)
        x_click = randint(673,891)
        y_click = randint(650,739)
        duree = uniform(0.06,0.1)
        pyautogui.click(x_click,y_click,duration=duree)

        time_sleep = uniform(0.42,0.46)
        time.sleep(time_sleep)

def check_opponent_quit_SL(data):
    if (pyautogui.locateOnScreen('../img/opponent_quit.png', region=(403, 255, 1070, 551),confidence=0.9)):
        while (pyautogui.locateOnScreen('../img/commencer_rta.png', region=(1211, 789, 426, 194), confidence=0.9) == None):
            x_click = randint(829,1043)
            y_click = randint(595,679)
            duree = uniform(0.06,0.1)
            pyautogui.click(x_click,y_click,duration=duree)

            time_sleep = uniform(0.42,0.47)
            time.sleep(time_sleep)
        rta_boucle_special_league_4(data)

def rta_boucle_special_league_4(data):
    # Check si l'adversaire quitte le combat pendant la draft ou si l'un des 5 monstres est pris en fasse et quitter
    # nb_combat_rta = 25
    # cmp = 0

    while (pyautogui.locateOnScreen('../img/commencer_rta.png', region=(1211, 789, 426, 194), confidence=0.8) == None):
        x_click = randint(882,991)
        y_click = randint(229,298)
        duree = uniform(0.06,0.1)
        pyautogui.click(x_click,y_click,duration=duree)

        time_sleep = uniform(0.45,0.49)
        time.sleep(time_sleep)

    while (1):
        while (pyautogui.locateOnScreen('../img/commencer_rta.png', region=(1211, 789, 426, 194), confidence=0.9) == None):
            check_opponent_quit_SL(data)
            time_sleep = uniform(0.25,0.29)
            time.sleep(time_sleep)

        if (pyautogui.locateOnScreen('../img/waiting_for_repet_battle2.png', region=(62, 97, 127, 356), confidence=0.8)):
            x_click = randint(1600,1656)
            y_click = randint(70,124)
            duree = uniform(0.06,0.1)
            pyautogui.click(x_click,y_click,duration=duree)
            while (pyautogui.locateOnScreen('../img/combat_a_repet.jpg', region=(105, 92, 638, 170), confidence=0.8) == None):
                x_click = randint(103,140)
                y_click = randint(312,342)
                duree = uniform(0.06,0.1)
                pyautogui.click(x_click,y_click,duration=duree)
                # x_pos_mob = pyautogui.locateOnScreen('../img/waiting_for_repet_battle2.png', region=(62, 97, 127, 356), confidence=0.8)
                # x_click, y_click = pyautogui.center(x_pos_mob)
                # x_click_add = randint(-15,15)
                # y_click_add = randint(-15,15)
                # x_click += x_click_add
                # y_click += y_click_add
                # duree = uniform(0.06,0.1)
                # pyautogui.click(x_click,y_click,duration=duree)

                time_sleep = uniform(0.44,0.48)
                time.sleep(time_sleep)
            sell_stuffs(data["launch_dungeon_status"], data)
            rejouer_dj(1)
            #attendre si plus d'energie dans le coffre
            while (pyautogui.pixelMatchesColor(1202, 654, (100, 78, 33))):
                while (pyautogui.locateOnScreen('../img/close_energy_box.png', region=(1302, 251, 125, 120), confidence=0.95) == None):
                    time_sleep = uniform(0.36,0.39)
                    time.sleep(time_sleep)

                time_sleep = uniform(0.34,0.37)
                time.sleep(time_sleep)

                while (pyautogui.locateOnScreen('../img/close_energy_box.png', region=(1302, 251, 125, 120), confidence=0.95)):
                    x_click = randint(1332,1393)
                    y_click = randint(287,343)
                    mouse.position = (x_click, y_click)
                    duree = uniform(0.06,0.1)
                    time.sleep(duree)
                    mouse.press(Button.left)
                    mouse.release(Button.left)

                    time_sleep = uniform(0.44,0.47)
                    time.sleep(time_sleep)
                
                print("Plus d'energie meme dans le coffre, besoin de refill l'énergie\nAttente pour récupération d'énergie avant de continuer la rta...")
                time_sleep = uniform(121.0,123.0)
                time.sleep(time_sleep)

                rejouer_dj(0)

            # click sur le bouton pour fermer la fenetre combat a repet
            while (pyautogui.locateOnScreen('../img/close_window_combat_repet.png', region=(1598, 95, 164, 134), confidence=0.95) == None):
                    time_sleep = uniform(0.22,0.31)
                    time.sleep(time_sleep)

            # time_sleep = uniform(0.22,0.31)
            # time.sleep(time_sleep)

            while (pyautogui.locateOnScreen('../img/close_window_combat_repet.png', region=(1598, 95, 164, 134), confidence=0.95)):
                x_click = randint(1669,1717)
                y_click = randint(154,198)
                mouse.position = (x_click, y_click)
                duree = uniform(0.06,0.1)
                time.sleep(duree)
                mouse.press(Button.left)
                mouse.release(Button.left)

                time_sleep = uniform(0.44,0.48)
                time.sleep(time_sleep)

            while (pyautogui.locateOnScreen('../img/commencer_rta.png', region=(1211, 789, 426, 194), confidence=0.8) == None):
                x_click = randint(882,991)
                y_click = randint(229,298)
                duree = uniform(0.06,0.1)
                pyautogui.click(x_click,y_click,duration=duree)

                time_sleep = uniform(0.45,0.49)
                time.sleep(time_sleep)

        if (pyautogui.locateOnScreen('../img/end_rta_SP_4.png', region=(1364, 349, 270, 112), confidence=0.98)):
            x_click = randint(1600,1656)
            y_click = randint(70,124)
            duree = uniform(0.06,0.1)
            pyautogui.click(x_click,y_click,duration=duree)
            break
        quit = 2
        while (quit == 2):
            # if (pyautogui.locateOnScreen('../img/silver_3_rta.png', region=(534, 282, 282, 130), confidence=0.9)):
            #     quit = 1
            if (pyautogui.locateOnScreen('../img/silver_2_rta_SP_4.png', region=(534, 282, 282, 130), confidence=0.9)):
                quit = 0
            if (pyautogui.locateOnScreen('../img/silver_1_rta_SP_4.jpg', region=(534, 282, 282, 130), confidence=0.9)):
                quit = 0
            if (pyautogui.locateOnScreen('../img/bronze_3_rta_SP_4.png', region=(534, 282, 282, 130), confidence=0.9)):
                quit = 0
            if (pyautogui.locateOnScreen('../img/bronze_2_rta_SP_4.png', region=(534, 282, 282, 130), confidence=0.9)):
                quit = 0
            if (pyautogui.locateOnScreen('../img/adversaire_quitte_rta.png', region=(391, 247, 1085, 563), confidence=0.95)):
                x_click = randint(826,1047)
                y_click = randint(591,681)
                duree = uniform(0.06,0.1)
                pyautogui.click(x_click,y_click,duration=duree)
            time_sleep = uniform(0.02,0.09)
            time.sleep(time_sleep)

        while (pyautogui.locateOnScreen('../img/commencer_rta.png', region=(1211, 789, 426, 194), confidence=0.9)
               and pyautogui.locateOnScreen('../img/fin_rta_SP_4.png', region=(414, 263, 990, 270), confidence=0.95) == None):
            x_click = randint(1252,1593)
            y_click = randint(839,935)
            duree = uniform(0.06,0.1)
            pyautogui.click(x_click,y_click,duration=duree)

            time_sleep = uniform(0.72,0.86)
            time.sleep(time_sleep)

        if (pyautogui.locateOnScreen('../img/fin_rta_SP_4.png', region=(414, 263, 990, 270), confidence=0.95)):
            print("plus de rta mec")

            x_click = randint(830,1048)
            y_click = randint(597,677)
            mouse.position = (x_click, y_click)
            duree = uniform(0.06,0.1)
            time.sleep(duree)
            mouse.press(Button.left)
            mouse.release(Button.left)

            continue

        while (pyautogui.locateOnScreen('../img/croix_rta.png', region=(1695, 19, 130, 107), confidence=0.95) == None
               and pyautogui.locateOnScreen('../img/fin_rta.png', region=(408, 273, 1057, 523), confidence=0.95) == None):
            time_sleep = uniform(0.25,0.29)
            time.sleep(time_sleep)


        # quit = 1
        if (quit == 1):
            quitter_combat_rta(data)
        
        if (quit == 0):
            # choisis les monstres
            while (pyautogui.locateOnScreen('../img/choisis_ton_monstre.png', region=(585, 33, 468, 121), confidence=0.8) == None
                   or pyautogui.pixelMatchesColor(1173, 93, (97, 77, 45)) == False):
                check_opponent_quit_SL(data)
                time_sleep = uniform(0.02,0.09)
                time.sleep(time_sleep)

            while (pyautogui.locateOnScreen('../img/first_pick_rta.png', region=(388, 188, 391, 388), confidence=0.8) ==  None
                   and pyautogui.locateOnScreen('../img/second_pick_rta.png', region=(215, 164, 269, 446), confidence=0.8) ==  None):
                check_opponent_quit_SL(data)
                time_sleep = uniform(0.12,0.19)
                time.sleep(time_sleep)

            if (pyautogui.locateOnScreen('../img/first_pick_rta.png', region=(388, 188, 391, 388), confidence=0.8)):
                first_pick = 1
            else:
                first_pick = 0
            
            # first pick
            while (pyautogui.pixelMatchesColor(1173, 93, (97, 77, 45)) == True):
                # time_sleep = uniform(0.02,0.09)
                # time.sleep(time_sleep)
                check_opponent_quit_SL(data)
                if (pyautogui.locateOnScreen('../img/monster_picked.png', region=(95, 700, 446, 308), grayscale=True,confidence=0.55)):
                    quitter_combat_rta(data)
                    rta_boucle_special_league_4(data)
                if (first_pick == 1):
                    if (pyautogui.locateOnScreen('../img/draco_35_icon.png', region=(95, 700, 446, 308), confidence=0.95)):
                        x_pos_mob = pyautogui.locateOnScreen('../img/draco_35_icon.png', region=(95, 700, 446, 308), confidence=0.95)
                        x_click, y_click = pyautogui.center(x_pos_mob)
                        x_click_add = randint(-40,40)
                        y_click_add = randint(-40,40)
                        x_click += x_click_add
                        y_click += y_click_add
                        duree = uniform(0.06,0.1)
                        pyautogui.click(x_click,y_click,duration=duree)

                        time_sleep = uniform(0.22,0.39)
                        time.sleep(time_sleep)
                    # if symbole mob utilisé alors quitter combat (quitter_combat_rta(data))
                else:
                    if (pyautogui.locateOnScreen('../img/draco_35_icon.png', region=(95, 700, 446, 308), confidence=0.95)):
                        x_pos_mob = pyautogui.locateOnScreen('../img/draco_35_icon.png', region=(95, 700, 446, 308), confidence=0.95)
                        x_click, y_click = pyautogui.center(x_pos_mob)
                        x_click_add = randint(-40,40)
                        y_click_add = randint(-40,40)
                        x_click += x_click_add
                        y_click += y_click_add
                        duree = uniform(0.06,0.1)
                        pyautogui.click(x_click,y_click,duration=duree)

                        time_sleep = uniform(0.22,0.39)
                        time.sleep(time_sleep)


                    if (pyautogui.locateOnScreen('../img/shimitae_40_icon.png', region=(95, 700, 446, 308), confidence=0.95)):
                        x_pos_mob = pyautogui.locateOnScreen('../img/shimitae_40_icon.png', region=(95, 700, 446, 308), confidence=0.95)
                        x_click, y_click = pyautogui.center(x_pos_mob)
                        x_click_add = randint(-40,40)
                        y_click_add = randint(-40,40)
                        x_click += x_click_add
                        y_click += y_click_add
                        duree = uniform(0.06,0.1)
                        pyautogui.click(x_click,y_click,duration=duree)

                        time_sleep = uniform(0.22,0.39)
                        time.sleep(time_sleep)

            # click sur ok
            while (pyautogui.locateOnScreen('../img/choisis_ton_monstre.png', region=(585, 33, 468, 121), confidence=0.8)):
                check_opponent_quit_SL(data)
                x_click = randint(1050,1202)
                y_click = randint(65,122)
                duree = uniform(0.06,0.1)
                pyautogui.click(x_click,y_click,duration=duree)
                time_sleep = uniform(0.22,0.31)
                time.sleep(time_sleep)

            while (pyautogui.locateOnScreen('../img/choisis_ton_monstre.png', region=(585, 33, 468, 121), confidence=0.8) == None
                   or pyautogui.pixelMatchesColor(1173, 93, (97, 77, 45)) == False):
                check_opponent_quit_SL(data)
                time_sleep = uniform(0.02,0.09)
                time.sleep(time_sleep)

            # second pick
            while (pyautogui.pixelMatchesColor(1173, 93, (97, 77, 45)) == True):
                check_opponent_quit_SL(data)
                if (pyautogui.locateOnScreen('../img/monster_picked.png', region=(95, 700, 446, 308), grayscale=True,confidence=0.55)):
                    quitter_combat_rta(data)
                    rta_boucle_special_league_4(data)
                if (first_pick == 1):
                    if (pyautogui.locateOnScreen('../img/shimitae_40_icon.png', region=(95, 700, 446, 308), confidence=0.95)):
                        x_pos_mob = pyautogui.locateOnScreen('../img/shimitae_40_icon.png', region=(95, 700, 446, 308), confidence=0.95)
                        x_click, y_click = pyautogui.center(x_pos_mob)
                        x_click_add = randint(-40,40)
                        y_click_add = randint(-40,40)
                        x_click += x_click_add
                        y_click += y_click_add
                        duree = uniform(0.06,0.1)
                        pyautogui.click(x_click,y_click,duration=duree)

                        time_sleep = uniform(0.22,0.39)
                        time.sleep(time_sleep)

                    
                    if (pyautogui.locateOnScreen('../img/gemini_35_icon.png', region=(95, 700, 446, 308), confidence=0.95)):
                        x_pos_mob = pyautogui.locateOnScreen('../img/gemini_35_icon.png', region=(95, 700, 446, 308), confidence=0.95)
                        x_click, y_click = pyautogui.center(x_pos_mob)
                        x_click_add = randint(-40,40)
                        y_click_add = randint(-40,40)
                        x_click += x_click_add
                        y_click += y_click_add
                        duree = uniform(0.06,0.1)
                        pyautogui.click(x_click,y_click,duration=duree)

                        time_sleep = uniform(0.22,0.39)
                        time.sleep(time_sleep)

                    # if symbole mob utilisé alors quitter combat (quitter_combat_rta(data))
                else:
                    if (pyautogui.locateOnScreen('../img/gemini_35_icon.png', region=(95, 700, 446, 308), confidence=0.95)):
                        x_pos_mob = pyautogui.locateOnScreen('../img/gemini_35_icon.png', region=(95, 700, 446, 308), confidence=0.95)
                        x_click, y_click = pyautogui.center(x_pos_mob)
                        x_click_add = randint(-40,40)
                        y_click_add = randint(-40,40)
                        x_click += x_click_add
                        y_click += y_click_add
                        duree = uniform(0.06,0.1)
                        pyautogui.click(x_click,y_click,duration=duree)

                        time_sleep = uniform(0.22,0.39)
                        time.sleep(time_sleep)

                    if (pyautogui.locateOnScreen('../img/julie_40_icon.png', region=(95, 700, 446, 308), confidence=0.95)):
                        x_pos_mob = pyautogui.locateOnScreen('../img/julie_40_icon.png', region=(95, 700, 446, 308), confidence=0.95)
                        x_click, y_click = pyautogui.center(x_pos_mob)
                        x_click_add = randint(-40,40)
                        y_click_add = randint(-40,40)
                        x_click += x_click_add
                        y_click += y_click_add
                        duree = uniform(0.06,0.1)
                        pyautogui.click(x_click,y_click,duration=duree)

                        time_sleep = uniform(0.22,0.39)
                        time.sleep(time_sleep)

                # # si l'adversaire a quitté
                # if (pyautogui.locateOnScreen('../img/opponent_quit.png', region=(403, 255, 1070, 551),confidence=0.9)):
                #     while (pyautogui.locateOnScreen('../img/combat_amical.png', region=(1332, 540, 476, 245), confidence=0.9) == None):
                #         x_click = randint(829,1043)
                #         y_click = randint(595,679)
                #         duree = uniform(0.06,0.1)
                #         pyautogui.click(x_click,y_click,duration=duree)
                #         time_sleep = uniform(0.52,0.59)
                #         time.sleep(time_sleep)
                #     rta_boucle_special_league_4(launch_dungeon_status)


            # click sur ok
            while (pyautogui.locateOnScreen('../img/choisis_ton_monstre.png', region=(585, 33, 468, 121), confidence=0.8)):
                check_opponent_quit_SL(data)
                x_click = randint(1050,1202)
                y_click = randint(65,122)
                duree = uniform(0.06,0.1)
                pyautogui.click(x_click,y_click,duration=duree)
                time_sleep = uniform(0.12,0.26)
                time.sleep(time_sleep)

            while (pyautogui.locateOnScreen('../img/choisis_ton_monstre.png', region=(585, 33, 468, 121), confidence=0.8) == None
                    or pyautogui.pixelMatchesColor(1173, 93, (97, 77, 45)) == False):
                check_opponent_quit_SL(data)
                time_sleep = uniform(0.02,0.09)
                time.sleep(time_sleep)

            #last pick
            while (pyautogui.pixelMatchesColor(1173, 93, (97, 77, 45)) == True):
                check_opponent_quit_SL(data)
                if (pyautogui.locateOnScreen('../img/monster_picked.png', region=(95, 700, 446, 308), grayscale=True,confidence=0.55)):
                    quitter_combat_rta(data)
                    rta_boucle_special_league_4(data)
                if (first_pick == 1):
                    if (pyautogui.locateOnScreen('../img/julie_40_icon.png', region=(95, 700, 446, 308), confidence=0.95)):
                        x_pos_mob = pyautogui.locateOnScreen('../img/julie_40_icon.png', region=(95, 700, 446, 308), confidence=0.95)
                        x_click, y_click = pyautogui.center(x_pos_mob)
                        x_click_add = randint(-40,40)
                        y_click_add = randint(-40,40)
                        x_click += x_click_add
                        y_click += y_click_add
                        duree = uniform(0.06,0.1)
                        pyautogui.click(x_click,y_click,duration=duree)

                        time_sleep = uniform(0.22,0.39)
                        time.sleep(time_sleep)
                    
                    if (pyautogui.locateOnScreen('../img/hongyeon_35_icon.png', region=(95, 700, 446, 308), confidence=0.95)):
                        x_pos_mob = pyautogui.locateOnScreen('../img/hongyeon_35_icon.png', region=(95, 700, 446, 308), confidence=0.95)
                        x_click, y_click = pyautogui.center(x_pos_mob)
                        x_click_add = randint(-40,40)
                        y_click_add = randint(-40,40)
                        x_click += x_click_add
                        y_click += y_click_add
                        duree = uniform(0.06,0.1)
                        pyautogui.click(x_click,y_click,duration=duree)

                        time_sleep = uniform(0.22,0.39)
                        time.sleep(time_sleep)

                    # if symbole mob utilisé alors quitter combat (quitter_combat_rta(data))
                else:
                    if (pyautogui.locateOnScreen('../img/hongyeon_35_icon.png', region=(95, 700, 446, 308), confidence=0.95)):
                        x_pos_mob = pyautogui.locateOnScreen('../img/hongyeon_35_icon.png', region=(95, 700, 446, 308), confidence=0.95)
                        x_click, y_click = pyautogui.center(x_pos_mob)
                        x_click_add = randint(-40,40)
                        y_click_add = randint(-40,40)
                        x_click += x_click_add
                        y_click += y_click_add
                        duree = uniform(0.06,0.1)
                        pyautogui.click(x_click,y_click,duration=duree)

                        time_sleep = uniform(0.22,0.39)
                        time.sleep(time_sleep)

                    # if symbole mob utilisé alors quitter combat (quitter_combat_rta(data))

            # click sur ok
            while (pyautogui.locateOnScreen('../img/choisis_ton_monstre.png', region=(585, 33, 468, 121), confidence=0.8)):
                check_opponent_quit_SL(data)
                x_click = randint(1050,1202)
                y_click = randint(65,122)
                duree = uniform(0.06,0.1)
                pyautogui.click(x_click,y_click,duration=duree)
                time_sleep = uniform(0.22,0.31)
                time.sleep(time_sleep)


            # bannis le monstre

            while (pyautogui.locateOnScreen('../img/bannis_monstre.png', region=(452, 23, 744, 137), confidence=0.8) == None):
                check_opponent_quit_SL(data)
                time_sleep = uniform(0.02,0.09)
                time.sleep(time_sleep)

            x_click = randint(1326, 1346)
            y_click = randint(322, 342)

            mouse.position = (x_click, y_click)

            time_sleep = uniform(0.42,0.48)
            time.sleep(time_sleep)

            if (pyautogui.locateOnScreen('../img/lead_atq_global.png', region=(1110, 308, 427, 247), confidence=0.9)):
                pos_lead = pyautogui.locateOnScreen('../img/lead_atq_global.png', region=(1110, 308, 427, 247), confidence=0.9)
                x_click, y_click = pyautogui.center(pos_lead)

                time_sleep = uniform(1.02,1.21)
                time.sleep(time_sleep)

            if (pyautogui.locateOnScreen('../img/lead_def_global.png', region=(1110, 308, 427, 247), confidence=0.9)):
                pos_lead = pyautogui.locateOnScreen('../img/lead_def_global.png', region=(1110, 308, 427, 247), confidence=0.9)
                x_click, y_click = pyautogui.center(pos_lead)

                time_sleep = uniform(1.02,1.21)
                time.sleep(time_sleep)

            if (pyautogui.locateOnScreen('../img/lead_pv_global.png', region=(1110, 308, 427, 247), confidence=0.9)):
                pos_lead = pyautogui.locateOnScreen('../img/lead_pv_global.png', region=(1110, 308, 427, 247), confidence=0.9)
                x_click, y_click = pyautogui.center(pos_lead)

                time_sleep = uniform(1.02,1.21)
                time.sleep(time_sleep)

            if (pyautogui.locateOnScreen('../img/lead_res_global.png', region=(1110, 308, 427, 247), confidence=0.9)):
                pos_lead = pyautogui.locateOnScreen('../img/lead_res_global.png', region=(1110, 308, 427, 247), confidence=0.9)
                x_click, y_click = pyautogui.center(pos_lead)

                time_sleep = uniform(1.02,1.21)
                time.sleep(time_sleep)

            if (pyautogui.locateOnScreen('../img/lead_speed_global.png', region=(1110, 308, 427, 247), confidence=0.9)):
                pos_lead = pyautogui.locateOnScreen('../img/lead_speed_global.png', region=(1110, 308, 427, 247), confidence=0.9)
                x_click, y_click = pyautogui.center(pos_lead)

                time_sleep = uniform(1.02,1.21)
                time.sleep(time_sleep)

            if (pyautogui.locateOnScreen('../img/lead_speed_arena.png', region=(1110, 308, 427, 247), confidence=0.9)):
                pos_lead = pyautogui.locateOnScreen('../img/lead_speed_arena.png', region=(1110, 308, 427, 247), confidence=0.9)
                x_click, y_click = pyautogui.center(pos_lead)

                time_sleep = uniform(1.02,1.21)
                time.sleep(time_sleep)

            x_click_add = randint(0,40)
            y_click_add = randint(-40,0)
            x_click += x_click_add + 20
            y_click += y_click_add - 20

            mouse.position = (x_click, y_click)

            duree = uniform(0.06,0.1)
            time.sleep(duree)
            mouse.press(Button.left)
            mouse.release(Button.left)

            # time_sleep = uniform(0.37,0.41)
            # time.sleep(time_sleep)

            while (pyautogui.locateOnScreen('../img/bannis_monstre.png', region=(453, 24, 738, 140), confidence=0.95)):
                if (pyautogui.pixelMatchesColor(1311, 97, (89, 69, 41)) == False):
                    x_click = randint(1180,1330)
                    y_click = randint(66,121)
                    duree = uniform(0.06,0.1)
                    pyautogui.click(x_click,y_click,duration=duree)
                    time_sleep = uniform(0.22,0.31)
                    time.sleep(time_sleep)
                time_sleep = uniform(0.22,0.31)
                time.sleep(time_sleep)

            # choisis le lead

            # time_sleep = uniform(0.42,0.48)
            # time.sleep(time_sleep)

            if (pyautogui.locateOnScreen('../img/gemini_35_icon2.png', region=(255, 198, 559, 371), confidence=0.9)):
                pos_lead = pyautogui.locateOnScreen('../img/gemini_35_icon2.png', region=(255, 198, 559, 371), confidence=0.9)
                x_click, y_click = pyautogui.center(pos_lead)

                time_sleep = uniform(1.02,1.21)
                time.sleep(time_sleep)

            if (pyautogui.locateOnScreen('../img/shimitae_40_icon2.png', region=(255, 198, 559, 371), confidence=0.9)):
                pos_lead = pyautogui.locateOnScreen('../img/shimitae_40_icon2.png', region=(255, 198, 559, 371), confidence=0.9)
                x_click, y_click = pyautogui.center(pos_lead)

                time_sleep = uniform(1.02,1.21)
                time.sleep(time_sleep)

            x_click_add = randint(-40,40)
            y_click_add = randint(-40,40)
            x_click += x_click_add
            y_click += y_click_add
            mouse.position = (x_click, y_click)
            duree = uniform(0.06,0.1)
            time.sleep(duree)
            mouse.press(Button.left)
            mouse.release(Button.left)

            while (pyautogui.locateOnScreen('../img/choisis_leader.png', region=(534, 25, 575, 141), confidence=0.95)):
                if (pyautogui.pixelMatchesColor(1217, 92, (97, 77, 45)) == False):
                    x_click = randint(1097,1246)
                    y_click = randint(69,120)
                    duree = uniform(0.06,0.1)
                    pyautogui.click(x_click,y_click,duration=duree)
                    time_sleep = uniform(0.22,0.31)
                    time.sleep(time_sleep)
                time_sleep = uniform(0.22,0.31)
                time.sleep(time_sleep)

            lance_sorts_en_rta_special_league_4_stars(data)

            # time_sleep = uniform(0.82,0.93)
            # time.sleep(time_sleep)
            
    print("apres boucle")

    while (pyautogui.locateOnScreen('../img/combat_amical.png', region=(1332, 540, 476, 245), confidence=0.9) == None):
        time_sleep = uniform(0.22,0.31)
        time.sleep(time_sleep)

    while (pyautogui.locateOnScreen('../img/rival.png', region=(1350, 504, 439, 220), confidence=0.9) == None):
        x_click = randint(110,425)  
        y_click = randint(84,147)
        mouse.position = (x_click, y_click)
        duree = uniform(0.06,0.1)
        time.sleep(duree)
        mouse.press(Button.left)
        mouse.release(Button.left)

        time_sleep = uniform(0.45,0.48)
        time.sleep(time_sleep)

    continue_routine(data)