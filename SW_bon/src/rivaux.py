import pyautogui
import time
from random import *
from pynput.mouse import Button, Controller
from auto_combat_arene import ou_est_la_cible_emplacement_deux_ou_quatre

mouse = Controller()

def descend_liste():
        x_pos = randint(671, 1186)
        y_pos = randint(446, 759)

        # x_drag_and_drop_range = randint(88, 137)
        # y_drag_and_drop_range = randint(280, 416)
        x_drag_and_drop_range = randint(55, 75)
        y_drag_and_drop_range = randint(160, 228)
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

def auto_maximilian():
    combat_finit = 0
    while  combat_finit == 0:
        #auto maximilian
        if pyautogui.locateOnScreen('../img/sort1_maximilian.png', region=(1273, 840, 188, 188), grayscale=True, confidence=0.8) != None:
            #sort 3 maximilian
            if pyautogui.locateOnScreen('../img/sort3_maximilian.png', region=(1640, 849, 166, 177), grayscale=True, confidence=0.83) != None:
                duree = uniform(0.06,0.1)
                x_sort3 = randint(1662, 1786)
                y_sort3 = randint(877, 1002)
                pyautogui.click(x_sort3, y_sort3, duration = duree)
                while pyautogui.locateOnScreen('../img/sort3_maximilian.png', region=(1640, 849, 166, 177), grayscale=True, confidence=0.83) != None:
                    ou_est_la_cible_emplacement_deux_ou_quatre()
            #sort 2 maximilian
            if pyautogui.locateOnScreen('../img/sort2_maximilian.png', region=(1462, 850, 171, 182), grayscale=True, confidence=0.7) != None:
                duree = uniform(0.06,0.1)
                x_sort2 = randint(1487, 1612)
                y_sort2 = randint(876, 1002)
                pyautogui.click(x_sort2, y_sort2, duration = duree)
                while pyautogui.locateOnScreen('../img/sort2_maximilian.png', region=(1462, 850, 171, 182), grayscale=True, confidence=0.7) != None:
                    ou_est_la_cible_emplacement_deux_ou_quatre()
            #sort 1 maximilian           
            elif pyautogui.locateOnScreen('../img/sort1_maximilian.png', region=(1273, 840, 188, 188), grayscale=True, confidence=0.8) != None:
                while pyautogui.locateOnScreen('../img/sort1_maximilian.png', region=(1273, 840, 188, 188), grayscale=True, confidence=0.8) != None:
                    ou_est_la_cible_emplacement_deux_ou_quatre()
        


        elif pyautogui.locateOnScreen('../img/victory_rta.png', region=(556, 110, 734, 177), confidence=0.85) != None:
            while (pyautogui.locateOnScreen('../img/victory_rta.png', region=(556, 110, 734, 177), confidence=0.85)):
                x_click = randint(75,1550)
                y_click = randint(139,219)
                duree = uniform(0.06,0.1)
                pyautogui.click(x_click,y_click,duration=duree)
                time_sleep = uniform(0.28,0.49)
                time.sleep(time_sleep)
            combat_finit = 1
            
        elif pyautogui.locateOnScreen('../img/defeated_rta.png', region = (605, 106, 641, 200), confidence = 0.55) != None:
            while (pyautogui.locateOnScreen('../img/defeated_rta.png', region=(605, 106, 641, 200), confidence = 0.55)):
                x_click = randint(75,1550)
                y_click = randint(139,219)
                duree = uniform(0.06,0.1)
                pyautogui.click(x_click,y_click,duration=duree)
                time_sleep = uniform(0.28,0.49)
                time.sleep(time_sleep)
            combat_finit = 1



