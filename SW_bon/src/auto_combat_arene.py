import pyautogui
import time
from random import *
from PIL import ImageGrab

def ou_est_la_cible_emplacement_deux_ou_quatre_allies_team():
        fIn = 0
        si_trois_emplacement_vide = 4*[0]
        while fIn == 0:
            empla_vide = 0
            cHoix = randint(0,3)
            if cHoix == 0 and si_trois_emplacement_vide[0] == 0:    
                if pyautogui.locateOnScreen('../img/emplacement_vide1_allies.png', region=(229, 597, 253, 321), grayscale=True, confidence=0.95) == None:
                    x_cible1_arene = randint(271,451)
                    y_cible1_arene = randint(712,846)
                    duree = uniform(0.06,0.1)
                    pyautogui.click(x_cible1_arene,y_cible1_arene,duration=duree)
                    fIn = 1
                else:
                    si_trois_emplacement_vide[0] = 1
                    
            if cHoix == 1 and si_trois_emplacement_vide[1] == 0:               
                if pyautogui.locateOnScreen('../img/emplacement_vide2_allies.png', region=(523, 648, 244, 295), grayscale=True, confidence=0.95) == None:
                    x_cible1_arene = randint(552,726)
                    y_cible1_arene = randint(696,902)
                    duree = uniform(0.06,0.1)
                    pyautogui.click(x_cible1_arene,y_cible1_arene,duration=duree)
                    fIn = 1
                else:
                    si_trois_emplacement_vide[1] = 1

            if cHoix == 2 and si_trois_emplacement_vide[2] == 0:
                if pyautogui.locateOnScreen('../img/emplacement_vide3_allies.png', region=(840, 600, 250, 378), grayscale=True, confidence=0.95) == None:

                    x_cible1_arene = randint(871,1051)
                    y_cible1_arene = randint(713,930)
                    duree = uniform(0.06,0.1)
                    pyautogui.click(x_cible1_arene,y_cible1_arene,duration=duree)
                    fIn = 1
                else:
                    si_trois_emplacement_vide[2] = 1

            for i in range(len(si_trois_emplacement_vide)):
                empla_vide = empla_vide + si_trois_emplacement_vide[i]

            if cHoix == 3 and si_trois_emplacement_vide[3] == 0:
                if pyautogui.locateOnScreen('../img/emplacement_vide4_allies.png', region=(1071, 585, 370, 358), grayscale=True, confidence=0.95) == None:
                    x_cible1_arene = randint(1192,1368)
                    y_cible1_arene = randint(772,843)
                    duree = uniform(0.06,0.1)
                    pyautogui.click(x_cible1_arene,y_cible1_arene,duration=duree)
                    fIn = 1
                else:
                    si_trois_emplacement_vide[3] = 1

def ou_est_la_cible_emplacement_deux_ou_quatre():
    fIn = 0
    si_trois_emplacement_vide = 4*[0]
    while fIn == 0:
        empla_vide = 0
        cHoix = randint(0,3)
        if cHoix == 0 and si_trois_emplacement_vide[0] == 0:    
            if pyautogui.locateOnScreen('../img/emplacement_vide1.png', region=(497, 178, 227, 276), grayscale=True, confidence=0.95) == None:
                x_cible1_arene = randint(581,669)
                y_cible1_arene = randint(328,413)
                duree = uniform(0.06,0.1)
                pyautogui.click(x_cible1_arene,y_cible1_arene,duration=duree)
                fIn = 1
            else:
                si_trois_emplacement_vide[0] = 1
                
        if cHoix == 1 and si_trois_emplacement_vide[1] == 0:               
            if pyautogui.locateOnScreen('../img/emplacement_vide2.png', region=(771, 196, 216, 250), grayscale=True, confidence=0.95) == None:
                x_cible1_arene = randint(855,930)
                y_cible1_arene = randint(313,382)
                duree = uniform(0.06,0.1)
                pyautogui.click(x_cible1_arene,y_cible1_arene,duration=duree)
                fIn = 1
            else:
                si_trois_emplacement_vide[1] = 1

        if cHoix == 2 and si_trois_emplacement_vide[2] == 0:
            if pyautogui.locateOnScreen('../img/emplacement_vide3.png', region=(1057, 204, 191, 245), grayscale=True, confidence=0.95) == None:
                x_cible1_arene = randint(1110,1196)
                y_cible1_arene = randint(316,393)
                duree = uniform(0.06,0.1)
                pyautogui.click(x_cible1_arene,y_cible1_arene,duration=duree)
                fIn = 1
            else:
                si_trois_emplacement_vide[2] = 1

        # for i in range(len(si_trois_emplacement_vide)):
        #     empla_vide = empla_vide + si_trois_emplacement_vide[i]

        # if empla_vide == 3:
        if cHoix == 3 and si_trois_emplacement_vide[3] == 0:
            if pyautogui.locateOnScreen('../img/emplacement_vide4.png', region=(1275, 268, 260, 316), grayscale=True, confidence=0.95) == None:
                x_cible1_arene = randint(1374,1460)
                y_cible1_arene = randint(353,436)
                duree = uniform(0.06,0.1)
                pyautogui.click(x_cible1_arene,y_cible1_arene,duration=duree)
                fIn = 1
            else:
                si_trois_emplacement_vide[3] = 1



