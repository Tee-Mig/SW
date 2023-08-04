import pyautogui
import time
from random import *
from pynput.mouse import Button, Controller
import numbers
import msvcrt
import combat_arene
import default_dungeon_variables
from default_dungeon_variables import default_donjon
import sys
from sell_and_up_runes import select_bad_runes, new_up_runes, select_bad_runes_rift, up_runes_rift
from enums import Dungeon_type, Dimension_type

mouse = Controller()

def take_energy_dungeon():
    if (pyautogui.pixelMatchesColor(1202, 654, (100, 78, 33))):
        while (pyautogui.pixelMatchesColor(1202, 654, (100, 78, 33))):
            x_click = randint(1331,1393)
            y_click = randint(287,340)
            duree = uniform(0.06,0.1)
            pyautogui.click(x_click,y_click,duration=duree)

            print("Je vois attendre enculé")
            time_sleep = uniform(121.0,123.0)
            time.sleep(time_sleep)

            while (pyautogui.locateOnScreen('../img/9_GO.png', region=(1428, 808, 181, 154), confidence=0.95)
                    or pyautogui.locateOnScreen('../img/8_GO.png', region=(1428, 808, 181, 154), confidence=0.95)):
                x_click = randint(1446,1584)
                y_click = randint(841,937)
                mouse.position = (x_click, y_click)
                duree = uniform(0.06,0.1)
                time.sleep(duree)
                mouse.press(Button.left)
                mouse.release(Button.left)

                time_sleep = uniform(0.44,0.47)
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

        # while (pyautogui.locateOnScreen('../img/9_GO.png', region=(1428, 808, 181, 154), confidence=0.95)
        #        or pyautogui.locateOnScreen('../img/8_GO.png', region=(1428, 808, 181, 154), confidence=0.95)):
        #     x_click = randint(1446,1584)
        #     y_click = randint(841,937)
        #     mouse.position = (x_click, y_click)
        #     duree = uniform(0.06,0.1)
        #     time.sleep(duree)
        #     mouse.press(Button.left)
        #     mouse.release(Button.left)

        #     time_sleep = uniform(0.44,0.47)
        #     time.sleep(time_sleep)

def take_screenshot():
    rand_numb = str(randint(0, sys.maxsize))
    file_name = '../new_data/pyautogui_screenshot'
    pyautogui.screenshot('../new_data/' + rand_numb + '7' + rand_numb + '.png')