def check_team_and_run_rivaux():
    if (pyautogui.locateOnScreen('../img/solo_maximilian.png', region=(379, 174, 446, 453), confidence=0.95) == None):
        while (pyautogui.locateOnScreen('../img/solo_maximilian_shortcut.png', region=(227, 565, 513, 161), confidence=0.95) == None):
            x_click = randint(110,170)
            y_click = randint(515,567)
            mouse.position = (x_click, y_click)
            duree = uniform(0.06,0.1)
            time.sleep(duree)
            mouse.press(Button.left)
            mouse.release(Button.left)

            time_sleep = uniform(0.42,0.45)
            time.sleep(time_sleep)

        # while (pyautogui.locateOnScreen('../img/solo_maximilian_shortcut.png', region=(227, 565, 513, 161), confidence=0.95) == None):
        #     time_sleep = uniform(0.22,0.31)
        #     time.sleep(time_sleep)

        x_click = randint(260,703)
        y_click = randint(599,693)
        mouse.position = (x_click, y_click)
        duree = uniform(0.06,0.1)
        time.sleep(duree)
        mouse.press(Button.left)
        mouse.release(Button.left)

        time_sleep = uniform(0.34,0.36)
        time.sleep(time_sleep)

        while (pyautogui.locateOnScreen('../img/solo_maximilian.png', region=(379, 174, 446, 453), confidence=0.95) == None):
            if (pyautogui.locateOnScreen('../img/solo_maximilian_shortcut.png', region=(227, 565, 513, 161), confidence=0.95)):
                x_click = randint(260,703)
                y_click = randint(599,693)
                mouse.position = (x_click, y_click)
                duree = uniform(0.06,0.1)
                time.sleep(duree)
                mouse.press(Button.left)
                mouse.release(Button.left)
            time_sleep = uniform(0.27,0.29)
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



