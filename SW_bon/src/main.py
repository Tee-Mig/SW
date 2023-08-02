import auto_combat_arene
import pyautogui
import pydirectinput
import time
from random import *
from pynput.mouse import Button, Controller
import rivaux
import combat_arene
from rta import auto_arena
from auto_toa import toa_auto
from rta_special_league_SP_20 import rta_special_league_boucle_20_stars
from rival_guild_battle import auto_rival_guild_battle
from world_boss import do_world_boss
from slides import *
from interserver_battle import do_interserver_arena
from rta import rta_boucle
import keyboard
import numbers
import msvcrt
from continue_routine import *
from rta import continue_routine, launch_dungeon, auto_combat, rta_boucle_special_league_4, auto_dj, sell_stuffs
import sys
import cv2
from enums import Dungeon_type, Dimension_type

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

def go_to_arena():
        while (pyautogui.locateOnScreen('../img/arena_building.png', region=(247, 220, 1289, 609), confidence=0.5) == None):
                time_sleep = uniform(0.22,0.31)
                time.sleep(time_sleep)
        x_pos_mob = pyautogui.locateOnScreen('../img/arena_building.png', region=(247, 220, 1289, 609), confidence=0.5)
        x_click, y_click = pyautogui.center(x_pos_mob)
        x_click_add = randint(-20,20)
        y_click_add = randint(-20,20)
        x_click += x_click_add
        y_click += y_click_add
        mouse.position = (x_click, y_click)
        duree = uniform(0.06,0.1)
        time.sleep(duree)
        mouse.press(Button.left)
        mouse.release(Button.left)