def rejouer_dj(rejouer_status):
    if (rejouer_status == 1):
        while (pyautogui.locateOnScreen('../img/rejouer_button.png', region=(846, 828, 302, 125))):
            x_click = randint(866,1125)
            y_click = randint(861,927)
            duree = uniform(0.06,0.1)
            pyautogui.click(x_click,y_click,duration=duree)

            time_sleep = uniform(0.41,0.45)
            time.sleep(time_sleep)

    while (1):
            
        if pyautogui.locateOnScreen('../img/emplacements_pleins.jpg', region=(509, 319, 902, 204), confidence=0.99):
            x_click = randint(826,1047)
            y_click = randint(593,676)
            duree = uniform(0.06,0.1)
            pyautogui.click(x_click,y_click,duration=duree)

        if (pyautogui.locateOnScreen('../img/rejouer_combat_repet_raid2.png', region=(92, 816, 173, 189), confidence=0.9)):
            while (pyautogui.locateOnScreen('../img/rejouer_combat_repet_raid2.png', region=(92, 816, 173, 189), confidence=0.9)):

                # time_sleep = uniform(0.41,0.45)
                # time.sleep(time_sleep)

                x_click = randint(1467,1756)
                y_click = randint(856,968)
                duree = uniform(0.06,0.1)
                pyautogui.click(x_click,y_click,duration=duree)

                time_sleep = uniform(0.41,0.45)
                time.sleep(time_sleep)

                if (pyautogui.pixelMatchesColor(1202, 654, (100, 78, 33))
                    or pyautogui.pixelMatchesColor(1197, 649, (202, 161, 71))):
                    break

            break

        # if (pyautogui.locateOnScreen('../img/rejouer_combat_repet_free_raid.png', region=(1424, 804, 376, 205), confidence=0.9)):
        #     x_click = randint(1467,1756)
        #     y_click = randint(856,968)
        #     duree = uniform(0.06,0.1)
        #     pyautogui.click(x_click,y_click,duration=duree)

        #     time_sleep = uniform(0.41,0.45)
        #     time.sleep(time_sleep)
        #     break

        if (pyautogui.locateOnScreen('../img/rejouer_combat_repet_dj.png', region=(1347, 620, 394, 392), confidence=0.9)):
            x_pos_mob = pyautogui.locateOnScreen('../img/rejouer_combat_repet_dj.png', region=(1347, 620, 394, 392), confidence=0.9)
            x_click, y_click = pyautogui.center(x_pos_mob)
            x_click_add = randint(-130,126)
            y_click_add = randint(-47,44)
            x_click += x_click_add
            y_click += y_click_add
            duree = uniform(0.06,0.1)
            pyautogui.click(x_click,y_click,duration=duree)

            time_sleep = uniform(0.41,0.45)
            time.sleep(time_sleep)
            break

        if (pyautogui.locateOnScreen('../img/rejouer_combat_repet_dimension.png', region=(1347, 620, 394, 392), confidence=0.9)):
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
            break

        if (pyautogui.locateOnScreen('../img/rejouer_combat_repet_scenario.png', region=(1347, 620, 394, 392), confidence=0.9)):
            x_pos_mob = pyautogui.locateOnScreen('../img/rejouer_combat_repet_scenario.png', region=(1347, 620, 394, 392), confidence=0.9)
            x_click, y_click = pyautogui.center(x_pos_mob)
            x_click_add = randint(-130,126)
            y_click_add = randint(-47,44)
            x_click += x_click_add
            y_click += y_click_add
            duree = uniform(0.06,0.1)
            pyautogui.click(x_click,y_click,duration=duree)

            time_sleep = uniform(0.41,0.45)
            time.sleep(time_sleep)
            break

        time_sleep = uniform(0.02,0.09)
        time.sleep(time_sleep)
    while (pyautogui.locateOnScreen('../img/rejouer_combat_repet_raid2.png', region=(92, 816, 173, 189), confidence=0.9)
            or pyautogui.locateOnScreen('../img/rejouer_combat_repet_dj.png', region=(1347, 620, 394, 392), confidence=0.9)
            or pyautogui.locateOnScreen('../img/rejouer_combat_repet_free_raid.png', region=(1424, 804, 376, 205), confidence=0.9)
            or pyautogui.locateOnScreen('../img/rejouer_combat_repet_dimension.png', region=(1347, 620, 394, 392), confidence=0.9)
            or pyautogui.locateOnScreen('../img/rejouer_combat_repet_scenario.png', region=(1347, 620, 394, 392), confidence=0.9)):
        img = pyautogui.screenshot()
        # if (pyautogui.pixelMatchesColor(1197, 649, (202, 161, 71))):
        if (pyautogui.pixelMatchesColor(1202, 654, (100, 78, 33))
            or pyautogui.locateOnScreen('../img/no_dimension_energy.jpg', region=(351, 230, 1155, 456), confidence=0.95)):
            break
        # if (0):
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

            while (1):
                if pyautogui.locateOnScreen('../img/emplacements_pleins.jpg', region=(509, 319, 902, 204), confidence=0.99):
                    x_click = randint(826,1047)
                    y_click = randint(593,676)
                    duree = uniform(0.06,0.1)
                    pyautogui.click(x_click,y_click,duration=duree)

                if (pyautogui.locateOnScreen('../img/rejouer_combat_repet_raid2.png', region=(92, 816, 173, 189), confidence=0.9)):
                    while (pyautogui.locateOnScreen('../img/rejouer_combat_repet_raid2.png', region=(92, 816, 173, 189), confidence=0.9)):
                        x_click = randint(1467,1756)
                        y_click = randint(856,968)
                        duree = uniform(0.06,0.1)
                        pyautogui.click(x_click,y_click,duration=duree)

                        time_sleep = uniform(0.41,0.45)
                        time.sleep(time_sleep)

                        if (pyautogui.pixelMatchesColor(1202, 654, (100, 78, 33))
                            or pyautogui.pixelMatchesColor(1197, 649, (202, 161, 71))):
                            break

                    break

                if (pyautogui.locateOnScreen('../img/rejouer_combat_repet_dj.png', region=(1347, 620, 394, 392), confidence=0.9)):
                    x_pos_mob = pyautogui.locateOnScreen('../img/rejouer_combat_repet_dj.png', region=(1347, 620, 394, 392), confidence=0.9)
                    x_click, y_click = pyautogui.center(x_pos_mob)
                    x_click_add = randint(-130,126)
                    y_click_add = randint(-47,44)
                    x_click += x_click_add
                    y_click += y_click_add
                    duree = uniform(0.06,0.1)
                    pyautogui.click(x_click,y_click,duration=duree)

                    time_sleep = uniform(0.41,0.45)
                    time.sleep(time_sleep)
                    break

                if (pyautogui.locateOnScreen('../img/rejouer_combat_repet_dimension.png', region=(1347, 620, 394, 392), confidence=0.9)):
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
                    break

                if (pyautogui.locateOnScreen('../img/rejouer_combat_repet_scenario.png', region=(1347, 620, 394, 392), confidence=0.9)):
                    x_pos_mob = pyautogui.locateOnScreen('../img/rejouer_combat_repet_scenario.png', region=(1347, 620, 394, 392), confidence=0.9)
                    x_click, y_click = pyautogui.center(x_pos_mob)
                    x_click_add = randint(-130,126)
                    y_click_add = randint(-47,44)
                    x_click += x_click_add
                    y_click += y_click_add
                    duree = uniform(0.06,0.1)
                    pyautogui.click(x_click,y_click,duration=duree)

                    time_sleep = uniform(0.41,0.45)
                    time.sleep(time_sleep)
                    break

                time_sleep = uniform(0.02,0.09)
                time.sleep(time_sleep)