def auto_rivaux():
    while (pyautogui.locateOnScreen('../img/haut_liste_rivaux.png', region=(501, 215, 344, 710), confidence=0.9) == None):
        x_click = randint(256,442)
        y_click = randint(353,418)
        duree = uniform(0.06,0.1)
        pyautogui.click(x_click,y_click,duration=duree)

        time_sleep = uniform(0.42,0.48)
        time.sleep(time_sleep)

    # premiere partie des rivaux
    while (len(list(pyautogui.locateAllOnScreen('../img/rival_available_part1.png', region=(1381, 376, 169, 526), confidence=0.9))) != 0):
        if (pyautogui.locateOnScreen('../img/rival_available_part1.png', region=(1381, 376, 169, 526), confidence=0.9)):
            pos_lead = pyautogui.locateOnScreen('../img/rival_available_part1.png', region=(1381, 376, 169, 526), confidence=0.9)
            x_click, y_click = pyautogui.center(pos_lead)
            x_click_add = randint(-64,60)
            y_click_add = randint(-25,28)
            x_click += x_click_add
            y_click += y_click_add
            mouse.position = (x_click, y_click)
            duree = uniform(0.06,0.1)
            time.sleep(duree)
            mouse.press(Button.left)
            mouse.release(Button.left)

            while (pyautogui.locateOnScreen('../img/in_arena2.png', region=(1368, 649, 354, 179), confidence=0.9) == None
                   and pyautogui.locateOnScreen('../img/pas_aile_rivaux.jpg', region=(491, 295, 887, 248), confidence=0.9) == None):
                time_sleep = uniform(0.22,0.31)
                time.sleep(time_sleep)
            
            if (pyautogui.locateOnScreen('../img/pas_aile_rivaux.jpg', region=(491, 295, 887, 248), confidence=0.9)):
                x_click = randint(1332,1394)
                y_click = randint(285,342)
                duree = uniform(0.06,0.1)
                pyautogui.click(x_click,y_click,duration=duree)
                return 0

            # time_sleep = uniform(0.82,0.93)
            # time.sleep(time_sleep)

            # changer team
            check_team_and_run_rivaux()

            # auto combat
            # click pour quitter ecran de fin
            auto_maximilian()

            while (pyautogui.locateOnScreen('../img/after_victory.png', region=(689, 84, 572, 175), confidence=0.9) == None):
                time_sleep = uniform(0.22,0.31)
                time.sleep(time_sleep)
            
            while (pyautogui.locateOnScreen('../img/haut_liste_rivaux.png', region=(503, 213, 351, 699), confidence=0.9) == None):
                time_sleep = uniform(0.22,0.31)
                time.sleep(time_sleep)

            # time_sleep = uniform(0.42,0.53)
            # time.sleep(time_sleep)

        # time_sleep = uniform(0.42,0.45)
        # time.sleep(time_sleep)

    # time_sleep = uniform(0.92,1.01)
    # time.sleep(time_sleep)

    if (pyautogui.locateOnScreen('../img/onglet_rival_selected.png', region=(237, 333, 227, 113), confidence=0.95) == None):
        while (pyautogui.locateOnScreen('../img/bas_liste_rivaux.png', region=(503, 213, 351, 699), confidence=0.9) == None):
            descend_liste()
            time_sleep = uniform(0.59,0.63)
            time.sleep(time_sleep)

        # time_sleep = uniform(0.92,1.01)
        # time.sleep(time_sleep)

        # deuxieme partie des rivaux
        while (len(list(pyautogui.locateAllOnScreen('../img/rival_available_part2.png', region=(1381, 211, 171, 676), confidence=0.9))) != 0):
            if (pyautogui.locateOnScreen('../img/rival_available_part2.png', region=(1381, 211, 171, 676), confidence=0.9)):
                pos_lead = pyautogui.locateOnScreen('../img/rival_available_part2.png', region=(1381, 211, 171, 676), confidence=0.9)
                x_click, y_click = pyautogui.center(pos_lead)
                x_click_add = randint(-63,51)
                y_click_add = randint(-27,17)
                x_click += x_click_add
                y_click += y_click_add
                mouse.position = (x_click, y_click)
                duree = uniform(0.06,0.1)
                time.sleep(duree)
                mouse.press(Button.left)
                mouse.release(Button.left)

                while (pyautogui.locateOnScreen('../img/in_arena2.png', region=(1368, 649, 354, 179), confidence=0.9) == None
                        and pyautogui.locateOnScreen('../img/pas_aile_rivaux.jpg', region=(491, 295, 887, 248), confidence=0.9) == None):
                    time_sleep = uniform(0.22,0.31)
                    time.sleep(time_sleep)

                if (pyautogui.locateOnScreen('../img/pas_aile_rivaux.jpg', region=(491, 295, 887, 248), confidence=0.9)):
                    x_click = randint(1332,1394)
                    y_click = randint(285,342)
                    duree = uniform(0.06,0.1)
                    pyautogui.click(x_click,y_click,duration=duree)
                    return 0

                # time_sleep = uniform(0.82,0.93)
                # time.sleep(time_sleep)

                # changer team
                check_team_and_run_rivaux()

                # auto combat
                # click pour quitter ecran de fin
                auto_maximilian()

                while (pyautogui.locateOnScreen('../img/after_victory.png', region=(689, 84, 572, 175), confidence=0.9) == None):
                    time_sleep = uniform(0.22,0.31)
                    time.sleep(time_sleep)

                while (pyautogui.locateOnScreen('../img/bas_liste_rivaux.png', region=(503, 213, 351, 699), confidence=0.9) == None):
                    if (pyautogui.locateOnScreen('../img/haut_liste_rivaux.png', region=(501, 215, 344, 710), confidence=0.9)):
                        if (pyautogui.locateOnScreen('../img/onglet_rival_selected.png', region=(237, 333, 227, 113), confidence=0.95)):
                            break
                        while (pyautogui.locateOnScreen('../img/bas_liste_rivaux.png', region=(503, 213, 351, 699), confidence=0.9) == None):
                            descend_liste()
                            time_sleep = uniform(0.59,0.63)
                            time.sleep(time_sleep)

                    time_sleep = uniform(0.59,0.63)
                    time.sleep(time_sleep)

                if (pyautogui.locateOnScreen('../img/onglet_rival_selected.png', region=(237, 333, 227, 113), confidence=0.95)):
                    break


                # time_sleep = uniform(0.54,0.57)
                # time.sleep(time_sleep)

            # time_sleep = uniform(0.42,0.45)
            # time.sleep(time_sleep)

    return 1