def ou_est_la_cible_emplacement_un_ou_trois():
    fIn = 0
    si_trois_emplacement_vide = 3*[0]
    while fIn == 0:
        empla_vide = 0
        cHoix = randint(0,2)
        if cHoix == 0 and si_trois_emplacement_vide[0] == 0:
            if pyautogui.locateOnScreen('../img/emplacement_vide1_3.png', region=(591, 211, 238, 239), grayscale=True, confidence=0.95) == None:
                x_cible1_arene = randint(691,770)
                y_cible1_arene = randint(323,405)
                duree = uniform(0.06,0.1)
                pyautogui.click(x_cible1_arene,y_cible1_arene,duration=duree)
                fIn = 1
            else:
                si_trois_emplacement_vide[0] = 1

        if cHoix == 1 and si_trois_emplacement_vide[1] == 0:
            if pyautogui.locateOnScreen('../img/emplacement_vide2_3.png', region=(903, 185, 246, 263), grayscale=True, confidence=0.95) == None:
                x_cible1_arene = randint(1003,1087)
                y_cible1_arene = randint(309,384)
                duree = uniform(0.06,0.1)
                pyautogui.click(x_cible1_arene,y_cible1_arene,duration=duree)
                fIn = 1
            else:
                si_trois_emplacement_vide[1] = 1

        # for i in range(len(si_trois_emplacement_vide)):
        #     empla_vide = empla_vide + si_trois_emplacement_vide[i]

        # if empla_vide == 2:
        if cHoix == 2 and si_trois_emplacement_vide[2] == 0:
            if pyautogui.locateOnScreen('../img/emplacement_vide3_3.png', region=(1226, 267, 270, 296), grayscale=True, confidence=0.95) == None:
                x_cible1_arene = randint(1312,1399)
                y_cible1_arene = randint(348,422)
                duree = uniform(0.06,0.1)
                pyautogui.click(x_cible1_arene,y_cible1_arene,duration=duree)
                fIn = 1
            else:
                si_trois_emplacement_vide[2] = 1


