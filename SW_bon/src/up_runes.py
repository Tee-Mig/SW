import pyautogui
from pynput.mouse import Button, Controller
import time
from random import *
import pytesseract as pyt
import cv2
import numpy as np
import re
import sys

mouse = Controller()

def compute_efficiency(subs):
    subs_info = [[0, 1], [0, 1], [0, 1], [0, 1]]
    for id, i in enumerate(subs):
        comp = re.findall("\d++", i)
        subs_info[id][0] = int(comp[0])
        if ((i.startswith('ATQ') and i.endswith('%'))
            or (i.startswith('PV') and i.endswith('%'))
            or (i.startswith('DEF') and i.endswith('%'))
            or (i.startswith('RES'))
            or (i.startswith('Pré')) or (i.startswith('Pre'))):
            subs_info[id][1] = int(8)
        # elif i.startswith('RES') or i.startswith('Pré') or i.startswith('Pre'):
        #     subs_info[id][1] = int(18)
        elif (i.startswith('Tx') or i.startswith('VIT')):
            subs_info[id][1] = int(6)
        elif (i.startswith('ATQ') or i.startswith('DEF')):
            subs_info[id][1] = int(20)
        elif (i.startswith('PV')):
            subs_info[id][1] = int(375)
        elif (i.startswith('Dgts')):
            subs_info[id][1] = int(7)
        else:
            subs_info[id][0] = int(0)



    # print("computeeeeeeeeeeeeeeeeeeee:")
    # for i in range(4):
    #     print(f'sortie eff = {subs_info[i][0]} / ({subs_info[i][1]} * 5)')


    eff = (1 + (subs_info[0][0] / (subs_info[0][1] * 5)) + (subs_info[1][0] / (subs_info[1][1] * 5)) + (subs_info[2][0] / (subs_info[2][1] * 5)) + (subs_info[3][0] / (subs_info[3][1] * 5))) / 2.8
    return eff

def get_good_sub(subs):
    good_sub = 0

    for i in subs:
        if i.startswith('VIT'):
            good_sub = good_sub + 1
        if i.startswith('ATQ') and i.endswith('%'):
            good_sub = good_sub + 1
        if i.startswith('Tx') or i.startswith('TX'):
            good_sub = good_sub + 1
        if i.startswith('Dgts'):
            good_sub = good_sub + 1

    good_sub2 = 0
    for i in subs:
        if i.startswith('VIT'):
            good_sub2 = good_sub2 + 1
        if i.startswith('ATQ') and i.endswith('%'):
            good_sub2 = good_sub2 + 1
        if i.startswith('PV') and i.endswith('%'):
            good_sub2 = good_sub2 + 1
        if i.startswith('DEF') and i.endswith('%'):
            good_sub2 = good_sub2 + 1

    if (good_sub > 1 or good_sub2 > 1):
        if (good_sub > good_sub2):
            return good_sub
        else:
            return good_sub2
    if (good_sub <= 1 and good_sub2 <= 1):
        for i in subs:
            if i.startswith('VIT'):
                return 1
    return 0