def sell_stuffs(status_dungeon, data):
    while (pyautogui.locateOnScreen('../img/vente_selective.png', region=(1406, 831, 356, 135)) == None):
        time_sleep = uniform(0.22,0.29)
        time.sleep(time_sleep)

    x_click = randint(1454,1722)
    y_click = randint(886,930)
    duree = uniform(0.06,0.1)
    pyautogui.click(x_click,y_click,duration=duree)

    time_sleep = uniform(0.33,0.36)
    time.sleep(time_sleep)

    if ((status_dungeon >= Dungeon_type.NONE.value and status_dungeon <= Dungeon_type.NECRO.value)
        or (status_dungeon > Dimension_type.NONE.value and status_dungeon <= Dimension_type.KARZHAN.value)):
        select_bad_runes()
    # elif (status_dungeon >= Dungeon_type.FIRE_RIFT.value and status_dungeon <= Dungeon_type.DARK_RIFT.value):
    #     select_bad_runes_rift()
    # take_screenshot()

    while (pyautogui.locateOnScreen('../img/vente_selective2.png', region=(1236, 822, 307, 173)) == None):
        time_sleep = uniform(0.22,0.29)
        time.sleep(time_sleep)

    x_click = randint(1285,1494)
    y_click = randint(885,952)
    duree = uniform(0.06,0.1)
    pyautogui.click(x_click,y_click,duration=duree)

    time_sleep = uniform(0.33,0.36)
    time.sleep(time_sleep)

    # print("test 11111111111111111111")

    while (pyautogui.locateOnScreen('../img/rejouer_button.png', region=(846, 828, 302, 125)) == None):
        if (pyautogui.locateOnScreen('../img/oui_sell_runes.png', region=(490, 456, 875, 296), confidence=0.9)):
            x_pos_mob = pyautogui.locateOnScreen('../img/oui_sell_runes.png', region=(490, 456, 875, 296), confidence=0.9)
            x_click, y_click = pyautogui.center(x_pos_mob)
            x_click_add = randint(-98,97)
            y_click_add = randint(-30,27)
            x_click += x_click_add
            y_click += y_click_add
            duree = uniform(0.06,0.1)
            pyautogui.click(x_click,y_click,duration=duree)

        if (pyautogui.locateOnScreen('../img/oui_sell_leg.png', region=(643, 549, 279, 169), confidence=0.9)):
            x_pos_mob = pyautogui.locateOnScreen('../img/oui_sell_leg.png', region=(643, 549, 279, 169), confidence=0.9)
            x_click, y_click = pyautogui.center(x_pos_mob)
            x_click_add = randint(-98,97)
            y_click_add = randint(-30,27)
            x_click += x_click_add
            y_click += y_click_add
            duree = uniform(0.06,0.1)
            pyautogui.click(x_click,y_click,duration=duree)

        if (pyautogui.locateOnScreen('../img/oui_meule_hero_ou_sup.png', region=(490, 456, 875, 296), confidence=0.9)):
            x_pos_mob = pyautogui.locateOnScreen('../img/oui_meule_hero_ou_sup.png', region=(490, 456, 875, 296), confidence=0.9)
            x_click, y_click = pyautogui.center(x_pos_mob)
            x_click_add = randint(-98,97)
            y_click_add = randint(-30,27)
            x_click += x_click_add
            y_click += y_click_add
            duree = uniform(0.06,0.1)
            pyautogui.click(x_click,y_click,duration=duree)

        if (pyautogui.locateOnScreen('../img/oui_sell_runes_no_selection.png', region=(490, 456, 875, 296), confidence=0.9)):
            x_pos_mob = pyautogui.locateOnScreen('../img/oui_sell_runes_no_selection.png', region=(490, 456, 875, 296), confidence=0.9)
            x_click, y_click = pyautogui.center(x_pos_mob)
            x_click_add = randint(-98,97)
            y_click_add = randint(-30,27)
            x_click += x_click_add
            y_click += y_click_add
            duree = uniform(0.06,0.1)
            pyautogui.click(x_click,y_click,duration=duree)

            time_sleep = uniform(0.51,0.55)
            time.sleep(time_sleep)

            x_click = randint(1522,1732)
            y_click = randint(886,949)
            duree = uniform(0.06,0.1)
            pyautogui.click(x_click,y_click,duration=duree)

        time_sleep = uniform(0.02,0.09)
        time.sleep(time_sleep)


    if ((status_dungeon >= Dungeon_type.NONE.value and status_dungeon <= Dungeon_type.NECRO.value)
        or (status_dungeon > Dimension_type.NONE.value and status_dungeon <= Dimension_type.KARZHAN.value)):
        new_up_runes(data)
    # elif (status_dungeon >= Dungeon_type.FIRE_RIFT.value and status_dungeon <= Dungeon_type.DARK_RIFT.value):
    #     up_runes_rift()

    while (pyautogui.locateOnScreen('../img/vente_selective.png', region=(1406, 831, 356, 135)) == None):
        time_sleep = uniform(0.22,0.29)
        time.sleep(time_sleep)

def descend_liste_dj():
        x_pos = randint(330, 647)
        y_pos = randint(409, 837)

        # x_drag_and_drop_range = randint(88, 137)
        # y_drag_and_drop_range = randint(280, 416)
        x_drag_and_drop_range = randint(17, 26)
        y_drag_and_drop_range = randint(50, 70)
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

