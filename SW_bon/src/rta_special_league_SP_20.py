import pyautogui
import time
from random import *
from pynput.mouse import Button, Controller
from rta import ou_est_la_cible_emplacement_deux_ou_quatre_rta

mouse = Controller()

def lance_sorts_en_rta_special_league_20_stars():
    time_sleep = uniform(0.28,0.49)
    time.sleep(time_sleep)
    combat_finit = 0
    while  combat_finit == 0:
        # time_sleep = uniform(0.0010,0.0030)
        # time.sleep(time_sleep)
        #auto Clara
        if pyautogui.locateOnScreen('../img/sort1_clara.png', region=(1273, 840, 188, 188), confidence=0.70) != None:
            time_sleep = uniform(0.38,0.59)
            time.sleep(time_sleep)
            #sort 3 Clara
            if pyautogui.locateOnScreen('../img/sort3_clara.png', region=(1640, 849, 166, 177), confidence=0.7) != None:
                duree = uniform(0.06,0.1)
                x_sort3 = randint(1662, 1786)
                y_sort3 = randint(877, 1002)
                pyautogui.click(x_sort3, y_sort3, duration = duree)
                while pyautogui.locateOnScreen('../img/sort3_clara.png', region=(1640, 849, 166, 177), confidence=0.70) != None:
                    ou_est_la_cible_emplacement_deux_ou_quatre_rta()
            #sort 2 Clara
            if pyautogui.locateOnScreen('../img/sort2_clara.png', region=(1462, 850, 171, 182), confidence=0.85) != None:
                duree = uniform(0.06,0.1)
                x_sort2 = randint(1487, 1612)
                y_sort2 = randint(876, 1002)
                pyautogui.click(x_sort2, y_sort2, duration = duree)
                while pyautogui.locateOnScreen('../img/sort2_clara.png', region=(1462, 850, 171, 182), confidence=0.70) != None:
                    ou_est_la_cible_emplacement_deux_ou_quatre_rta()
            #sort 1 Clara           
            if pyautogui.locateOnScreen('../img/sort1_clara.png', region=(1273, 840, 188, 188), confidence=0.70) != None:
                while pyautogui.locateOnScreen('../img/sort1_clara.png', region=(1273, 840, 188, 188), confidence=0.70) != None:
                    ou_est_la_cible_emplacement_deux_ou_quatre_rta()

        #auto Shimitae
        elif pyautogui.locateOnScreen('../img/sort1_shimitae.png', region=(1273, 840, 188, 188), confidence=0.70) != None:
            time_sleep = uniform(0.38,0.59)
            time.sleep(time_sleep)
            #sort 2 Shimitae
            if pyautogui.locateOnScreen('../img/sort2_shimitae.png', region=(1462, 850, 171, 182), confidence=0.85) != None:
                duree = uniform(0.06,0.1)
                x_sort2 = randint(1487, 1612)
                y_sort2 = randint(876, 1002)
                pyautogui.click(x_sort2, y_sort2, duration = duree)
                while pyautogui.locateOnScreen('../img/sort2_shimitae.png', region=(1462, 850, 171, 182), confidence=0.70) != None:
                    ou_est_la_cible_emplacement_deux_ou_quatre_rta()
            #sort 3 Shimitae
            if pyautogui.locateOnScreen('../img/sort3_shimitae.png', region=(1640, 849, 166, 177), confidence=0.85) != None:
                duree = uniform(0.06,0.1)
                x_sort3 = randint(1662, 1786)
                y_sort3 = randint(877, 1002)
                pyautogui.click(x_sort3, y_sort3, duration = duree)
                while pyautogui.locateOnScreen('../img/sort3_shimitae.png', region=(1640, 849, 166, 177), confidence=0.70) != None:
                    ou_est_la_cible_emplacement_deux_ou_quatre_rta()
            #sort 1 Shimitae           
            if pyautogui.locateOnScreen('../img/sort1_shimitae.png', region=(1273, 840, 188, 188), confidence=0.70) != None:
                while pyautogui.locateOnScreen('../img/sort1_shimitae.png', region=(1273, 840, 188, 188), confidence=0.70) != None:
                    ou_est_la_cible_emplacement_deux_ou_quatre_rta()

        #auto Maximilian    
        elif pyautogui.locateOnScreen('../img/sort1_maximilian.png', region=(1273, 840, 188, 188), confidence=0.70) != None:
            time_sleep = uniform(0.38,0.59)
            time.sleep(time_sleep)
            #sort 3 Maximilian
            if pyautogui.locateOnScreen('../img/sort3_maximilian.png', region=(1640, 849, 166, 177), confidence=0.85) != None:
                duree = uniform(0.06,0.1)
                x_sort3 = randint(1662, 1786)
                y_sort3 = randint(877, 1002)
                pyautogui.click(x_sort3, y_sort3, duration = duree)
                while pyautogui.locateOnScreen('../img/sort3_maximilian.png', region=(1640, 849, 166, 177), confidence=0.70) != None:
                    ou_est_la_cible_emplacement_deux_ou_quatre_rta()
            #sort 2 Maximilian
            if pyautogui.locateOnScreen('../img/sort2_maximilian.png', region=(1462, 850, 171, 182), confidence=0.85) != None:
                duree = uniform(0.06,0.1)
                x_sort2 = randint(1487, 1612)
                y_sort2 = randint(876, 1002)
                pyautogui.click(x_sort2, y_sort2, duration = duree)
                while pyautogui.locateOnScreen('../img/sort2_maximilian.png', region=(1462, 850, 171, 182), confidence=0.70) != None:
                    ou_est_la_cible_emplacement_deux_ou_quatre_rta()
            #sort 1 Maximilian           
            if pyautogui.locateOnScreen('../img/sort1_maximilian.png', region=(1273, 840, 188, 188), confidence=0.70) != None:
                while pyautogui.locateOnScreen('../img/sort1_maximilian.png', region=(1273, 840, 188, 188), confidence=0.70) != None:
                    ou_est_la_cible_emplacement_deux_ou_quatre_rta()

        # auto dark robo
        elif pyautogui.locateOnScreen('../img/sort1_dark_robo.png', region=(1273, 840, 188, 188), confidence=0.70) != None:
            time_sleep = uniform(0.38,0.59)
            time.sleep(time_sleep)
            #sort 2 dark robo
            if pyautogui.locateOnScreen('../img/sort2_dark_robo.png', region=(1462, 850, 171, 182), confidence=0.85) != None:
                duree = uniform(0.06,0.1)
                x_sort2 = randint(1487, 1612)
                y_sort2 = randint(876, 1002)
                pyautogui.click(x_sort2, y_sort2, duration = duree)
                while pyautogui.locateOnScreen('../img/sort2_dark_robo.png', region=(1462, 850, 171, 182), confidence=0.70) != None:
                    ou_est_la_cible_emplacement_deux_ou_quatre_rta()
            #sort 3 dark robo
            if pyautogui.locateOnScreen('../img/sort3_dark_robo.png', region=(1640, 849, 166, 177), confidence=0.85) != None:
                duree = uniform(0.06,0.1)
                x_sort3 = randint(1662, 1786)
                y_sort3 = randint(877, 1002)
                pyautogui.click(x_sort3, y_sort3, duration = duree)
                while pyautogui.locateOnScreen('../img/sort3_dark_robo.png', region=(1640, 849, 166, 177), confidence=0.70) != None:
                    ou_est_la_cible_emplacement_deux_ou_quatre_rta()
            #sort 1 dark robo           
            if pyautogui.locateOnScreen('../img/sort1_dark_robo.png', region=(1273, 840, 188, 188), confidence=0.70) != None:
                while pyautogui.locateOnScreen('../img/sort1_dark_robo.png', region=(1273, 840, 188, 188), confidence=0.70) != None:
                    ou_est_la_cible_emplacement_deux_ou_quatre_rta()

        # auto Prom
        elif pyautogui.locateOnScreen('../img/sort1_prom.png', region=(1273, 840, 188, 188), confidence=0.70) != None:
            time_sleep = uniform(0.38,0.59)
            time.sleep(time_sleep)
            #sort 3 Prom
            if pyautogui.locateOnScreen('../img/sort3_prom.png', region=(1640, 849, 166, 177), confidence=0.85) != None:
                duree = uniform(0.06,0.1)
                x_sort3 = randint(1662, 1786)
                y_sort3 = randint(877, 1002)
                pyautogui.click(x_sort3, y_sort3, duration = duree)
                while pyautogui.locateOnScreen('../img/sort3_prom.png', region=(1640, 849, 166, 177), confidence=0.70) != None:
                    ou_est_la_cible_emplacement_deux_ou_quatre_rta()
            #sort 2 Prom
            if pyautogui.locateOnScreen('../img/sort2_prom.png', region=(1462, 850, 171, 182), confidence=0.85) != None:
                duree = uniform(0.06,0.1)
                x_sort2 = randint(1487, 1612)
                y_sort2 = randint(876, 1002)
                pyautogui.click(x_sort2, y_sort2, duration = duree)
                while pyautogui.locateOnScreen('../img/sort2_prom.png', region=(1462, 850, 171, 182), confidence=0.70) != None:
                    ou_est_la_cible_emplacement_deux_ou_quatre_rta()
            #sort 1 Prom           
            if pyautogui.locateOnScreen('../img/sort1_prom.png', region=(1273, 840, 188, 188), confidence=0.70) != None:
                while pyautogui.locateOnScreen('../img/sort1_prom.png', region=(1273, 840, 188, 188), confidence=0.70) != None:
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
            
        elif pyautogui.locateOnScreen('../img/defeated_rta.png', region = (605, 106, 641, 200), confidence = 0.55) != None:
            while (pyautogui.locateOnScreen('../img/defeated_rta.png', region=(605, 106, 641, 200), confidence = 0.55)):
                x_click = randint(314,1374)
                y_click = randint(386,840)
                duree = uniform(0.06,0.1)
                pyautogui.click(x_click,y_click,duration=duree)
                time_sleep = uniform(0.28,0.49)
                time.sleep(time_sleep)
            combat_finit = 1
        check_opponent_quit()