def check_if_bad_sub_proc_on_up(rune_data, subs):
    if (rune_data["grade"] == "heroic"):
        nb_bad_proc = 0
        for i in subs:
            if (i.startswith('ATQ') or i.startswith('DEF') or i.startswith('PV')):
                if i.endswith('%'):
                    continue
                else:
                    number = re.findall("\d++", i)

                    # peut etre enlevé si sert a rien
                    if (i.startswith('ATQ') or i.startswith('DEF')):
                        if (int(number[0]) > int(20 * rune_data["heroic_bad_proc_sell"])):
                            return 0
                    if (i.startswith('PV')):
                        if (int(number[0]) > int(375 * rune_data["heroic_bad_proc_sell"])):
                            return 0
                    # peut etre enlevé si sert a rien

                    if (i.startswith('ATQ') or i.startswith('DEF')):
                        if (int(number[0]) > int(20)):
                            nb_bad_proc = nb_bad_proc + 1
                    if (i.startswith('PV')):
                        if (int(number[0]) > int(375)):
                            nb_bad_proc = nb_bad_proc + 1
                    if (nb_bad_proc == int(rune_data["heroic_bad_proc_sell"])):
                        return 0
        return 1
    elif (rune_data["grade"] == "legend"):
        nb_bad_proc = 0
        for i in subs:
            if (i.startswith('ATQ') or i.startswith('DEF') or i.startswith('PV')):
                if i.endswith('%'):
                    continue
                else:
                    number = re.findall("\d++", i)
                    if (i.startswith('ATQ') or i.startswith('DEF')):
                        if (int(number[0]) > int(20 * rune_data["legend_bad_proc_sell"])):
                            return 0
                    if (i.startswith('PV')):
                        if (int(number[0]) > int(375 * rune_data["legend_bad_proc_sell"])):
                            return 0
                        
                    if (i.startswith('ATQ') or i.startswith('DEF')):
                        if (int(number[0]) > int(20)):
                            nb_bad_proc = nb_bad_proc + 1
                    if (i.startswith('PV')):
                        if (int(number[0]) > int(375)):
                            nb_bad_proc = nb_bad_proc + 1

                    if (nb_bad_proc == int(rune_data["legend_bad_proc_sell"])):
                        return 0
                    
        return 1

def get_subs():
    pyt.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract"

    # img = cv2.imread('../test.jpg')

    img = pyautogui.screenshot(region=(1036, 464, 284, 183)) # toutes les lignes

    img2 = np.array(img)
    
    img2 = cv2.resize(img2, (0, 0), fx=2, fy=2)

    # Convert to HSV color-space
    hsv = cv2.cvtColor(img2, cv2.COLOR_BGR2HSV)

    # Get the binary mask
    msk = cv2.inRange(hsv, np.array([0, 0, 123]), np.array([179, 255, 255]))

    text = pyt.image_to_string(msk)


    split_text = text.split()


    split_text_process = []
    for i in range(len(split_text)):
        if ((split_text[i - 1] == "Tx" or split_text[i - 1] == "TX") and (split_text[i] == "critiq." or split_text[i] == "critiq,"
                                                                          or split_text[i] == "critig." or split_text[i] == "critig,")):
            continue
        if (split_text[i - 1] == "Dgts" and (split_text[i] == "critiq." or split_text[i] == "critiq,"
                                             or split_text[i] == "critig." or split_text[i] == "critig,")):
            continue
        if ((split_text[i] == "Tx" or split_text[i] == "TX") and (split_text[i + 1] == "critiq." or split_text[i + 1] == "critiq,"
                                            or split_text[i + 1] == "critig." or split_text[i + 1] == "critig,")):
            split_text_process.append("Tx" + "critiq.")
        elif (split_text[i] == "Dgts" and (split_text[i + 1] == "critiq." or split_text[i + 1] == "critiq,"
                                            or split_text[i + 1] == "critig." or split_text[i + 1] == "critig,")):
            split_text_process.append("Dgts" + "critiq.")
        else:
            split_text_process.append(split_text[i])

    split_text = split_text_process

    new_text_split = []
    if (len(split_text) <= 10 and len(split_text) % 2 == 0):
        if (split_text[1].startswith('+')):
            for i in range(0, len(split_text), 2):
                new_text_split.append(split_text[i] + split_text[i + 1])
        else:
            for i in range(int(len(split_text) / 2)):
                new_text_split.append(split_text[i] + split_text[int(i + len(split_text) / 2)])
    


    if (len(new_text_split) == 5):
        new_text_split.pop(0)

    # print("new listttttttttttttttttttttt: ")
    # for i in new_text_split:
    #     print(i)

    return new_text_split