def launch_dungeon(status_dungeon, click_building_status, close_window_status, data):

        if (click_building_status == 1):
                # click sur le batiment
                while (pyautogui.locateOnScreen('../img/repetition_building.png', region=(247, 220, 1289, 609), confidence=0.5) == None):
                    time_sleep = uniform(0.22,0.31)
                    time.sleep(time_sleep)

                # x_pos_mob = pyautogui.locateOnScreen('../img/repetition_building.png', region=(247, 220, 1289, 609), confidence=0.5)
                # x_click, y_click = pyautogui.center(x_pos_mob)
                # x_click_add = randint(-20,20)
                # y_click_add = randint(-20,20)
                # x_click += x_click_add
                # y_click += y_click_add
                # mouse.position = (x_click, y_click)
                # duree = uniform(0.06,0.1)
                # time.sleep(duree)
                # mouse.press(Button.left)
                # mouse.release(Button.left)

                # while (pyautogui.locateOnScreen('../img/recharger.jpg', region=(1265, 827, 236, 223), confidence=0.8) == None):
                #     time_sleep = uniform(0.08,0.12)
                #     time.sleep(time_sleep)

                while (pyautogui.locateOnScreen('../img/recharger.jpg', region=(1265, 827, 236, 223), confidence=0.8) == None):
                    x_pos_mob = pyautogui.locateOnScreen('../img/repetition_building.png', region=(247, 220, 1289, 609), confidence=0.5)
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

                    time_sleep = uniform(0.52,0.55)
                    time.sleep(time_sleep)

                # click sur combat a repetition
                # while (pyautogui.locateOnScreen('../img/combat_repet_button.png', region=(952, 834, 182, 194), confidence=0.6) == None):
                #     time_sleep = uniform(0.22,0.31)
                #     time.sleep(time_sleep)


                while (pyautogui.locateOnScreen('../img/combat_a_repet.jpg', region=(105, 92, 638, 170), confidence=0.8) == None):
                    x_click = randint(993,1101)
                    y_click = randint(903,998)
                    mouse.position = (x_click, y_click)
                    duree = uniform(0.06,0.1)
                    time.sleep(duree)
                    mouse.press(Button.left)
                    mouse.release(Button.left)

                    time_sleep = uniform(0.52,0.55)
                    time.sleep(time_sleep)

                time_sleep = uniform(0.43,0.46)
                time.sleep(time_sleep)

                if (pyautogui.locateOnScreen('../img/recompenses_en_ordre.jpg', region=(479, 311, 949, 232), confidence=0.9)):
                    x_click = randint(982,1203)
                    y_click = randint(594,678)
                    mouse.position = (x_click, y_click)
                    duree = uniform(0.06,0.1)
                    time.sleep(duree)
                    mouse.press(Button.left)
                    mouse.release(Button.left)

                if (pyautogui.locateOnScreen('../img/finir_dj.png', region=(357, 230, 1138, 589))):
                    x_click = randint(983,1199)
                    y_click = randint(594,677)
                    mouse.position = (x_click, y_click)
                    duree = uniform(0.06,0.1)
                    time.sleep(duree)
                    mouse.press(Button.left)
                    mouse.release(Button.left)

        while (pyautogui.locateOnScreen('../img/donjon_cairos_button.png', region=(1160, 445, 605, 187), confidence=0.9) == None
                and pyautogui.locateOnScreen('../img/vente_selective.png', region=(1406, 831, 356, 135)) == None):
                if (pyautogui.locateOnScreen('../img/karzhan.png', region=(1141, 284, 642, 208), confidence=0.9)):
                    x_click = randint(1196,1440)
                    y_click = randint(246,302)
                    mouse.position = (x_click, y_click)
                    duree = uniform(0.06,0.1)
                    time.sleep(duree)
                    mouse.press(Button.left)
                    mouse.release(Button.left)

                time_sleep = uniform(0.22,0.31)
                time.sleep(time_sleep)
        
        time_sleep = uniform(0.49,0.51)
        time.sleep(time_sleep)

        if (pyautogui.locateOnScreen('../img/donjon_cairos_button.png', region=(1160, 445, 605, 187), confidence=0.95)):
            time_sleep = uniform(0.22,0.31)
            time.sleep(time_sleep)

            if (status_dungeon >= Dungeon_type.GIANT.value and status_dungeon <= Dungeon_type.CRYPT.value):
                while (pyautogui.locateOnScreen('../img/donjon_cairos_button.png', region=(1160, 445, 605, 187), confidence=0.9)):
                    x_click = randint(1193,1725)
                    y_click = randint(488,600)
                    mouse.position = (x_click, y_click)
                    duree = uniform(0.06,0.1)
                    time.sleep(duree)
                    mouse.press(Button.left)
                    mouse.release(Button.left)

                    time_sleep = uniform(0.44,0.47)
                    time.sleep(time_sleep)

                # click sur Taniere du dragon
                if (status_dungeon == Dungeon_type.DRAGON.value):
                        while (pyautogui.locateOnScreen('../img/taniere_du_dragon.png', region=(275, 460, 448, 180), confidence=0.9) == None):
                                time_sleep = uniform(0.22,0.31)
                                time.sleep(time_sleep)

                        while (pyautogui.locateOnScreen('../img/9_GO.png', region=(1428, 808, 181, 154), confidence=0.95) == None):
                            x_click = randint(299,693)
                            y_click = randint(504,616)
                            mouse.position = (x_click, y_click)
                            duree = uniform(0.06,0.1)
                            time.sleep(duree)
                            mouse.press(Button.left)
                            mouse.release(Button.left)

                            time_sleep = uniform(0.44,0.47)
                            time.sleep(time_sleep)
                
                # click sur Necro
                if (status_dungeon == Dungeon_type.NECRO.value):
                        while (pyautogui.locateOnScreen('../img/necro.png', region=(254, 607, 484, 199), confidence=0.9) == None):
                                time_sleep = uniform(0.22,0.31)
                                time.sleep(time_sleep)

                        while (pyautogui.locateOnScreen('../img/9_GO.png', region=(1428, 808, 181, 154), confidence=0.95) == None):
                            x_click = randint(303,691)
                            y_click = randint(659,763)
                            mouse.position = (x_click, y_click)
                            duree = uniform(0.06,0.1)
                            time.sleep(duree)
                            mouse.press(Button.left)
                            mouse.release(Button.left)

                            time_sleep = uniform(0.44,0.47)
                            time.sleep(time_sleep)

                # click sur Spiritual Realm
                if (status_dungeon == Dungeon_type.SPIRITUAL_REALM.value):
                        while (pyautogui.locateOnScreen('../img/spiritual_realm.png', region=(257, 767, 474, 189), confidence=0.9) == None):
                                time_sleep = uniform(0.22,0.31)
                                time.sleep(time_sleep)

                        while (pyautogui.locateOnScreen('../img/8_GO.png', region=(1428, 808, 181, 154), confidence=0.95) == None):
                            x_click = randint(305,687)
                            y_click = randint(813,918)
                            mouse.position = (x_click, y_click)
                            duree = uniform(0.06,0.1)
                            time.sleep(duree)
                            mouse.press(Button.left)
                            mouse.release(Button.left)

                            time_sleep = uniform(0.44,0.47)
                            time.sleep(time_sleep)

                # click sur Forteresse
                if (status_dungeon == Dungeon_type.FORTRESS.value):
                        while (pyautogui.locateOnScreen('../img/forteresse.png', region=(250, 287, 498, 712), confidence=0.9) == None):
                                descend_liste_dj()
                                time_sleep = uniform(0.59,0.63)
                                time.sleep(time_sleep)

                        while (pyautogui.locateOnScreen('../img/8_GO.png', region=(1428, 808, 181, 154), confidence=0.95) == None):
                            x_pos_mob = pyautogui.locateOnScreen('../img/forteresse.png', region=(250, 287, 498, 712), confidence=0.9)
                            x_click, y_click = pyautogui.center(x_pos_mob)
                            x_click_add = randint(-140,140)
                            y_click_add = randint(-40,40)
                            x_click += x_click_add
                            y_click += y_click_add
                            duree = uniform(0.06,0.1)
                            pyautogui.click(x_click,y_click,duration=duree)

                            time_sleep = uniform(0.44,0.47)
                            time.sleep(time_sleep)

                # click sur crypte du jugement
                if (status_dungeon == Dungeon_type.CRYPT.value):
                        while (pyautogui.locateOnScreen('../img/crypte.png', region=(250, 287, 498, 712), confidence=0.9) == None):
                                descend_liste_dj()
                                time_sleep = uniform(0.59,0.63)
                                time.sleep(time_sleep)

                        while (pyautogui.locateOnScreen('../img/8_GO.png', region=(1428, 808, 181, 154), confidence=0.95) == None):
                            x_pos_mob = pyautogui.locateOnScreen('../img/crypte.png', region=(250, 287, 498, 712), confidence=0.9)
                            x_click, y_click = pyautogui.center(x_pos_mob)
                            x_click_add = randint(-140,140)
                            y_click_add = randint(-40,40)
                            x_click += x_click_add
                            y_click += y_click_add
                            duree = uniform(0.06,0.1)
                            pyautogui.click(x_click,y_click,duration=duree)

                            time_sleep = uniform(0.44,0.47)
                            time.sleep(time_sleep)

                if (status_dungeon == Dungeon_type.GIANT.value):
                    for i in range(3);
                        descend_liste_dj2()
                    while (pyautogui.locateOnScreen('../img/8_GO.png', region=(1408, 460, 224, 177), confidence=0.95) == None
                        and pyautogui.pixelMatchesColor(1202, 654, (100, 78, 33)) == False
                        and pyautogui.pixelMatchesColor(1197, 649, (202, 161, 71)) == False):
                        if (pyautogui.locateOnScreen('../img/6_GO.png', region=(1316, 683, 392, 316), confidence=0.95)
                            or pyautogui.locateOnScreen('../img/7_GO.png', region=(1316, 683, 392, 316), confidence=0.95)):
                            while (pyautogui.locateOnScreen('../img/8_GO.png', region=(1408, 460, 224, 177), confidence=0.95) == None):
                                descend_liste_dj2()
                        time_sleep = uniform(0.22,0.31)
                        time.sleep(time_sleep)

                    while (pyautogui.locateOnScreen('../img/8_GO.png', region=(1408, 460, 224, 177), confidence=0.95)
                            or pyautogui.pixelMatchesColor(1202, 654, (100, 78, 33))
                            or pyautogui.pixelMatchesColor(1197, 649, (202, 161, 71))):
                        x_click = randint(1449, 1581)
                        y_click = randint(509, 603)
                        mouse.position = (x_click, y_click)
                        duree = uniform(0.06,0.1)
                        time.sleep(duree)
                        mouse.press(Button.left)
                        mouse.release(Button.left)

                        time_sleep = uniform(0.57,0.59)
                        time.sleep(time_sleep)

                        take_energy_dungeon()

                    # click sur 9x10 combat a repetition
                    while (pyautogui.locateOnScreen('../img/8x10_combat_repet.png', region=(1366, 635, 367, 201), confidence=0.95) == None):
                        time_sleep = uniform(0.05,0.09)
                        time.sleep(time_sleep)

                    while (pyautogui.locateOnScreen('../img/8x10_combat_repet.png', region=(1366, 635, 367, 201), confidence=0.95)):
                        x_pos_mob = pyautogui.locateOnScreen('../img/8x10_combat_repet.png', region=(1366, 635, 367, 201), confidence=0.95)
                        x_click, y_click = pyautogui.center(x_pos_mob)
                        x_click_add = randint(-136,126)
                        y_click_add = randint(-45,45)
                        x_click += x_click_add
                        y_click += y_click_add
                        duree = uniform(0.06,0.1)
                        pyautogui.click(x_click,y_click,duration=duree)

                        time_sleep = uniform(0.44,0.47)
                        time.sleep(time_sleep)
                
                # if (status_dungeon == Dungeon_type.GIANT.value or status_dungeon == Dungeon_type.DRAGON.value or status_dungeon == Dungeon_type.NECRO.value):
                if (status_dungeon == Dungeon_type.DRAGON.value or status_dungeon == Dungeon_type.NECRO.value):
                # click sur GO
                        while (pyautogui.locateOnScreen('../img/9_GO.png', region=(1428, 808, 181, 154), confidence=0.95) == None):
                            if (pyautogui.locateOnScreen('../img/6_GO.png', region=(1316, 683, 392, 316), confidence=0.95)
                                or pyautogui.locateOnScreen('../img/7_GO.png', region=(1316, 683, 392, 316), confidence=0.95)):
                                while (pyautogui.locateOnScreen('../img/9_GO.png', region=(1428, 808, 181, 154), confidence=0.95) == None):
                                    descend_liste_dj2()
                            time_sleep = uniform(0.22,0.31)
                            time.sleep(time_sleep)

                        while (pyautogui.locateOnScreen('../img/9_GO.png', region=(1428, 808, 181, 154), confidence=0.95)
                                or pyautogui.pixelMatchesColor(1202, 654, (100, 78, 33))
                                or pyautogui.pixelMatchesColor(1197, 649, (202, 161, 71))):
                            x_click = randint(1446,1584)
                            y_click = randint(841,937)
                            mouse.position = (x_click, y_click)
                            duree = uniform(0.06,0.1)
                            time.sleep(duree)
                            mouse.press(Button.left)
                            mouse.release(Button.left)

                            time_sleep = uniform(0.57,0.59)
                            time.sleep(time_sleep)

                            take_energy_dungeon()

                        # click sur 9x10 combat a repetition
                        while (pyautogui.locateOnScreen('../img/9x10_combat_repet.png', region=(1366, 635, 367, 201), confidence=0.95) == None):
                            time_sleep = uniform(0.05,0.09)
                            time.sleep(time_sleep)

                        while (pyautogui.locateOnScreen('../img/9x10_combat_repet.png', region=(1366, 635, 367, 201), confidence=0.95)):
                            x_pos_mob = pyautogui.locateOnScreen('../img/9x10_combat_repet.png', region=(1366, 635, 367, 201), confidence=0.95)
                            x_click, y_click = pyautogui.center(x_pos_mob)
                            x_click_add = randint(-136,126)
                            y_click_add = randint(-45,45)
                            x_click += x_click_add
                            y_click += y_click_add
                            duree = uniform(0.06,0.1)
                            pyautogui.click(x_click,y_click,duration=duree)

                            time_sleep = uniform(0.44,0.47)
                            time.sleep(time_sleep)

                if (status_dungeon == Dungeon_type.FORTRESS.value or status_dungeon == Dungeon_type.CRYPT.value or status_dungeon == Dungeon_type.SPIRITUAL_REALM.value):
                # click sur GO
                        while (pyautogui.locateOnScreen('../img/8_GO.png', region=(1428, 808, 181, 154), confidence=0.95) == None
                            and pyautogui.pixelMatchesColor(1202, 654, (100, 78, 33)) == False
                            and pyautogui.pixelMatchesColor(1197, 649, (202, 161, 71)) == False):
                            if (pyautogui.locateOnScreen('../img/6_GO.png', region=(1316, 683, 392, 316), confidence=0.95)
                                or pyautogui.locateOnScreen('../img/7_GO.png', region=(1316, 683, 392, 316), confidence=0.95)):
                                while (pyautogui.locateOnScreen('../img/8_GO.png', region=(1428, 808, 181, 154), confidence=0.95) == None):
                                    descend_liste_dj2()
                            time_sleep = uniform(0.22,0.31)
                            time.sleep(time_sleep)

                        while (pyautogui.locateOnScreen('../img/8_GO.png', region=(1428, 808, 181, 154), confidence=0.95)
                                or pyautogui.pixelMatchesColor(1202, 654, (100, 78, 33))
                                or pyautogui.pixelMatchesColor(1197, 649, (202, 161, 71))):
                            x_click = randint(1446,1584)
                            y_click = randint(841,937)
                            mouse.position = (x_click, y_click)
                            duree = uniform(0.06,0.1)
                            time.sleep(duree)
                            mouse.press(Button.left)
                            mouse.release(Button.left)

                            time_sleep = uniform(0.57,0.59)
                            time.sleep(time_sleep)

                            take_energy_dungeon()

                        # click sur 9x10 combat a repetition
                        while (pyautogui.locateOnScreen('../img/8x10_combat_repet.png', region=(1366, 635, 367, 201), confidence=0.95) == None):
                            time_sleep = uniform(0.05,0.09)
                            time.sleep(time_sleep)

                        while (pyautogui.locateOnScreen('../img/8x10_combat_repet.png', region=(1366, 635, 367, 201), confidence=0.95)):
                            x_pos_mob = pyautogui.locateOnScreen('../img/8x10_combat_repet.png', region=(1366, 635, 367, 201), confidence=0.95)
                            x_click, y_click = pyautogui.center(x_pos_mob)
                            x_click_add = randint(-136,126)
                            y_click_add = randint(-45,45)
                            x_click += x_click_add
                            y_click += y_click_add
                            duree = uniform(0.06,0.1)
                            pyautogui.click(x_click,y_click,duration=duree)

                            time_sleep = uniform(0.44,0.47)
                            time.sleep(time_sleep)

            if (status_dungeon == Dungeon_type.R5.value):
                while (pyautogui.locateOnScreen('../img/donjon_cairos_button.png', region=(1160, 445, 605, 187), confidence=0.95)):
                    x_click = randint(1193,1722)
                    y_click = randint(799,904)
                    mouse.position = (x_click, y_click)
                    duree = uniform(0.06,0.1)
                    time.sleep(duree)
                    mouse.press(Button.left)
                    mouse.release(Button.left)

                    time_sleep = uniform(0.44,0.47)
                    time.sleep(time_sleep)

                while (pyautogui.locateOnScreen('../img/combat_raid.png', region=(1117, 708, 482, 266), confidence=0.95) == None):
                    time_sleep = uniform(0.05,0.09)
                    time.sleep(time_sleep)

                while (pyautogui.locateOnScreen('../img/combat_raid.png', region=(1117, 708, 482, 266), confidence=0.95)):
                    x_click = randint(1192,1523)
                    y_click = randint(793,899)
                    mouse.position = (x_click, y_click)
                    duree = uniform(0.06,0.1)
                    time.sleep(duree)
                    mouse.press(Button.left)
                    mouse.release(Button.left)

                    time_sleep = uniform(0.57,0.59)
                    time.sleep(time_sleep)

                while (pyautogui.locateOnScreen('../img/rejouer_combat_repet_raid2.png', region=(92, 816, 173, 189), confidence=0.9) == None):
                    time_sleep = uniform(0.05,0.09)
                    time.sleep(time_sleep)

                while ((pyautogui.locateOnScreen('../img/rejouer_combat_repet_raid2.png', region=(92, 816, 173, 189), confidence=0.9))):
                    # time_sleep = uniform(0.41,0.45)
                    # time.sleep(time_sleep)

                    x_click = randint(1467,1756)
                    y_click = randint(856,968)
                    duree = uniform(0.06,0.1)
                    pyautogui.click(x_click,y_click,duration=duree)

                    time_sleep = uniform(0.41,0.45)
                    time.sleep(time_sleep)

                    take_energy_dungeon()

            if (status_dungeon >= Dungeon_type.FIRE_RIFT.value and status_dungeon <= Dungeon_type.DARK_RIFT.value):
                while (pyautogui.locateOnScreen('../img/donjon_cairos_button.png', region=(1160, 445, 605, 187), confidence=0.95)):
                    x_click = randint(1192,1724)
                    y_click = randint(646,747)
                    mouse.position = (x_click, y_click)
                    duree = uniform(0.06,0.1)
                    time.sleep(duree)
                    mouse.press(Button.left)
                    mouse.release(Button.left)

                    time_sleep = uniform(0.44,0.47)
                    time.sleep(time_sleep)

                while (pyautogui.locateOnScreen('../img/combat_rift.png', region=(1117, 708, 482, 266), confidence=0.95) == None):
                    time_sleep = uniform(0.05,0.09)
                    time.sleep(time_sleep)

                if (status_dungeon == Dungeon_type.WATER_RIFT.value):
                    while (pyautogui.locateOnScreen('../img/water_rift.png', region=(521, 271, 676, 525), confidence=0.95) == None):
                        x_click = randint(1041,1132)
                        y_click = randint(194,288)
                        mouse.position = (x_click, y_click)
                        duree = uniform(0.06,0.1)
                        time.sleep(duree)
                        mouse.press(Button.left)
                        mouse.release(Button.left)

                        time_sleep = uniform(0.44,0.47)
                        time.sleep(time_sleep)

                if (status_dungeon == Dungeon_type.WIND_RIFT.value):
                    while (pyautogui.locateOnScreen('../img/wind_rift.png', region=(521, 271, 676, 525), confidence=0.95) == None):
                        x_click = randint(1172,1260)
                        y_click = randint(196,278)
                        mouse.position = (x_click, y_click)
                        duree = uniform(0.06,0.1)
                        time.sleep(duree)
                        mouse.press(Button.left)
                        mouse.release(Button.left)

                        time_sleep = uniform(0.44,0.47)
                        time.sleep(time_sleep)
                
                if (status_dungeon == Dungeon_type.LIGHT_RIFT.value):
                    while (pyautogui.locateOnScreen('../img/light_rift.png', region=(521, 271, 676, 525), confidence=0.95) == None):
                        x_click = randint(1302,1392)
                        y_click = randint(197,285)
                        mouse.position = (x_click, y_click)
                        duree = uniform(0.06,0.1)
                        time.sleep(duree)
                        mouse.press(Button.left)
                        mouse.release(Button.left)

                        time_sleep = uniform(0.44,0.47)
                        time.sleep(time_sleep)

                if (status_dungeon == Dungeon_type.DARK_RIFT.value):
                    while (pyautogui.locateOnScreen('../img/dark_rift.png', region=(521, 271, 676, 525), confidence=0.95) == None):
                        x_click = randint(1436,1528)
                        y_click = randint(193,282)
                        mouse.position = (x_click, y_click)
                        duree = uniform(0.06,0.1)
                        time.sleep(duree)
                        mouse.press(Button.left)
                        mouse.release(Button.left)

                        time_sleep = uniform(0.44,0.47)
                        time.sleep(time_sleep)

                while (pyautogui.locateOnScreen('../img/combat_rift.png', region=(1117, 708, 482, 266), confidence=0.95)):
                    x_click = randint(1192,1523)
                    y_click = randint(793,899)
                    mouse.position = (x_click, y_click)
                    duree = uniform(0.06,0.1)
                    time.sleep(duree)
                    mouse.press(Button.left)
                    mouse.release(Button.left)

                    time_sleep = uniform(0.57,0.59)
                    time.sleep(time_sleep)

                    take_energy_dungeon()

                while (pyautogui.locateOnScreen('../img/8x10_combat_repet.png', region=(1366, 635, 367, 201), confidence=0.95) == None):
                    time_sleep = uniform(0.05,0.09)
                    time.sleep(time_sleep)

                while (pyautogui.locateOnScreen('../img/8x10_combat_repet.png', region=(1366, 635, 367, 201), confidence=0.95)):
                    x_pos_mob = pyautogui.locateOnScreen('../img/8x10_combat_repet.png', region=(1366, 635, 367, 201), confidence=0.95)
                    x_click, y_click = pyautogui.center(x_pos_mob)
                    x_click_add = randint(-136,126)
                    y_click_add = randint(-45,45)
                    x_click += x_click_add
                    y_click += y_click_add
                    duree = uniform(0.06,0.1)
                    pyautogui.click(x_click,y_click,duration=duree)

                    time_sleep = uniform(0.44,0.47)
                    time.sleep(time_sleep)

            if (close_window_status == 1):
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

        else:
                # --------------------------------------------------------------------------------
                current_dj = get_window_status()
                if (status_dungeon == current_dj):
                    if (pyautogui.locateOnScreen('../img/rejouer_button.png', region=(846, 828, 302, 125))):
                        sell_stuffs(status_dungeon, data)
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
                            time_sleep = uniform(120.0,122.0)
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
                else:
                    if (pyautogui.locateOnScreen('../img/rejouer_button.png', region=(846, 828, 302, 125))):
                        sell_stuffs(current_dj, data)

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

                        launch_dungeon(status_dungeon, 0, 1, data)
                    else:
                        while (pyautogui.locateOnScreen('../img/fin_des_combats.png', region=(716, 802, 467, 176)) == None):
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
                        if (pyautogui.locateOnScreen('../img/selection_donjon.png', region=(124, 806, 339, 168))):
                            sell_stuffs(current_dj, data)

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

                            launch_dungeon(status_dungeon, 0, 1, data)
                # --------------------------------------------------------------------------------
                # if (pyautogui.locateOnScreen('../img/rejouer_button.png', region=(846, 828, 302, 125))):
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

                #     launch_dungeon(status_dungeon, 0, 1, data)
                # else:
                #     # click sur le bouton pour fermer la fenetre combat a repet
                #     while (pyautogui.locateOnScreen('../img/close_window_combat_repet.png', region=(1598, 95, 164, 134), confidence=0.95) == None):
                #         time_sleep = uniform(0.22,0.31)
                #         time.sleep(time_sleep)

                #     # time_sleep = uniform(0.22,0.31)
                #     # time.sleep(time_sleep)

                #     while (pyautogui.locateOnScreen('../img/close_window_combat_repet.png', region=(1598, 95, 164, 134), confidence=0.95)):
                #         x_click = randint(1669,1717)
                #         y_click = randint(154,198)
                #         mouse.position = (x_click, y_click)
                #         duree = uniform(0.06,0.1)
                #         time.sleep(duree)
                #         mouse.press(Button.left)
                #         mouse.release(Button.left)

                #         time_sleep = uniform(0.44,0.48)
                #         time.sleep(time_sleep)