def quitter_combat_rta():
    while (pyautogui.locateOnScreen('../img/croix_rta.png', region=(1695, 19, 130, 107), confidence=0.95) == None):
        time_sleep = uniform(0.02,0.09)
        time.sleep(time_sleep)
    x_click = randint(1742,1786)
    y_click = randint(60,99)
    duree = uniform(0.06,0.1)
    pyautogui.click(x_click,y_click,duration=duree)

    while (pyautogui.locateOnScreen('../img/oui_quit_rta.png', region=(642, 619, 290, 150), confidence=0.95) == None):
        time_sleep = uniform(0.02,0.09)
        time.sleep(time_sleep)
    x_click = randint(673,891)
    y_click = randint(650,739)
    duree = uniform(0.06,0.1)
    pyautogui.click(x_click,y_click,duration=duree)

def check_opponent_quit():
    if (pyautogui.locateOnScreen('../img/opponent_quit.png', region=(403, 255, 1070, 551),confidence=0.9)):
        while (pyautogui.locateOnScreen('../img/commencer_rta.png', region=(1215, 792, 413, 178), confidence=0.9) == None):
            x_click = randint(829,1043)
            y_click = randint(595,679)
            duree = uniform(0.06,0.1)
            pyautogui.click(x_click,y_click,duration=duree)
            time_sleep = uniform(0.42,0.47)
            time.sleep(time_sleep)
        rta_special_league_boucle_20_stars()