def scroll_to_next_rune():
    x_pos = randint(553, 852)
    y_pos = randint(764, 833)

    x_drag_and_drop_range = randint(84, 124)
    y_drag_and_drop_range = randint(260, 378)
    plus_ou_moins = randint(1,2)
    if plus_ou_moins == 1:
        y_fin = y_pos - y_drag_and_drop_range
    else:
        y_fin = y_pos + y_drag_and_drop_range
    x_fin = x_pos + x_drag_and_drop_range


    duree = uniform(0.16,0.19)
    pyautogui.moveTo(x_pos, y_pos, duration = duree)
    duree = uniform(0.16,0.19)
    pyautogui.dragTo(x_fin, y_fin, duration = duree)

def get_amelioration():
    pyt.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract"

    img = pyautogui.screenshot(region=(1009, 265, 536, 56)) # toutes les lignes

    img2 = np.array(img)
    
    img2 = cv2.resize(img2, (0, 0), fx=2, fy=2)

    # Convert to HSV color-space
    hsv = cv2.cvtColor(img2, cv2.COLOR_BGR2HSV)

    # Get the binary mask
    msk = cv2.inRange(hsv, np.array([0, 0, 123]), np.array([179, 255, 255]))

    text = pyt.image_to_string(msk)
    if text.startswith('+12'):
        return 12
    if text.startswith('+9'):
        return 9
    if text.startswith('+6'):
        return 6
    if text.startswith('15'):
        return 15

def check_sell(rune_data, subs, amelioration, slot):

    keep_rune = check_if_bad_sub_proc_on_up(rune_data, subs)
    # print(f'keep_rune check 1 = {keep_rune}')
    if (keep_rune == 0):
        return 0, 0
    eff = compute_efficiency(subs)
    # print(f'efficiency of rune = {eff}')
    if (int(amelioration) == 6 or (int(amelioration) == 9 and rune_data["grade"] == "legend")):
        for i in subs:
            if i.startswith('VIT') or i.startswith('Txcritiq.'):
                if (int(re.findall("\d++", i)[0]) >= int(rune_data["tc_vit_one_proc"])):
                    # print("tc_vit_one_proc")
                    return 1, eff
                
            if i.startswith('Dgtscritiq.'):
                if (int(re.findall("\d++", i)[0]) >= int(rune_data["dcc_one_proc"])):
                    # print("dcc_one_proc")
                    return 1, eff
                
            if i.startswith('DEF') or i.startswith('PV') or i.startswith('ATQ') or i.startswith('RES') or i.startswith('Pré') or i.startswith('Pre'):
                if (int(re.findall("\d++", i)[0]) >= int(rune_data["percent_one_proc"])):
                    # print("percent_one_proc")
                    return 1, eff
            
    if (int(amelioration) == 9 or int(amelioration) == 12):
        for i in subs:
            if i.startswith('VIT') or i.startswith('Txcritiq.'):
                if (int(re.findall("\d++", i)[0]) >= int(rune_data["tc_vit_max_proc"])):
                    # print("tc_vit_max_proc")
                    return 1, eff
                
            if i.startswith('Dgtscritiq.'):
                if (int(re.findall("\d++", i)[0]) >= int(rune_data["dcc_max_proc"])):
                    # print("dcc_max_proc")
                    return 1, eff
                
            if i.startswith('DEF') or i.startswith('PV') or i.startswith('ATQ') or i.startswith('RES') or i.startswith('Pré') or i.startswith('Pre'):
                if (int(re.findall("\d++", i)[0]) >= int(rune_data["percent_max_proc"])):
                    # print("percent_max_proc")
                    return 1, eff

    if (int(slot) == 1 or int(slot) == 3 or int(slot) == 5):
        # print("slot135")
        if (rune_data["grade"] == "heroic" and float(eff) > float(rune_data["1_3_5_efficiency_heroic"])):
            # print(f'{eff} > {rune_data["1_3_5_efficiency_heroic"]}')
            return 1, eff
        elif (rune_data["grade"] == "legend" and float(eff) > float(rune_data["1_3_5_efficiency_legend_plus_9"] and amelioration == 9)):
            # print(f'{eff} > {rune_data["1_3_5_efficiency_legend_plus_9"]}')
            return 1, eff
        elif (rune_data["grade"] == "legend" and float(eff) > float(rune_data["1_3_5_efficiency_legend"] and amelioration == 12)):
            # print(f'{eff} > {rune_data["1_3_5_efficiency_legend"]}')
            return 1, eff
    else:
        # print("slot246")
        if (rune_data["grade"] == "heroic" and float(eff) > float(rune_data["2_4_6_efficiency_heroic"])):
            print(f'{eff} > {rune_data["2_4_6_efficiency_heroic"]}')
            return 1, eff
        elif (rune_data["grade"] == "legend" and float(eff) > float(rune_data["2_4_6_efficiency_legend_plus_9"] and amelioration == 9)):
            print(f'{eff} > {rune_data["2_4_6_efficiency_legend_plus_9"]}')
            return 1, eff
        elif (rune_data["grade"] == "legend" and float(eff) > float(rune_data["2_4_6_efficiency_legend"] and amelioration == 12)):
            print(f'{eff} > {rune_data["2_4_6_efficiency_legend"]}')
            return 1, eff
    
    return 0, eff