def auto_rivaux_collab():
    while (pyautogui.locateOnScreen('../img/haut_liste_rivaux_collab.png', region=(501, 215, 344, 710), confidence=0.9) == None):
        x_click = randint(256,442)
        y_click = randint(353,418)
        duree = uniform(0.06,0.1)
        pyautogui.click(x_click,y_click,duration=duree)

        time_sleep = uniform(0.42,0.48)
        time.sleep(time_sleep)

    #lance le rival de la collab
    if (pyautogui.locateOnScreen('../img/rival_available_part1.png', region=(1372, 229, 193, 151), confidence=0.9)):
        pos_lead = pyautogui.locateOnScreen('../img/rival_available_part1.png', region=(1372, 229, 193, 151), confidence=0.9)
        x_click, y_click = pyautogui.center(pos_lead)
        x_click_add = randint(-64,60)
        y_click_add = randint(-25,28)
        x_click += x_click_add
        y_click += y_click_add
        mouse.position = (x_click, y_click)
        duree = uniform(0.06,0.1)
        time.sleep(duree)
        mouse.press(Button.left)
        mouse.release(Button.left)

        while (pyautogui.locateOnScreen('../img/in_arena2.png', region=(1368, 649, 354, 179), confidence=0.9) == None):
            time_sleep = uniform(0.22,0.31)
            time.sleep(time_sleep)

        # changer team
        check_team_and_run_rivaux()

        # auto combat
        auto_maximilian()

        while (pyautogui.locateOnScreen('../img/after_victory.png', region=(689, 84, 572, 175), confidence=0.9) == None):
            time_sleep = uniform(0.22,0.31)
            time.sleep(time_sleep)

    # premiere partie des rivaux
    while (len(list(pyautogui.locateAllOnScreen('../img/rival_available_part1.png', region=(1378, 518, 183, 393), confidence=0.9))) != 0):
        if (pyautogui.locateOnScreen('../img/rival_available_part1.png', region=(1378, 518, 183, 393), confidence=0.9)):
            pos_lead = pyautogui.locateOnScreen('../img/rival_available_part1.png', region=(1378, 518, 183, 393), confidence=0.9)
            x_click, y_click = pyautogui.center(pos_lead)
            x_click_add = randint(-64,60)
            y_click_add = randint(-25,28)
            x_click += x_click_add
            y_click += y_click_add
            mouse.position = (x_click, y_click)
            duree = uniform(0.06,0.1)
            time.sleep(duree)
            mouse.press(Button.left)
            mouse.release(Button.left)

            while (pyautogui.locateOnScreen('../img/in_arena2.png', region=(1368, 649, 354, 179), confidence=0.9) == None):
                time_sleep = uniform(0.22,0.31)
                time.sleep(time_sleep)

            # changer team
            check_team_and_run_rivaux()

            # auto combat
            auto_maximilian()

            while (pyautogui.locateOnScreen('../img/after_victory.png', region=(689, 84, 572, 175), confidence=0.9) == None):
                time_sleep = uniform(0.22,0.31)
                time.sleep(time_sleep)

        # time_sleep = uniform(0.42,0.45)
        # time.sleep(time_sleep)

    # time_sleep = uniform(0.92,1.01)
    # time.sleep(time_sleep)

    if (pyautogui.locateOnScreen('../img/onglet_rival_selected.png', region=(237, 333, 227, 113), confidence=0.95) == None):
        # descend la liste jusqu'a arriver au milieu
        while (pyautogui.locateOnScreen('../img/milieu_liste_rivaux.png', region=(503, 213, 351, 699), confidence=0.9) == None
               and pyautogui.locateOnScreen('../img/bas_liste_rivaux.png', region=(463, 654, 433, 311), confidence=0.9) == None):
            descend_liste()
            time_sleep = uniform(0.62,0.65)
            time.sleep(time_sleep)

        # partie du milieu des rivaux
        while (len(list(pyautogui.locateAllOnScreen('../img/rival_available_part2.png', region=(1381, 211, 171, 676), confidence=0.9))) != 0):
            if (pyautogui.locateOnScreen('../img/rival_available_part2.png', region=(1381, 211, 171, 676), confidence=0.9)):
                pos_lead = pyautogui.locateOnScreen('../img/rival_available_part2.png', region=(1381, 211, 171, 676), confidence=0.9)
                x_click, y_click = pyautogui.center(pos_lead)
                x_click_add = randint(-63,51)
                y_click_add = randint(-27,17)
                x_click += x_click_add
                y_click += y_click_add
                mouse.position = (x_click, y_click)
                duree = uniform(0.06,0.1)
                time.sleep(duree)
                mouse.press(Button.left)
                mouse.release(Button.left)

                while (pyautogui.locateOnScreen('../img/in_arena2.png', region=(1368, 649, 354, 179), confidence=0.9) == None):
                    time_sleep = uniform(0.22,0.31)
                    time.sleep(time_sleep)

                # changer team
                check_team_and_run_rivaux()

                # auto combat
                auto_maximilian()

                while (pyautogui.locateOnScreen('../img/after_victory.png', region=(689, 84, 572, 175), confidence=0.9) == None):
                    time_sleep = uniform(0.22,0.31)
                    time.sleep(time_sleep)

        if (pyautogui.locateOnScreen('../img/onglet_rival_selected.png', region=(237, 333, 227, 113), confidence=0.95) == None):
            while (pyautogui.locateOnScreen('../img/bas_liste_rivaux.png', region=(463, 654, 433, 311), confidence=0.9) == None):
                descend_liste()
                time_sleep = uniform(0.62,0.65)
                time.sleep(time_sleep)

            # time_sleep = uniform(0.92,1.01)
            # time.sleep(time_sleep)

            # deuxieme partie des rivaux
            while (len(list(pyautogui.locateAllOnScreen('../img/rival_available_part2.png', region=(1381, 211, 171, 676), confidence=0.9))) != 0):
                if (pyautogui.locateOnScreen('../img/rival_available_part2.png', region=(1381, 211, 171, 676), confidence=0.9)):
                    pos_lead = pyautogui.locateOnScreen('../img/rival_available_part2.png', region=(1381, 211, 171, 676), confidence=0.9)
                    x_click, y_click = pyautogui.center(pos_lead)
                    x_click_add = randint(-63,51)
                    y_click_add = randint(-27,17)
                    x_click += x_click_add
                    y_click += y_click_add
                    mouse.position = (x_click, y_click)
                    duree = uniform(0.06,0.1)
                    time.sleep(duree)
                    mouse.press(Button.left)
                    mouse.release(Button.left)

                    while (pyautogui.locateOnScreen('../img/in_arena2.png', region=(1368, 649, 354, 179), confidence=0.9) == None):
                        time_sleep = uniform(0.22,0.31)
                        time.sleep(time_sleep)

                    # time_sleep = uniform(0.82,0.93)
                    # time.sleep(time_sleep)

                    # changer team
                    check_team_and_run_rivaux()

                    # auto combat
                    # click pour quitter ecran de fin
                    auto_maximilian()

                    while (pyautogui.locateOnScreen('../img/after_victory.png', region=(689, 84, 572, 175), confidence=0.9) == None):
                        time_sleep = uniform(0.22,0.31)
                        time.sleep(time_sleep)

                    # time_sleep = uniform(0.54,0.57)
                    # time.sleep(time_sleep)

                # time_sleep = uniform(0.42,0.45)
                # time.sleep(time_sleep)