def get_window_status():
    if (pyautogui.locateOnScreen('../img/window_old_giant.jpg', region=(609, 102, 918, 162), confidence=0.9)):
        return Dungeon_type.GIANT.value
    #if (pyautogui.locateOnScreen('../img/window_giant.jpg', region=(609, 102, 918, 162), confidence=0.9)):
    #    return Dungeon_type.GIANT.value
    if (pyautogui.locateOnScreen('../img/window_dragon.jpg', region=(609, 102, 918, 162), confidence=0.9)):
            return Dungeon_type.DRAGON.value
    if (pyautogui.locateOnScreen('../img/window_necro.jpg', region=(609, 102, 918, 162), confidence=0.9)):
        return Dungeon_type.NECRO.value
    if (pyautogui.locateOnScreen('../img/window_spiritual_realm.jpg', region=(609, 102, 918, 162), confidence=0.9)):
        return Dungeon_type.SPIRITUAL_REALM.value
    if (pyautogui.locateOnScreen('../img/window_fortress.jpg', region=(609, 102, 918, 162), confidence=0.9)):
            return Dungeon_type.FORTRESS.value
    if (pyautogui.locateOnScreen('../img/window_crypt.jpg', region=(609, 102, 918, 162), confidence=0.9)):
        return Dungeon_type.CRYPT.value
    
    if (pyautogui.locateOnScreen('../img/window_r5.jpg', region=(609, 102, 918, 162), confidence=0.9)):
        return Dungeon_type.R5.value
    
    if (pyautogui.locateOnScreen('../img/window_fire_rift.jpg', region=(609, 102, 918, 162), confidence=0.9)):
        return Dungeon_type.FIRE_RIFT.value
    if (pyautogui.locateOnScreen('../img/window_water_rift.jpg', region=(609, 102, 918, 162), confidence=0.9)):
        return Dungeon_type.WATER_RIFT.value
    if (pyautogui.locateOnScreen('../img/window_wind_rift.jpg', region=(609, 102, 918, 162), confidence=0.9)):
        return Dungeon_type.WIND_RIFT.value
    if (pyautogui.locateOnScreen('../img/window_light_rift.jpg', region=(609, 102, 918, 162), confidence=0.9)):
        return Dungeon_type.LIGHT_RIFT.value
    if (pyautogui.locateOnScreen('../img/window_dark_rift.jpg', region=(609, 102, 918, 162), confidence=0.9)):
        return Dungeon_type.DARK_RIFT.value
    if (pyautogui.locateOnScreen('../img/window_karzhan.jpg', region=(609, 102, 918, 162), confidence=0.9)):
        return Dimension_type.KARZHAN.value
    return 0