def take_screenshot_rune_sold_up(name):
    rand_numb = str(randint(0, sys.maxsize))
    pyautogui.screenshot('../runes_vendues/' + name + rand_numb + '7' + rand_numb + '.png')

def take_screenshot_rune_kept_up(name):
    rand_numb = str(randint(0, sys.maxsize))
    pyautogui.screenshot('../runes_gardees/' + name + rand_numb + '7' + rand_numb + '.png')

def rune_process():
    # good_sub = get_good_sub(subs)
    # print(f'good sub = {good_sub}')
    subs = get_subs()
    amelioration = get_amelioration()
    # print(f'amelioration = {amelioration}')
    up_rune, eff = check_sell(amelioration, subs)
    name_picture = ""
    eff_rounded = round(eff, 3)
    name_picture = name_picture + str(eff_rounded) + "_"
    for i in subs:
        name_picture = name_picture + i + "_"
    # print(f'name ===================== {name_picture}')

    if (up_rune == 1 and (amelioration == 9 or amelioration == 6)):
        # click sur ok
        x_click = randint(1014,1252)
        y_click = randint(887,955)
        mouse.position = (x_click, y_click)
        duree = uniform(0.06,0.1)
        time.sleep(duree)
        mouse.press(Button.left)
        mouse.release(Button.left)

        while (pyautogui.locateOnScreen('../img/amelioration_de_rune.jpg', region=(625, 43, 621, 157), confidence=0.9) == None):
            time_sleep = uniform(0.22,0.31)
            time.sleep(time_sleep)
        
        x_click = randint(711,984)
        y_click = randint(643,705)
        mouse.position = (x_click, y_click)
        duree = uniform(0.06,0.1)
        time.sleep(duree)
        mouse.press(Button.left)
        mouse.release(Button.left)

        while (pyautogui.locateOnScreen('../img/ameliorer2.jpg', region=(602, 624, 332, 212), confidence=0.9) == None):
            time_sleep = uniform(0.22,0.29)
            time.sleep(time_sleep)

        time_sleep = uniform(0.32,0.34)
        time.sleep(time_sleep)

        x_click = randint(660,875)
        y_click = randint(690,765)
        mouse.position = (x_click, y_click)
        duree = uniform(0.06,0.1)
        time.sleep(duree)
        mouse.press(Button.left)
        mouse.release(Button.left)

    if ((up_rune == 1 and amelioration == 12) or amelioration == 15):
        # click sur ok
        take_screenshot_rune_kept_up(name_picture)
        x_click = randint(1014,1252)
        y_click = randint(887,955)
        mouse.position = (x_click, y_click)
        duree = uniform(0.06,0.1)
        time.sleep(duree)
        mouse.press(Button.left)
        mouse.release(Button.left)

    if (up_rune == 0):
        take_screenshot_rune_sold_up(name_picture)
        x_click = randint(714,952)
        y_click = randint(887,958)
        mouse.position = (x_click, y_click)
        duree = uniform(0.06,0.1)
        time.sleep(duree)
        mouse.press(Button.left)
        mouse.release(Button.left)

        while (pyautogui.locateOnScreen('../img/amelioration_de_rune.jpg', region=(625, 43, 621, 157), confidence=0.9) == None):
            if (pyautogui.locateOnScreen('../img/oui_sell_runes.png', region=(490, 456, 875, 296), confidence=0.9)):
                x_pos_mob = pyautogui.locateOnScreen('../img/oui_sell_runes.png', region=(490, 456, 875, 296), confidence=0.9)
                x_click, y_click = pyautogui.center(x_pos_mob)
                x_click_add = randint(-98,97)
                y_click_add = randint(-30,27)
                x_click += x_click_add
                y_click += y_click_add
                duree = uniform(0.06,0.1)
                pyautogui.click(x_click,y_click,duration=duree)