def routine(data):
        if (data["world_boss_status"] != 0 and data["world_boss_status"] != 1):
                print("Error world boss status")
                return 1
        if (data["gvg_status"] != 0 and data["gvg_status"] != 1):
                print("Error gvg_status status")
                return 1
        if (data["dimension_status"] < Dimension_type.NONE.value or data["dimension_status"] > Dimension_type.KARZHAN.value):
                print("Error dimension status")
                return 1
        if (data["launch_dungeon_status"] < Dungeon_type.NONE.value or data["launch_dungeon_status"] > Dungeon_type.DARK_RIFT.value):
                print("Error launch dungeon status")
                return 1
        while (pyautogui.locateOnScreen('../img/repetition_building.png', region=(247, 220, 1289, 609), confidence=0.5) == None):
                time_sleep = uniform(0.22,0.31)
                time.sleep(time_sleep)

        do_arena = data["arena_status"]
        if (data["launch_dungeon_status"] != Dungeon_type.NONE.value):
                launch_dungeon(data["launch_dungeon_status"], 1, 1, data)

        if (data["world_boss_status"] == 1 or data["gvg_status"] == 1):
                # while (pyautogui.locateOnScreen('../img/arena_building.png', region=(247, 220, 1289, 609), confidence=0.5) == None):
                #         time_sleep = uniform(0.22,0.31)
                #         time.sleep(time_sleep)

                x_click = randint(994,1106)
                y_click = randint(902,992)
                mouse.position = (x_click, y_click)
                duree = uniform(0.06,0.1)
                time.sleep(duree)
                mouse.press(Button.left)
                mouse.release(Button.left)

        if (data["world_boss_status"] == 1):
                do_world_boss()

        if (data["gvg_status"] == 1):
                while (pyautogui.locateOnScreen('../img/ile_de_combat.png', region=(606, 57, 1194, 322), confidence=0.7) == None):
                        slide_to_right()
                        time_sleep = uniform(0.59,0.63)
                        time.sleep(time_sleep)

                pos_lead = pyautogui.locateOnScreen('../img/ile_de_combat.png', region=(606, 57, 1194, 322), confidence=0.7)
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

                while (pyautogui.locateOnScreen('../img/rivaux_de_guilde.png', region=(139, 172, 566, 708), confidence=0.9) == None):
                        time_sleep = uniform(0.22,0.31)
                        time.sleep(time_sleep)
                
                if (pyautogui.locateOnScreen('../img/rivaux_de_guilde_available.png', region=(589, 163, 126, 126), confidence=0.8)):
                        x_click = randint(197,635)
                        y_click = randint(279,801)
                        mouse.position = (x_click, y_click)
                        duree = uniform(0.06,0.1)
                        time.sleep(duree)
                        mouse.press(Button.left)
                        mouse.release(Button.left)

                        auto_rival_guild_battle()
                else:
                        while (pyautogui.locateOnScreen('../img/rivaux_de_guilde.png', region=(139, 172, 566, 708), confidence=0.9)):
                                x_click = randint(657,1253)
                                y_click = randint(873,1006)
                                mouse.position = (x_click, y_click)
                                duree = uniform(0.06,0.1)
                                time.sleep(duree)
                                mouse.press(Button.left)
                                mouse.release(Button.left)

                                time_sleep = uniform(0.44,0.47)
                                time.sleep(time_sleep)

                while (pyautogui.locateOnScreen('../img/ile_de_combat.png', region=(606, 57, 1194, 322), confidence=0.7) == None):
                        time_sleep = uniform(0.22,0.31)
                        time.sleep(time_sleep)


        if (data["world_boss_status"] == 1 or data["gvg_status"] == 1):
                data["gvg_status"] = 0
                data["world_boss_status"] = 0
                while (pyautogui.locateOnScreen('../img/ile_arena.png', region=(65, 128, 463, 353), confidence=0.9) == None):
                        slide_to_left()
                        time_sleep = uniform(0.59,0.63)
                        time.sleep(time_sleep)

                while (pyautogui.locateOnScreen('../img/ile_arena.png', region=(65, 128, 463, 353), confidence=0.9)):
                        x_click = randint(194, 291)
                        y_click = randint(234, 310)
                        mouse.position = (x_click, y_click)
                        duree = uniform(0.06,0.1)
                        time.sleep(duree)
                        mouse.press(Button.left)
                        mouse.release(Button.left)

                        time_sleep = uniform(0.44,0.47)
                        time.sleep(time_sleep)

                while (pyautogui.locateOnScreen('../img/arena2.png', region=(375, 174, 568, 699), confidence=0.9) == None):
                        time_sleep = uniform(0.22,0.31)
                        time.sleep(time_sleep)

                while (pyautogui.locateOnScreen('../img/arena2.png', region=(375, 174, 568, 699), confidence=0.9)):
                        x_click = randint(432, 870)
                        y_click = randint(244, 798)
                        mouse.position = (x_click, y_click)
                        duree = uniform(0.06,0.1)
                        time.sleep(duree)
                        mouse.press(Button.left)
                        mouse.release(Button.left)

                        time_sleep = uniform(0.44,0.47)
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

        else:
                x_click = randint(994,1106)
                y_click = randint(902,992)
                mouse.position = (x_click, y_click)
                duree = uniform(0.06,0.1)
                time.sleep(duree)
                mouse.press(Button.left)
                mouse.release(Button.left)

                while (pyautogui.locateOnScreen('../img/ile_arena.png', region=(65, 128, 463, 353), confidence=0.9) == None):
                        time_sleep = uniform(0.59,0.63)
                        time.sleep(time_sleep)

                while (pyautogui.locateOnScreen('../img/ile_arena.png', region=(65, 128, 463, 353), confidence=0.9)):
                        x_click = randint(194, 291)
                        y_click = randint(234, 310)
                        mouse.position = (x_click, y_click)
                        duree = uniform(0.06,0.1)
                        time.sleep(duree)
                        mouse.press(Button.left)
                        mouse.release(Button.left)

                        time_sleep = uniform(0.44,0.47)
                        time.sleep(time_sleep)

                while (pyautogui.locateOnScreen('../img/arena2.png', region=(375, 174, 568, 699), confidence=0.9) == None):
                        time_sleep = uniform(0.22,0.31)
                        time.sleep(time_sleep)

                while (pyautogui.locateOnScreen('../img/arena2.png', region=(375, 174, 568, 699), confidence=0.9)):
                        x_click = randint(432, 870)
                        y_click = randint(244, 798)
                        mouse.position = (x_click, y_click)
                        duree = uniform(0.06,0.1)
                        time.sleep(duree)
                        mouse.press(Button.left)
                        mouse.release(Button.left)

                        time_sleep = uniform(0.44,0.47)
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

                # else:
                #         go_to_arena()
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