def rta_special_league_boucle_20_stars():
    # Check si l'adversaire quitte le combat pendant la draft ou si l'un des 5 monstres est pris en fasse et quitter
    end = 0
    while (end == 0):
        quit = 2
        while (quit == 2):
            if (pyautogui.locateOnScreen('../img/silver_1_rta_SP_20.png', region=(554, 265, 169, 91), confidence=0.95)):
                quit = 1
            if (pyautogui.locateOnScreen('../img/bronze_3_rta_SP_20.png', region=(554, 265, 169, 91), confidence=0.95)):
                quit = 1
            if (pyautogui.locateOnScreen('../img/bronze_2_rta_SP_20.png', region=(554, 265, 169, 91), confidence=0.95)):
                quit = 0
            if (pyautogui.locateOnScreen('../img/adversaire_quitte_rta.png', region=(391, 247, 1085, 563), confidence=0.95)):
                x_click = randint(826,1047)
                y_click = randint(591,681)
                duree = uniform(0.06,0.1)
                pyautogui.click(x_click,y_click,duration=duree)
            time_sleep = uniform(0.02,0.09)
            time.sleep(time_sleep)
        
        while (pyautogui.locateOnScreen('../img/commencer_rta.png', region=(1215, 792, 413, 178), confidence=0.9)):
            x_click = randint(1251,1595)
            y_click = randint(834,938)
            duree = uniform(0.06,0.1)
            pyautogui.click(x_click,y_click,duration=duree)

            time_sleep = uniform(0.72,0.86)
            time.sleep(time_sleep)

            if (pyautogui.locateOnScreen('../img/fin_rta_SP.png', region=(408, 260, 1056, 538), confidence=0.95)):
                print("plus de rta mec")
                exit(0)

        if (quit == 1):
            quitter_combat_rta()
        
        if (quit == 0):
            # choisis les monstres
            while (pyautogui.locateOnScreen('../img/choisis_ton_monstre.png', region=(585, 33, 468, 121), confidence=0.95) == None):
                check_opponent_quit()
                time_sleep = uniform(0.02,0.09)
                time.sleep(time_sleep)
            
            time_sleep = uniform(0.77,0.89)
            time.sleep(time_sleep)

            if (pyautogui.locateOnScreen('../img/first_pick_rta.png', region=(388, 188, 391, 388), confidence=0.95)):
                first_pick = 1
            else:
                first_pick = 0
            
            # first pick
            time_sleep = uniform(0.42,0.48)
            time.sleep(time_sleep)
            while (pyautogui.locateOnScreen('../img/not_ok_rta.png', region=(1025, 46, 196, 102), confidence=0.97)):
                # time_sleep = uniform(0.02,0.09)
                # time.sleep(time_sleep)
                check_opponent_quit()
                if (pyautogui.locateOnScreen('../img/monster_picked.png', region=(95, 700, 446, 308), grayscale=True,confidence=0.55)):
                    quitter_combat_rta()
                    rta_special_league_boucle_20_stars()
                if (first_pick == 1):
                    if (pyautogui.locateOnScreen('../img/clara_40_icon.png', region=(95, 700, 446, 308), confidence=0.95)):
                        x_pos_mob = pyautogui.locateOnScreen('../img/clara_40_icon.png', region=(95, 700, 446, 308), confidence=0.95)
                        x_click, y_click = pyautogui.center(x_pos_mob)
                        x_click_add = randint(-40,40)
                        y_click_add = randint(-40,40)
                        x_click += x_click_add
                        y_click += y_click_add
                        duree = uniform(0.06,0.1)
                        pyautogui.click(x_click,y_click,duration=duree)

                        time_sleep = uniform(0.22,0.39)
                        time.sleep(time_sleep)
                    # if symbole mob utilisé alors quitter combat (quitter_combat_rta())
                else:
                    if (pyautogui.locateOnScreen('../img/clara_40_icon.png', region=(95, 700, 446, 308), confidence=0.95)):
                        x_pos_mob = pyautogui.locateOnScreen('../img/clara_40_icon.png', region=(95, 700, 446, 308), confidence=0.95)
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

            # time_sleep = uniform(0.27,0.31)
            # time.sleep(time_sleep)

            # click sur ok
            while (pyautogui.locateOnScreen('../img/choisis_ton_monstre.png', region=(585, 33, 468, 121), confidence=0.8)):
                check_opponent_quit()
                x_click = randint(1050,1202)
                y_click = randint(65,122)
                duree = uniform(0.06,0.1)
                pyautogui.click(x_click,y_click,duration=duree)
                time_sleep = uniform(0.22,0.31)
                time.sleep(time_sleep)

            while (pyautogui.locateOnScreen('../img/choisis_ton_monstre.png', region=(585, 33, 468, 121), confidence=0.8) == None):
                check_opponent_quit()
                time_sleep = uniform(0.02,0.09)
                time.sleep(time_sleep)

            # second pick
            time_sleep = uniform(0.42,0.48)
            time.sleep(time_sleep)
            while (pyautogui.locateOnScreen('../img/not_ok_rta.png', region=(1025, 46, 196, 102), confidence=0.97)):
                # time_sleep = uniform(0.02,0.09)
                # time.sleep(time_sleep)
                check_opponent_quit()
                if (pyautogui.locateOnScreen('../img/monster_picked.png', region=(95, 700, 446, 308), grayscale=True,confidence=0.55)):
                    quitter_combat_rta()
                    rta_special_league_boucle_20_stars()
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

                    
                    if (pyautogui.locateOnScreen('../img/dark_robo_40_icon.png', region=(95, 700, 446, 308), confidence=0.95)):
                        x_pos_mob = pyautogui.locateOnScreen('../img/dark_robo_40_icon.png', region=(95, 700, 446, 308), confidence=0.95)
                        x_click, y_click = pyautogui.center(x_pos_mob)
                        x_click_add = randint(-40,40)
                        y_click_add = randint(-40,40)
                        x_click += x_click_add
                        y_click += y_click_add
                        duree = uniform(0.06,0.1)
                        pyautogui.click(x_click,y_click,duration=duree)

                        time_sleep = uniform(0.22,0.39)
                        time.sleep(time_sleep)

                    # if symbole mob utilisé alors quitter combat (quitter_combat_rta())
                else:
                    if (pyautogui.locateOnScreen('../img/dark_robo_40_icon.png', region=(95, 700, 446, 308), confidence=0.95)):
                        x_pos_mob = pyautogui.locateOnScreen('../img/dark_robo_40_icon.png', region=(95, 700, 446, 308), confidence=0.95)
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

                # si l'adversaire a quitté
                if (pyautogui.locateOnScreen('../img/opponent_quit.png', region=(403, 255, 1070, 551),confidence=0.9)):
                    while (pyautogui.locateOnScreen('../img/combat_amical.png', region=(1332, 540, 476, 245), confidence=0.9) == None):
                        x_click = randint(829,1043)
                        y_click = randint(595,679)
                        duree = uniform(0.06,0.1)
                        pyautogui.click(x_click,y_click,duration=duree)
                        time_sleep = uniform(0.52,0.59)
                        time.sleep(time_sleep)
                    rta_special_league_boucle_20_stars()

            # time_sleep = uniform(0.27,0.31)
            # time.sleep(time_sleep)

            # click sur ok
            while (pyautogui.locateOnScreen('../img/choisis_ton_monstre.png', region=(585, 33, 468, 121), confidence=0.8)):
                check_opponent_quit()
                x_click = randint(1050,1202)
                y_click = randint(65,122)
                duree = uniform(0.06,0.1)
                pyautogui.click(x_click,y_click,duration=duree)
                time_sleep = uniform(0.12,0.26)
                time.sleep(time_sleep)

            while (pyautogui.locateOnScreen('../img/choisis_ton_monstre.png', region=(585, 33, 468, 121), confidence=0.8) == None):
                check_opponent_quit()
                time_sleep = uniform(0.02,0.09)
                time.sleep(time_sleep)

            #last pick
            time_sleep = uniform(0.42,0.48)
            time.sleep(time_sleep)
            while (pyautogui.locateOnScreen('../img/not_ok_rta.png', region=(1025, 46, 196, 102), confidence=0.97)):
                # time_sleep = uniform(0.02,0.09)
                # time.sleep(time_sleep)
                check_opponent_quit()
                if (pyautogui.locateOnScreen('../img/monster_picked.png', region=(95, 700, 446, 308), grayscale=True,confidence=0.55)):
                    quitter_combat_rta()
                    rta_special_league_boucle_20_stars()
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
                    
                    if (pyautogui.locateOnScreen('../img/prom_40_icon.png', region=(95, 700, 446, 308), confidence=0.95)):
                        x_pos_mob = pyautogui.locateOnScreen('../img/prom_40_icon.png', region=(95, 700, 446, 308), confidence=0.95)
                        x_click, y_click = pyautogui.center(x_pos_mob)
                        x_click_add = randint(-40,40)
                        y_click_add = randint(-40,40)
                        x_click += x_click_add
                        y_click += y_click_add
                        duree = uniform(0.06,0.1)
                        pyautogui.click(x_click,y_click,duration=duree)

                        time_sleep = uniform(0.22,0.39)
                        time.sleep(time_sleep)

                    # if symbole mob utilisé alors quitter combat (quitter_combat_rta())
                else:
                    if (pyautogui.locateOnScreen('../img/prom_40_icon.png', region=(95, 700, 446, 308), confidence=0.95)):
                        x_pos_mob = pyautogui.locateOnScreen('../img/prom_40_icon.png', region=(95, 700, 446, 308), confidence=0.95)
                        x_click, y_click = pyautogui.center(x_pos_mob)
                        x_click_add = randint(-40,40)
                        y_click_add = randint(-40,40)
                        x_click += x_click_add
                        y_click += y_click_add
                        duree = uniform(0.06,0.1)
                        pyautogui.click(x_click,y_click,duration=duree)

                        time_sleep = uniform(0.22,0.39)
                        time.sleep(time_sleep)

                    # if symbole mob utilisé alors quitter combat (quitter_combat_rta())

            # time_sleep = uniform(0.27,0.31)
            # time.sleep(time_sleep)

            # click sur ok
            while (pyautogui.locateOnScreen('../img/choisis_ton_monstre.png', region=(585, 33, 468, 121), confidence=0.8)):
                check_opponent_quit()
                x_click = randint(1050,1202)
                y_click = randint(65,122)
                duree = uniform(0.06,0.1)
                pyautogui.click(x_click,y_click,duration=duree)
                time_sleep = uniform(0.22,0.31)
                time.sleep(time_sleep)


            # bannis le monstre

            while (pyautogui.locateOnScreen('../img/bannis_monstre.png', region=(452, 23, 744, 137), confidence=0.8) == None):
                check_opponent_quit()
                time_sleep = uniform(0.02,0.09)
                time.sleep(time_sleep)

            x_click = randint(1326, 1346)
            y_click = randint(322, 342)

            mouse.position = (x_click, y_click)

            time_sleep = uniform(1.02,1.21)
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

            time_sleep = uniform(0.37,0.41)
            time.sleep(time_sleep)

            while (pyautogui.locateOnScreen('../img/bannis_monstre.png', region=(453, 24, 738, 140), confidence=0.95)):
                if (pyautogui.locateOnScreen('../img/not_ok_rta.png', region=(1152, 32, 200, 120), confidence=0.97) == None):
                    x_click = randint(1180,1330)
                    y_click = randint(66,121)
                    duree = uniform(0.06,0.1)
                    pyautogui.click(x_click,y_click,duration=duree)
                    time_sleep = uniform(0.22,0.31)
                    time.sleep(time_sleep)
                time_sleep = uniform(0.22,0.31)
                time.sleep(time_sleep)

            # choisis le lead

            time_sleep = uniform(1.02,1.21)
            time.sleep(time_sleep)

            if (pyautogui.locateOnScreen('../img/shimitae_40_icon2.png', region=(255, 198, 559, 371), confidence=0.9)):
                pos_lead = pyautogui.locateOnScreen('../img/shimitae_40_icon2.png', region=(255, 198, 559, 371), confidence=0.9)
                x_click, y_click = pyautogui.center(pos_lead)

                time_sleep = uniform(1.02,1.21)
                time.sleep(time_sleep)

            if (pyautogui.locateOnScreen('../img/maximilian_40_icon2.png', region=(255, 198, 559, 371), confidence=0.9)):
                pos_lead = pyautogui.locateOnScreen('../img/maximilian_40_icon2.png', region=(255, 198, 559, 371), confidence=0.9)
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


            time_sleep = uniform(0.37,0.41)
            time.sleep(time_sleep)

            while (pyautogui.locateOnScreen('../img/choisis_leader.png', region=(534, 25, 575, 141), confidence=0.95)):
                if (pyautogui.locateOnScreen('../img/not_ok_rta.png', region=(1079, 48, 189, 93), confidence=0.97) == None):
                    x_click = randint(1097,1246)
                    y_click = randint(69,120)
                    duree = uniform(0.06,0.1)
                    pyautogui.click(x_click,y_click,duration=duree)
                    time_sleep = uniform(0.22,0.31)
                    time.sleep(time_sleep)
                time_sleep = uniform(0.22,0.31)
                time.sleep(time_sleep)

            lance_sorts_en_rta_special_league_20_stars()

            time_sleep = uniform(0.82,0.93)
            time.sleep(time_sleep)

        # time_sleep = uniform(0.02,0.09)
        # time.sleep(time_sleep)
            
            