# def select_rune_inventory():
#     rune_pos = list(pyautogui.locateAllOnScreen('../img/rune_inventory.png', region=(843, 579, 931, 325), grayscale=True, confidence=0.925))
#     for i in rune_pos:
#         # x_click_add = randint(26, 114)
#         # y_click_add = randint(32, 80)
#         x_click_add = randint(0, 20)
#         y_click_add = randint(0, 20)
#         mouse.position = (i[0] + x_click_add, i[1] + y_click_add)
#         duree = uniform(0.06,0.1)
#         time.sleep(duree)
#         # mouse.press(Button.left)
#         # mouse.release(Button.left)

#         time_sleep = uniform(0.59,0.61)
#         time.sleep(time_sleep)

def new_up_rune():
    pass

def old_up_all_runes():
    while (pyautogui.locateOnScreen('../img/amelioration_de_rune.jpg', region=(625, 43, 621, 157), confidence=0.9) == None):
            time_sleep = uniform(0.22,0.31)
            time.sleep(time_sleep)
    end = 0
    # if (1):
    while (1):
        while(len(list(pyautogui.locateAllOnScreen('../img/rune_montee.jpg', region=(441, 742, 493, 53), confidence=0.97)))):
            pos_lead = pyautogui.locateOnScreen('../img/rune_montee.jpg', region=(441, 742, 493, 53), confidence=0.97)
            while (pyautogui.locateOnScreen('../img/resultat_amelioration.jpg', region=(705, 65, 540, 149), confidence=0.9) == None):
                x_click, y_click = pyautogui.center(pos_lead)
                x_click_add = randint(-70, 5)
                y_click_add = randint(-10, 65)
                mouse.position = (x_click + x_click_add, y_click + y_click_add)
                duree = uniform(0.06,0.1)
                time.sleep(duree)
                mouse.press(Button.left)
                mouse.release(Button.left)

                time_sleep = uniform(0.43,0.45)
                time.sleep(time_sleep)

            rune_process()

        if (end == 1):
            break

        while (len(list(pyautogui.locateAllOnScreen('../img/rune_montee.jpg', region=(499, 731, 498, 65), confidence=0.97))) < 1):
            tmp_interserver = pyautogui.screenshot(region=(447, 762, 510, 75))
            scroll_to_next_rune()

            time_sleep = uniform(0.75, 0.78)
            time.sleep(time_sleep)

            if (pyautogui.locateOnScreen(tmp_interserver, region=(447, 762, 510, 75), confidence=0.97)):
                end = 1
                break