def lance_sorts_en_arene(numb_monster):
    time_sleep = uniform(0.28,0.49)
    time.sleep(time_sleep)
    combat_finit = 0
    while  combat_finit == 0:
        #auto woonsa
        if pyautogui.locateOnScreen('../img/sort1_woonsa.png', region=(1273, 840, 188, 188), grayscale=True, confidence=0.8) != None:
            #sort 3 woonsa
            if pyautogui.locateOnScreen('../img/sort3_woonsa.png', region=(1640, 849, 166, 177), grayscale=True, confidence=0.83) != None:
                duree = uniform(0.06,0.1)
                x_sort3 = randint(1662, 1786)
                y_sort3 = randint(877, 1002)
                pyautogui.click(x_sort3, y_sort3, duration = duree)
                while pyautogui.locateOnScreen('../img/sort3_woonsa.png', region=(1640, 849, 166, 177), grayscale=True, confidence=0.83) != None:
                    if numb_monster == 1 or numb_monster == 3:
                        ou_est_la_cible_emplacement_un_ou_trois()
                    else:
                        ou_est_la_cible_emplacement_deux_ou_quatre()
            #sort 2 woonsa
            if pyautogui.locateOnScreen('../img/sort2_woonsa.png', region=(1462, 850, 171, 182), grayscale=True, confidence=0.85) != None:
                duree = uniform(0.06,0.1)
                x_sort2 = randint(1487, 1612)
                y_sort2 = randint(876, 1002)
                pyautogui.click(x_sort2, y_sort2, duration = duree)
                while pyautogui.locateOnScreen('../img/sort2_woonsa.png', region=(1462, 850, 171, 182), grayscale=True, confidence=0.7) != None:
                    if numb_monster == 1 or numb_monster == 3:
                        ou_est_la_cible_emplacement_un_ou_trois()
                    else:
                        ou_est_la_cible_emplacement_deux_ou_quatre()
            #sort 1 woonsa           
            if pyautogui.locateOnScreen('../img/sort1_woonsa.png', region=(1273, 840, 188, 188), grayscale=True, confidence=0.8) != None:
                while pyautogui.locateOnScreen('../img/sort1_woonsa.png', region=(1273, 840, 188, 188), grayscale=True, confidence=0.8) != None:
                    if numb_monster == 1 or numb_monster == 3:
                        ou_est_la_cible_emplacement_un_ou_trois()
                    else:
                        ou_est_la_cible_emplacement_deux_ou_quatre()
        #auto galion
        if pyautogui.locateOnScreen('../img/sort1_galion.png', region=(1273, 840, 188, 188), grayscale=True, confidence=0.8) != None:
            #sort 3 galion
            if pyautogui.locateOnScreen('../img/sort3_galion.png', region=(1640, 849, 166, 177), grayscale=True, confidence=0.83) != None:
                duree = uniform(0.06,0.1)
                x_sort3 = randint(1662, 1786)
                y_sort3 = randint(877, 1002)
                pyautogui.click(x_sort3, y_sort3, duration = duree)
                while pyautogui.locateOnScreen('../img/sort3_galion.png', region=(1640, 849, 166, 177), grayscale=True, confidence=0.83) != None:
                    if numb_monster == 1 or numb_monster == 3:
                        ou_est_la_cible_emplacement_un_ou_trois()
                    else:
                        ou_est_la_cible_emplacement_deux_ou_quatre()
            #sort 2 galion
            if pyautogui.locateOnScreen('../img/sort2_galion.png', region=(1462, 850, 171, 182), grayscale=True, confidence=0.85) != None:
                duree = uniform(0.06,0.1)
                x_sort2 = randint(1487, 1612)
                y_sort2 = randint(876, 1002)
                pyautogui.click(x_sort2, y_sort2, duration = duree)
                while pyautogui.locateOnScreen('../img/sort2_galion.png', region=(1462, 850, 171, 182), grayscale=True, confidence=0.7) != None:
                    if numb_monster == 1 or numb_monster == 3:
                        ou_est_la_cible_emplacement_un_ou_trois()
                    else:
                        ou_est_la_cible_emplacement_deux_ou_quatre()
            #sort 1 galion           
            if pyautogui.locateOnScreen('../img/sort1_galion.png', region=(1273, 840, 188, 188), grayscale=True, confidence=0.8) != None:
                while pyautogui.locateOnScreen('../img/sort1_galion.png', region=(1273, 840, 188, 188), grayscale=True, confidence=0.8) != None:
                    if numb_monster == 1 or numb_monster == 3:
                        ou_est_la_cible_emplacement_un_ou_trois()
                    else:
                        ou_est_la_cible_emplacement_deux_ou_quatre()

        #auto cp
        if pyautogui.locateOnScreen('../img/sort1_cp.png', region=(1273, 840, 188, 188), grayscale=True, confidence=0.8) != None:
            #sort 3 cp
            if pyautogui.locateOnScreen('../img/sort3_cp.png', region=(1640, 849, 166, 177), grayscale=True, confidence=0.83) != None:
                duree = uniform(0.06,0.1)
                x_sort3 = randint(1662, 1786)
                y_sort3 = randint(877, 1002)
                pyautogui.click(x_sort3, y_sort3, duration = duree)
                while pyautogui.locateOnScreen('../img/sort3_cp.png', region=(1640, 849, 166, 177), grayscale=True, confidence=0.83) != None:
                    if numb_monster == 1 or numb_monster == 3:
                        ou_est_la_cible_emplacement_un_ou_trois()
                    else:
                        ou_est_la_cible_emplacement_deux_ou_quatre()
            #sort 2 cp
            if pyautogui.locateOnScreen('../img/sort2_cp.png', region=(1462, 850, 171, 182), grayscale=True, confidence=0.85) != None:
                duree = uniform(0.06,0.1)
                x_sort2 = randint(1487, 1612)
                y_sort2 = randint(876, 1002)
                pyautogui.click(x_sort2, y_sort2, duration = duree)
                while pyautogui.locateOnScreen('../img/sort2_cp.png', region=(1462, 850, 171, 182), grayscale=True, confidence=0.7) != None:
                    if numb_monster == 1 or numb_monster == 3:
                        ou_est_la_cible_emplacement_un_ou_trois()
                    else:
                        ou_est_la_cible_emplacement_deux_ou_quatre()
            #sort 1 cp           
            if pyautogui.locateOnScreen('../img/sort1_cp.png', region=(1273, 840, 188, 188), grayscale=True, confidence=0.8) != None:
                while pyautogui.locateOnScreen('../img/sort1_cp.png', region=(1273, 840, 188, 188), grayscale=True, confidence=0.8) != None:
                    if numb_monster == 1 or numb_monster == 3:
                        ou_est_la_cible_emplacement_un_ou_trois()
                    else:
                        ou_est_la_cible_emplacement_deux_ou_quatre()

        #auto maximilian
        if pyautogui.locateOnScreen('../img/sort1_maximilian.png', region=(1273, 840, 188, 188), grayscale=True, confidence=0.8) != None:
            #sort 3 maximilian
            if pyautogui.locateOnScreen('../img/sort3_maximilian.png', region=(1640, 849, 166, 177), grayscale=True, confidence=0.83) != None:
                duree = uniform(0.06,0.1)
                x_sort3 = randint(1662, 1786)
                y_sort3 = randint(877, 1002)
                pyautogui.click(x_sort3, y_sort3, duration = duree)
                while pyautogui.locateOnScreen('../img/sort3_maximilian.png', region=(1640, 849, 166, 177), grayscale=True, confidence=0.83) != None:
                    if numb_monster == 1 or numb_monster == 3:
                        ou_est_la_cible_emplacement_un_ou_trois()
                    else:
                        ou_est_la_cible_emplacement_deux_ou_quatre()
            #sort 2 maximilian
            if pyautogui.locateOnScreen('../img/sort2_maximilian.png', region=(1462, 850, 171, 182), grayscale=True, confidence=0.85) != None:
                duree = uniform(0.06,0.1)
                x_sort2 = randint(1487, 1612)
                y_sort2 = randint(876, 1002)
                pyautogui.click(x_sort2, y_sort2, duration = duree)
                while pyautogui.locateOnScreen('../img/sort2_maximilian.png', region=(1462, 850, 171, 182), grayscale=True, confidence=0.7) != None:
                    if numb_monster == 1 or numb_monster == 3:
                        ou_est_la_cible_emplacement_un_ou_trois()
                    else:
                        ou_est_la_cible_emplacement_deux_ou_quatre()
            #sort 1 maximilian           
            if pyautogui.locateOnScreen('../img/sort1_maximilian.png', region=(1273, 840, 188, 188), grayscale=True, confidence=0.8) != None:
                while pyautogui.locateOnScreen('../img/sort1_maximilian.png', region=(1273, 840, 188, 188), grayscale=True, confidence=0.8) != None:
                    if numb_monster == 1 or numb_monster == 3:
                        ou_est_la_cible_emplacement_un_ou_trois()
                    else:
                        ou_est_la_cible_emplacement_deux_ou_quatre()
            
        
        elif pyautogui.locateOnScreen('../img/victory_rta.png', region=(556, 110, 734, 177), confidence=0.85) != None:
            while (pyautogui.locateOnScreen('../img/victory_rta.png', region=(556, 110, 734, 177), confidence=0.85)):
                x_click = randint(528,1365)
                y_click = randint(342,878)
                duree = uniform(0.06,0.1)
                pyautogui.click(x_click,y_click,duration=duree)
                time_sleep = uniform(0.28,0.49)
                time.sleep(time_sleep)
            combat_finit = 1
            
        elif pyautogui.locateOnScreen('../img/defeated_rta.png', region = (605, 106, 641, 200), confidence = 0.55) != None:
            while (pyautogui.locateOnScreen('../img/defeated_rta.png', region=(605, 106, 641, 200), confidence = 0.55)):
                x_click = randint(528,1365)
                y_click = randint(342,878)
                duree = uniform(0.06,0.1)
                pyautogui.click(x_click,y_click,duration=duree)
                time_sleep = uniform(0.28,0.49)
                time.sleep(time_sleep)
            combat_finit = 1