import time

def take_sreenshot_for_tests():
        while (True):
                if (msvcrt.getch()):
                        click_windows()
                        time_sleep = uniform(0.45,0.48)
                        time.sleep(time_sleep)
                        rand_numb = str(randint(0, sys.maxsize))
                        pyautogui.screenshot('../test_type_rune/' + rand_numb + '7' + rand_numb + '.png')

def descend_liste_dj2():
        x_pos = randint(881, 1367)
        y_pos = randint(390, 876)

        x_drag_and_drop_range = randint(30, 50)
        y_drag_and_drop_range = randint(90, 130)
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

        time_sleep = uniform(0.59,0.63)
        time.sleep(time_sleep)

import pytesseract as pyt
import cv2
import numpy as np
import re
from up_runes import old_up_all_runes, rune_process, get_subs, check_if_bad_sub_proc_on_up, get_good_sub, compute_efficiency, get_amelioration, new_up_rune
from sell_and_up_runes import select_bad_runes, new_up_runes, rune_process_new, get_grade, get_subs_in_dj, get_slot
from rta import get_current_energy

def main():
        data = {
                "rune_properties" : {
                        # "subs" : [],
                        # "grade" : None,
                        # "amelioration" : None,
                        # "slot" : None,
                        "heroic_bad_proc_sell" : 1,
                        "legend_bad_proc_sell" : 2,
                        "tc_vit_one_proc" : 14, # heroic + 6 or legend + 9 -> one proc left
                        "tc_vit_max_proc" : 20, 
                        "dcc_one_proc" : 15, # heroic + 9 or legend + 12 -> no proc left
                        "dcc_max_proc" : 22, 
                        "percent_one_proc" : 19, # check proc for atq, def, hp, accuracy and res
                        "percent_max_proc" : 27,
                        "1_3_5_efficiency_heroic" : 0.732,
                        "2_4_6_efficiency_heroic" : 0.696,
                        "1_3_5_efficiency_legend_plus_9" : 0.723,
                        "1_3_5_efficiency_legend" : 0.794,
                        "2_4_6_efficiency_legend_plus_9" : 0.687,
                        "2_4_6_efficiency_legend" : 0.758,
                },
                "min_energy_launch_dungeon" : 90,
                "world_boss_status" : 0,
                "gvg_status" : 0,
                "rta_status" : 0,
                "arena_status" : 0,
                "dimension_status" : Dimension_type.NONE.value,
                "launch_dungeon_status" : Dungeon_type.GIANT.value
        }

        data["launch_dungeon_status"] = int(input("enter the dungeon to launch:\n0: None| 1: giant | 2: dragon | 3: spiritual realm | 4: necro | 5: fortress | 6: crypt |\n7: r5 | 8: fire rift  | 9: water rift  | 10: wind rift  | 11: light rift  | 12: dark rift : "))
        while (data["launch_dungeon_status"] < Dungeon_type.NONE.value or data["launch_dungeon_status"] > Dungeon_type.DARK_RIFT.value):
                data["launch_dungeon_status"] = int(input("enter the dungeon to launch:\n0: None| 1: giant | 2: dragon | 3: spiritual realm | 4: necro | 5: fortress | 6: crypt |\n7: r5 | 8: fire rift  | 9: water rift  | 10: wind rift  | 11: light rift  | 12: dark rift : "))

        click_windows()
        routine(data)

        print("Fin")

if __name__ == '__main__':
        main()