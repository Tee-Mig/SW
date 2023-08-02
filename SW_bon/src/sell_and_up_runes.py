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
import pytesseract as pyt
import cv2
import numpy as np
import re
from up_runes import get_amelioration, check_sell

mouse = Controller()

def get_subs_new():
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

    # print(text)

    split_text = text.split()

    split_text_process = []
    for i in range(len(split_text)):
        # print(f'list index = {i} | {split_text[i]}')
        if(split_text[i].startswith('+')
           or split_text[i].startswith('ATQ') or split_text[i].startswith('PV') or split_text[i].startswith('DEF')
           or split_text[i].startswith('RES') or split_text[i].startswith('Pré') or split_text[i].startswith('Pre')
           or split_text[i].startswith('VIT')):
            split_text_process.append(split_text[i])
        
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


    # for i in range(len(split_text_process)):
    #     print(split_text_process[i])


    final_split_text_process = []
    count = 0
    tmp_str = ""
    for i in range(len(split_text_process)):
        tmp_str = tmp_str + split_text_process[i]
        count = count + 1
        if (count == 2):
            final_split_text_process.append(tmp_str)
            count = 0
            tmp_str = ""

    return final_split_text_process

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

def get_subs_in_dj(area):
    pyt.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract"

    if (area == "before"):
        img = pyautogui.screenshot(region=(411, 607, 281, 182))
    else:
        img = pyautogui.screenshot(region=(591, 423, 288, 201))

    img2 = np.array(img)
    
    img2 = cv2.resize(img2, (0, 0), fx=2, fy=2)

    # Convert to HSV color-space
    hsv = cv2.cvtColor(img2, cv2.COLOR_BGR2HSV)

    # Get the binary mask
    msk = cv2.inRange(hsv, np.array([0, 0, 123]), np.array([179, 255, 255]))

    text = pyt.image_to_string(msk)


    for charr in range(0, len(text)):
        if (text[charr] == '+' and text[charr - 1] != ' '):
            text = text[:charr] + ' ' + text[charr:]

    # print(text)

    split_text = text.split()

    # for i in range(len(split_text)):
    #     print(split_text[i])

    split_text_process = []
    for i in range(len(split_text)):
        # print(f'list index = {i} | {split_text[i]}')
        if(split_text[i].startswith('+')
           or split_text[i].startswith('ATQ') or split_text[i].startswith('PV') or split_text[i].startswith('DEF')
           or split_text[i].startswith('RES') or split_text[i].startswith('Pré') or split_text[i].startswith('Pre')
           or split_text[i].startswith('VIT')):
            split_text_process.append(split_text[i])
        
        if ((split_text[i - 1] == "Tx" or split_text[i - 1] == "TX") and (split_text[i] == "critiq." or split_text[i] == "critiq,"
                                                                          or split_text[i] == "critig." or split_text[i] == "critig,"
                                                                          or split_text[i] == "Critiq." or split_text[i] == "Critiq,"
                                                                          or split_text[i] == "Critig." or split_text[i] == "Critig,")):
            continue
        if (split_text[i - 1] == "Dgts" and (split_text[i] == "critiq." or split_text[i] == "critiq,"
                                             or split_text[i] == "critig." or split_text[i] == "critig,"
                                             or split_text[i] == "Critiq." or split_text[i] == "Critiq,"
                                             or split_text[i] == "Critig." or split_text[i] == "Critig,")):
            continue
        if ((split_text[i] == "Tx" or split_text[i] == "TX") and (split_text[i + 1] == "critiq." or split_text[i + 1] == "critiq,"
                                                                    or split_text[i + 1] == "critig." or split_text[i + 1] == "critig,"
                                                                    or split_text[i + 1] == "Critiq." or split_text[i + 1] == "Critiq,"
                                                                    or split_text[i + 1] == "Critig." or split_text[i + 1] == "Critig,")):
            split_text_process.append("Tx" + "critiq.")
        elif (split_text[i] == "Dgts" and (split_text[i + 1] == "critiq." or split_text[i + 1] == "critiq,"
                                            or split_text[i + 1] == "critig." or split_text[i + 1] == "critig,"
                                            or split_text[i + 1] == "Critiq." or split_text[i + 1] == "Critiq,"
                                            or split_text[i + 1] == "Critig." or split_text[i + 1] == "Critig,")):
            split_text_process.append("Dgts" + "critiq.")


    # for i in range(len(split_text_process)):
    #     print(split_text_process[i])


    final_split_text_process = []
    count = 0
    tmp_str = ""
    for i in range(len(split_text_process)):
        tmp_str = tmp_str + split_text_process[i]
        count = count + 1
        if (count == 2):
            final_split_text_process.append(tmp_str)
            count = 0
            tmp_str = ""

    # for i in range(len(final_split_text_process)):
    #     print(final_split_text_process[i])

    return final_split_text_process

    # img2 = np.array(img)
    
    # img2 = cv2.resize(img2, (0, 0), fx=2, fy=2)

    # # Convert to HSV color-space
    # hsv = cv2.cvtColor(img2, cv2.COLOR_BGR2HSV)

    # # Get the binary mask
    # msk = cv2.inRange(hsv, np.array([0, 0, 123]), np.array([179, 255, 255]))

    # text = pyt.image_to_string(msk)

    # # text.replace(" ", "")

    # split_text = text.split()


    # split_text_process = []
    # for i in range(len(split_text)):
    #     if ((split_text[i - 1] == "Tx" or split_text[i - 1] == "TX") and (split_text[i] == "critiq." or split_text[i] == "critiq,"
    #                                                                       or split_text[i] == "critig." or split_text[i] == "critig,")):
    #         continue
    #     if (split_text[i - 1] == "Dgts" and (split_text[i] == "critiq." or split_text[i] == "critiq,"
    #                                          or split_text[i] == "critig." or split_text[i] == "critig,")):
    #         continue
    #     if ((split_text[i] == "Tx" or split_text[i] == "TX") and (split_text[i + 1] == "critiq." or split_text[i + 1] == "critiq,"
    #                                         or split_text[i + 1] == "critig." or split_text[i + 1] == "critig,")):
    #         split_text_process.append("Tx" + "critiq.")
    #     elif (split_text[i] == "Dgts" and (split_text[i + 1] == "critiq." or split_text[i + 1] == "critiq,"
    #                                         or split_text[i + 1] == "critig." or split_text[i + 1] == "critig,")):
    #         split_text_process.append("Dgts" + "critiq.")
    #     else:
    #         split_text_process.append(split_text[i])

    # split_text = split_text_process

    # # print("TESTTTTTTTTTTTTTTTTT:")
    # # for i in split_text:
    # #     print(i)

    # # print(f'sortie = {len(split_text)}')
    # # return 0
    # new_text_split = []
    # if (len(split_text) <= 10 and len(split_text) % 2 == 0):
    #     if (split_text[1].startswith('+')):
    #         # print("dans le if")
    #         for i in range(0, len(split_text), 2):
    #             new_text_split.append(split_text[i] + split_text[i + 1])
    #     else:
    #         # print("dans le else")
    #         for i in range(int(len(split_text) / 2)):
    #             new_text_split.append(split_text[i] + split_text[int(i + len(split_text) / 2)])

    # if (len(new_text_split) == 5):
    #     new_text_split.pop(0)

    # # print("new listttttttttttttttttttttt: ")
    # # for i in new_text_split:
    # #     print(i)

    # return new_text_split

def make_name_with_sub_after():
    subs = ""
    if (pyautogui.locateOnScreen('../img/vit2.jpg', region=(560, 400, 557, 251), confidence=0.65)):
        subs = subs + "_vit"

    if (pyautogui.locateOnScreen('../img/tc2.jpg', region=(560, 400, 557, 251), confidence=0.85)):
        subs = subs + "_tc"

    if (pyautogui.locateOnScreen('../img/dcc2.jpg', region=(560, 400, 557, 251), confidence=0.8)):
        subs = subs + "_dcc"

    if (pyautogui.locateOnScreen('../img/atq2.jpg', region=(560, 400, 557, 251), confidence=0.96)): # parfait
        sub_len = len(list(pyautogui.locateAllOnScreen('../img/atq2.jpg', region=(560, 400, 557, 251), confidence=0.96)))
        if (sub_len > 1):
            subs = subs + "_atq_pourcent"
        else:
            x_pos_mob = pyautogui.locateOnScreen('../img/atq2.jpg', region=(560, 400, 557, 251), confidence=0.96)
            x_click, y_click = pyautogui.center(x_pos_mob)
            if (pyautogui.locateOnScreen('../img/pourcent2.jpg', region=(x_click + 12, y_click - 40, 145, 80), confidence=0.9)):
                subs = subs + "_atq_pourcent"

    if (pyautogui.locateOnScreen('../img/pv2.jpg', region=(560, 400, 557, 251), confidence=0.975)): # parfait
        sub_len = len(list(pyautogui.locateAllOnScreen('../img/pv2.jpg', region=(560, 400, 557, 251), confidence=0.975)))
        if (sub_len > 1):
            subs = subs + "_pv_pourcent"
        else:
            x_pos_mob = pyautogui.locateOnScreen('../img/pv2.jpg', region=(560, 400, 557, 251), confidence=0.975)
            x_click, y_click = pyautogui.center(x_pos_mob)
            if (pyautogui.locateOnScreen('../img/pourcent2.jpg', region=(x_click + 12, y_click - 40, 145, 80), confidence=0.9)):
                subs = subs + "_pv_pourcent"

    if (pyautogui.locateOnScreen('../img/def2.jpg', region=(560, 400, 557, 251), confidence=0.96)): # parfait
        sub_len = len(list(pyautogui.locateAllOnScreen('../img/def2.jpg', region=(560, 400, 557, 251), confidence=0.96)))
        # print(f'def len = {sub_len}')
        if (sub_len > 1):
            subs = subs + "_def_pourcent"
        else:
            x_pos_mob = pyautogui.locateOnScreen('../img/def2.jpg', region=(560, 400, 557, 251), confidence=0.96)
            x_click, y_click = pyautogui.center(x_pos_mob)
            if (pyautogui.locateOnScreen('../img/pourcent2.jpg', region=(x_click + 12, y_click - 40, 145, 80), confidence=0.9)):
                subs = subs + "_def_pourcent"

    return subs

def take_screenshot_rune_sold_after():
    subs = make_name_with_sub_after()
    rand_numb = str(randint(0, sys.maxsize))
    pyautogui.screenshot('../runes_vendues/after_' + subs + rand_numb + '7' + rand_numb + '.png')

def take_screenshot_rune_kept_after():
    subs = make_name_with_sub_after()
    rand_numb = str(randint(0, sys.maxsize))
    pyautogui.screenshot('../runes_gardees/after_' + subs + rand_numb + '7' + rand_numb + '.png')

def take_screenshot_rune_sold_after2(subs):
    pyautogui.screenshot('../runes_vendues/after_' + subs + str(round(randint(0, sys.maxsize), 6)) + '7' + str(round(randint(0, sys.maxsize), 6)) + '.png')

def take_screenshot_rune_kept_after2(subs):
    pyautogui.screenshot('../runes_gardees/afterAI_' + subs + str(round(randint(0, sys.maxsize), 6)) + '7' + str(round(randint(0, sys.maxsize), 6)) + '.png')

def make_name_with_sub_before():
    subs = ""
    if (pyautogui.locateOnScreen('../img/vit.jpg', region=(401, 593, 522, 204), confidence=0.65)):
        subs = subs + "_vit"

    if (pyautogui.locateOnScreen('../img/tc.jpg', region=(401, 593, 522, 204), confidence=0.8)):
        subs = subs + "_tc"

    if (pyautogui.locateOnScreen('../img/dcc.jpg', region=(401, 593, 522, 204), confidence=0.8)):
        subs = subs + "_dcc"

    if (pyautogui.locateOnScreen('../img/atq.jpg', region=(401, 593, 522, 204), confidence=0.96)): # parfait
        sub_len = len(list(pyautogui.locateAllOnScreen('../img/atq.jpg', region=(401, 593, 522, 204), confidence=0.96)))
        if (sub_len > 1):
            subs = subs + "_atq_pourcent"
        else:
            x_pos_mob = pyautogui.locateOnScreen('../img/atq.jpg', region=(401, 593, 522, 204), confidence=0.96)
            x_click, y_click = pyautogui.center(x_pos_mob)
            if (pyautogui.locateOnScreen('../img/pourcent.jpg', region=(x_click + 12, y_click - 40, 145, 80), confidence=0.8)):
                subs = subs + "_atq_pourcent"

    if (pyautogui.locateOnScreen('../img/pv.jpg', region=(401, 593, 522, 204), confidence=0.97)): # parfait
        sub_len = len(list(pyautogui.locateAllOnScreen('../img/pv.jpg', region=(401, 593, 522, 204), confidence=0.97)))
        if (sub_len > 1):
            subs = subs + "_pv_pourcent"
        else:
            x_pos_mob = pyautogui.locateOnScreen('../img/pv.jpg', region=(401, 593, 522, 204), confidence=0.97)
            x_click, y_click = pyautogui.center(x_pos_mob)
            if (pyautogui.locateOnScreen('../img/pourcent.jpg', region=(x_click + 12, y_click - 40, 145, 80), confidence=0.8)):
                subs = subs + "_pv_pourcent"

    if (pyautogui.locateOnScreen('../img/def.jpg', region=(401, 593, 522, 204), confidence=0.95)): # parfait
        sub_len = len(list(pyautogui.locateAllOnScreen('../img/def.jpg', region=(401, 593, 522, 204), confidence=0.95)))
        if (sub_len > 1):
            subs = subs + "_def_pourcent"
        else:
            x_pos_mob = pyautogui.locateOnScreen('../img/def.jpg', region=(401, 593, 522, 204), confidence=0.95)
            x_click, y_click = pyautogui.center(x_pos_mob)
            if (pyautogui.locateOnScreen('../img/pourcent.jpg', region=(x_click + 12, y_click - 40, 145, 80), confidence=0.8)):
                subs = subs + "_def_pourcent"
    return subs

def take_screenshot_rune_sold_before():
    subs = make_name_with_sub_before()
    rand_numb = str(randint(0, sys.maxsize))
    pyautogui.screenshot('../runes_vendues/before_' + subs + rand_numb + '7' + rand_numb + '.png')

def take_screenshot_rune_kept_before():
    subs = make_name_with_sub_before()
    rand_numb = str(randint(0, sys.maxsize))
    pyautogui.screenshot('../runes_gardees/before_' + subs + rand_numb + '7' + rand_numb + '.png')

def take_screenshot_rune_sold_before2(subs):
    pyautogui.screenshot('../runes_vendues/beforeAI_' + subs + str(round(randint(0, sys.maxsize), 6)) + '7' + str(round(randint(0, sys.maxsize), 6)) + '.png')

def take_screenshot_rune_kept_before2(subs):
    pyautogui.screenshot('../runes_gardees/beforeAI_' + subs + str(round(randint(0, sys.maxsize), 6)) + '7' + str(round(randint(0, sys.maxsize), 6)) + '.png')

def check_sub_after():
    good_sub = 0
    if (pyautogui.locateOnScreen('../img/vit2.jpg', region=(560, 400, 557, 251), confidence=0.65)):
        good_sub = good_sub + 1
        # print("vit")
    if (pyautogui.locateOnScreen('../img/atq2.jpg', region=(560, 400, 557, 251), confidence=0.96)): # parfait
        sub_len = len(list(pyautogui.locateAllOnScreen('../img/atq2.jpg', region=(560, 400, 557, 251), confidence=0.96)))
        if (sub_len > 1):
            good_sub = good_sub + 1
            # print("atq pourcent")
        else:
            x_pos_mob = pyautogui.locateOnScreen('../img/atq2.jpg', region=(560, 400, 557, 251), confidence=0.96)
            x_click, y_click = pyautogui.center(x_pos_mob)
            if (pyautogui.locateOnScreen('../img/pourcent2.jpg', region=(x_click + 12, y_click - 40, 145, 80), confidence=0.95)):
                good_sub = good_sub + 1
                # print("atq pourcent")
    if (pyautogui.locateOnScreen('../img/tc2.jpg', region=(560, 400, 557, 251), confidence=0.85)):
        good_sub = good_sub + 1
        # print("tc")
    if (pyautogui.locateOnScreen('../img/dcc2.jpg', region=(560, 400, 557, 251), confidence=0.8)):
        good_sub = good_sub + 1
        # print("dcc")

    good_sub2 = 0
    if (pyautogui.locateOnScreen('../img/vit2.jpg', region=(560, 400, 557, 251), confidence=0.65)):
        good_sub2 = good_sub2 + 1
    if (pyautogui.locateOnScreen('../img/atq2.jpg', region=(560, 400, 557, 251), confidence=0.96)): # parfait
        sub_len = len(list(pyautogui.locateAllOnScreen('../img/atq2.jpg', region=(560, 400, 557, 251), confidence=0.96)))
        if (sub_len > 1):
            good_sub2 = good_sub2 + 1
        else:
            x_pos_mob = pyautogui.locateOnScreen('../img/atq2.jpg', region=(560, 400, 557, 251), confidence=0.96)
            x_click, y_click = pyautogui.center(x_pos_mob)
            if (pyautogui.locateOnScreen('../img/pourcent2.jpg', region=(x_click + 12, y_click - 40, 145, 80), confidence=0.95)):
                good_sub2 = good_sub2 + 1
    if (pyautogui.locateOnScreen('../img/pv2.jpg', region=(560, 400, 557, 251), confidence=0.975)): # parfait
        sub_len = len(list(pyautogui.locateAllOnScreen('../img/pv2.jpg', region=(560, 400, 557, 251), confidence=0.975)))
        # print(f'pv len = {sub_len}')
        if (sub_len > 1):
            good_sub2 = good_sub2 + 1
            # print("pv pourcent")
        else:
            x_pos_mob = pyautogui.locateOnScreen('../img/pv2.jpg', region=(560, 400, 557, 251), confidence=0.975)
            x_click, y_click = pyautogui.center(x_pos_mob)
            if (pyautogui.locateOnScreen('../img/pourcent2.jpg', region=(x_click + 12, y_click - 40, 145, 80), confidence=0.95)):
                good_sub2 = good_sub2 + 1
                # print("pv pourcent")
    if (pyautogui.locateOnScreen('../img/def2.jpg', region=(560, 400, 557, 251), confidence=0.96)): # parfait
        sub_len = len(list(pyautogui.locateAllOnScreen('../img/def2.jpg', region=(560, 400, 557, 251), confidence=0.96)))
        # print(f'def len = {sub_len}')
        if (sub_len > 1):
            good_sub2 = good_sub2 + 1
            # print("def pourcent")
        else:
            x_pos_mob = pyautogui.locateOnScreen('../img/def2.jpg', region=(560, 400, 557, 251), confidence=0.96)
            x_click, y_click = pyautogui.center(x_pos_mob)
            if (pyautogui.locateOnScreen('../img/pourcent2.jpg', region=(x_click + 12, y_click - 40, 145, 80), confidence=0.95)):
                good_sub2 = good_sub2 + 1
                # print("def pourcent")

    if (good_sub > 1 or good_sub2 > 1):
        if (good_sub > good_sub2):
            return good_sub
        else:
            return good_sub2
    if (good_sub <= 1 and good_sub2 <= 1):
        if (pyautogui.locateOnScreen('../img/vit.jpg', region=(560, 400, 557, 251), confidence=0.65)):
            return 1
    return 0

def check_sub_before():
    good_sub = 0
    if (pyautogui.locateOnScreen('../img/vit.jpg', region=(401, 593, 522, 204), confidence=0.65)):
        good_sub = good_sub + 1
    if (pyautogui.locateOnScreen('../img/atq.jpg', region=(401, 593, 522, 204), confidence=0.96)): # parfait
        sub_len = len(list(pyautogui.locateAllOnScreen('../img/atq.jpg', region=(401, 593, 522, 204), confidence=0.96)))
        if (sub_len > 1):
            good_sub = good_sub + 1
        else:
            x_pos_mob = pyautogui.locateOnScreen('../img/atq.jpg', region=(401, 593, 522, 204), confidence=0.96)
            x_click, y_click = pyautogui.center(x_pos_mob)
            if (pyautogui.locateOnScreen('../img/pourcent.jpg', region=(x_click + 12, y_click - 40, 145, 80), confidence=0.8)):
                good_sub = good_sub + 1
    if (pyautogui.locateOnScreen('../img/tc.jpg', region=(401, 593, 522, 204), confidence=0.8)):
        good_sub = good_sub + 1
    if (pyautogui.locateOnScreen('../img/dcc.jpg', region=(401, 593, 522, 204), confidence=0.8)):
        good_sub = good_sub + 1

    good_sub2 = 0
    if (pyautogui.locateOnScreen('../img/vit.jpg', region=(401, 593, 522, 204), confidence=0.65)):
        good_sub2 = good_sub2 + 1
    if (pyautogui.locateOnScreen('../img/atq.jpg', region=(401, 593, 522, 204), confidence=0.96)): # parfait
        sub_len = len(list(pyautogui.locateAllOnScreen('../img/atq.jpg', region=(401, 593, 522, 204), confidence=0.96)))
        if (sub_len > 1):
            good_sub2 = good_sub2 + 1
        else:
            x_pos_mob = pyautogui.locateOnScreen('../img/atq.jpg', region=(401, 593, 522, 204), confidence=0.96)
            x_click, y_click = pyautogui.center(x_pos_mob)
            if (pyautogui.locateOnScreen('../img/pourcent.jpg', region=(x_click + 12, y_click - 40, 145, 80), confidence=0.8)):
                good_sub2 = good_sub2 + 1
    if (pyautogui.locateOnScreen('../img/pv.jpg', region=(401, 593, 522, 204), confidence=0.97)): # parfait
        sub_len = len(list(pyautogui.locateAllOnScreen('../img/pv.jpg', region=(401, 593, 522, 204), confidence=0.97)))
        if (sub_len > 1):
            good_sub2 = good_sub2 + 1
        else:
            x_pos_mob = pyautogui.locateOnScreen('../img/pv.jpg', region=(401, 593, 522, 204), confidence=0.97)
            x_click, y_click = pyautogui.center(x_pos_mob)
            if (pyautogui.locateOnScreen('../img/pourcent.jpg', region=(x_click + 12, y_click - 40, 145, 80), confidence=0.8)):
                good_sub2 = good_sub2 + 1
    if (pyautogui.locateOnScreen('../img/def.jpg', region=(401, 593, 522, 204), confidence=0.95)): # parfait
        sub_len = len(list(pyautogui.locateAllOnScreen('../img/def.jpg', region=(401, 593, 522, 204), confidence=0.95)))
        if (sub_len > 1):
            good_sub2 = good_sub2 + 1
        else:
            x_pos_mob = pyautogui.locateOnScreen('../img/def.jpg', region=(401, 593, 522, 204), confidence=0.95)
            x_click, y_click = pyautogui.center(x_pos_mob)
            if (pyautogui.locateOnScreen('../img/pourcent.jpg', region=(x_click + 12, y_click - 40, 145, 80), confidence=0.8)):
                good_sub2 = good_sub2 + 1

    if (good_sub > 1 or good_sub2 > 1):
        if (good_sub > good_sub2):
            return good_sub
        else:
            return good_sub2
    if (good_sub <= 1 and good_sub2 <= 1):
        if (pyautogui.locateOnScreen('../img/vit.jpg', region=(401, 593, 522, 204), confidence=0.65)):
            return 1
    return 0

def go_up_rift():
        x_pos = randint(1221, 1686)
        y_pos = randint(449, 816)

        x_drag_and_drop_range = randint(30, 50)
        y_drag_and_drop_range = randint(100, 150)
        plus_ou_moins = randint(1,2)
        if plus_ou_moins == 1:
            x_fin = x_pos-x_drag_and_drop_range
        else:
            x_fin = x_pos+x_drag_and_drop_range
        y_fin = y_pos+y_drag_and_drop_range


        duree = uniform(0.16,0.19)
        pyautogui.moveTo(x_pos, y_pos, duration = duree)
        duree = uniform(0.16,0.19)
        pyautogui.dragTo(x_fin, y_fin, duration = duree)

def go_down_rift():
        x_pos = randint(1221, 1686)
        y_pos = randint(449, 816)

        x_drag_and_drop_range = randint(30, 50)
        y_drag_and_drop_range = randint(100, 150)
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

def select_bad_runes_rift():
    while (pyautogui.locateOnScreen('../img/vente_selective2.png', region=(1236, 822, 307, 173)) == None):
        time_sleep = uniform(0.22,0.29)
        time.sleep(time_sleep)

    x_range = 1176
    y_range = 715
    if (pyautogui.locateOnScreen('../img/top_rift2.jpg', region=(1284, 347, 233, 229), confidence=0.99) == None):
        for i in range(2):
            # pyautogui.moveTo(x_range, y_range, 0.45)
            # pyautogui.moveTo(x_range + 154, y_range + 167, 0.45)
            # x_range = x_range + 140
            # continue
            if ((pyautogui.locateOnScreen('../img/rune_heroique.jpg', region=(x_range, y_range, 154, 167), confidence=0.85)
                    or pyautogui.locateOnScreen('../img/rune_legendaire.jpg', region=(x_range, y_range, 154, 167), confidence=0.85))
                    and pyautogui.locateOnScreen('../img/rune_sold.jpg', region=(x_range, y_range, 154, 167), confidence=0.4) == None
                    and pyautogui.locateOnScreen('../img/rune_sold2.jpg', region=(x_range, y_range, 154, 167), confidence=0.4) == None):
                    # print("----------------------------------------------------------------------------------------")

                    # while (pyautogui.locateOnScreen('../img/croix_rune.jpg', region=(1057, 393, 88, 79), confidence=0.8) == None):
                    #     time_sleep = uniform(0.22,0.25)
                    #     time.sleep(time_sleep)

                    x_click = x_range + 75
                    y_click = y_range + 83
                    x_click_add = randint(-35,35)
                    y_click_add = randint(-35,35)
                    x_click += x_click_add
                    y_click += y_click_add
                    mouse.position = (x_click, y_click)
                    duree = uniform(0.06,0.1)
                    time.sleep(duree)
                    mouse.press(Button.left)
                    mouse.release(Button.left)

                    time_sleep = uniform(0.55,0.57)
                    time.sleep(time_sleep)

                    while (pyautogui.locateOnScreen('../img/croix_rune.jpg', region=(1057, 393, 88, 79), confidence=0.8) == None):
                        x_click = x_range + 75
                        y_click = y_range + 83
                        x_click_add = randint(-35,35)
                        y_click_add = randint(-35,35)
                        x_click += x_click_add
                        y_click += y_click_add
                        mouse.position = (x_click, y_click)
                        duree = uniform(0.06,0.1)
                        time.sleep(duree)
                        mouse.press(Button.left)
                        mouse.release(Button.left)

                        time_sleep = uniform(0.45,0.47)
                        time.sleep(time_sleep)

                    # while (pyautogui.locateOnScreen('../img/croix_rune.jpg', region=(1057, 393, 88, 79), confidence=0.9) == None):
                    #     time_sleep = uniform(0.22,0.29)
                    #     time.sleep(time_sleep)
                    
                    subs = check_sub_before()
                    # subs_arr = get_subs_in_dj("before")
                    # subs = get_good_sub(subs_arr)
                    # file_name = ""
                    # for i in subs_arr:
                    #     file_name = file_name + i + "_"

                    # print(f'status subs = {subs}')
                    if (subs > 0):
                        # take_screenshot_rune_kept_before2(file_name)
                        x_click = x_range + 75
                        y_click = y_range + 83
                        x_click_add = randint(-35,35)
                        y_click_add = randint(-35,35)
                        x_click += x_click_add
                        y_click += y_click_add
                        mouse.position = (x_click, y_click)
                        duree = uniform(0.06,0.1)
                        time.sleep(duree)
                        mouse.press(Button.left)
                        mouse.release(Button.left)
                    # else:
                    #     take_screenshot_rune_sold_before2(file_name)

            x_range = x_range + 140

        while (pyautogui.locateOnScreen('../img/top_rift2.jpg', region=(1284, 347, 233, 229), confidence=0.98) == None):
            go_up_rift()
            time_sleep = uniform(0.59,0.63)
            time.sleep(time_sleep)

    select_bad_runes()

def up_runes_rift():
    while (pyautogui.locateOnScreen('../img/vente_selective.png', region=(1406, 831, 356, 135)) == None):
        time_sleep = uniform(0.22,0.29)
        time.sleep(time_sleep)

    up_runes(1)

    #Miguel
    for i in range (2):
        go_down_rift()
        time_sleep = uniform(0.59,0.63)
        time.sleep(time_sleep)

    x_range = 1176
    y_range = 715
    if (pyautogui.locateOnScreen('../img/top_rift.jpg', region=(1284, 347, 233, 229), confidence=0.99) == None):
        for i in range(2):
            # pyautogui.moveTo(x_range, y_range, 0.45)
            # pyautogui.moveTo(x_range + 154, y_range + 167, 0.45)
            # x_range = x_range + 140
            # continue
            if ((pyautogui.locateOnScreen('../img/rune_heroique.jpg', region=(x_range, y_range, 154, 167), confidence=0.85)
                or pyautogui.locateOnScreen('../img/rune_legendaire.jpg', region=(x_range, y_range, 154, 167), confidence=0.85))
                and pyautogui.locateOnScreen('../img/rune_sold2.jpg', region=(x_range, y_range, 154, 167), confidence=0.4) == None):
                x_click = x_range + 75
                y_click = y_range + 83
                x_click_add = randint(-35,35)
                y_click_add = randint(-35,35)
                x_click += x_click_add
                y_click += y_click_add
                mouse.position = (x_click, y_click)
                duree = uniform(0.06,0.1)
                time.sleep(duree)
                mouse.press(Button.left)
                mouse.release(Button.left)

                time_sleep = uniform(0.34,0.36)
                time.sleep(time_sleep)
                
                while (pyautogui.locateOnScreen('../img/ameliorer.jpg', region=(931, 683, 300, 178), confidence=0.8) == None):
                    x_click = x_range + 75
                    y_click = y_range + 83
                    x_click_add = randint(-35,35)
                    y_click_add = randint(-35,35)
                    x_click += x_click_add
                    y_click += y_click_add
                    mouse.position = (x_click, y_click)
                    duree = uniform(0.06,0.1)
                    time.sleep(duree)
                    mouse.press(Button.left)
                    mouse.release(Button.left)

                    time_sleep = uniform(0.52,0.54)
                    time.sleep(time_sleep)

                # while (pyautogui.locateOnScreen('../img/ameliorer.jpg', region=(931, 683, 300, 178), confidence=0.9) == None):
                #     time_sleep = uniform(0.22,0.29)
                #     time.sleep(time_sleep)
                
                subs = check_sub_after()
                # subs_arr = get_subs_in_dj("after")
                # subs = get_good_sub(subs_arr)
                # file_name = ""
                # for i in subs_arr:
                #     file_name = file_name + i + "_"
                # take_screenshot_rune_kept_after2(file_name)

                x_click = randint(979,1191)
                y_click = randint(738,814)
                mouse.position = (x_click, y_click)
                duree = uniform(0.06,0.1)
                time.sleep(duree)
                mouse.press(Button.left)
                mouse.release(Button.left)
                
                while (pyautogui.locateOnScreen('../img/amelioration_rune.jpg', region=(303, 566, 774, 222), confidence=0.9) == None):
                    time_sleep = uniform(0.22,0.29)
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

                if (subs == 1):
                    x_click = randint(709,824)
                    y_click = randint(486,577)
                    mouse.position = (x_click, y_click)
                    duree = uniform(0.06,0.1)
                    time.sleep(duree)
                    mouse.press(Button.left)
                    mouse.release(Button.left)
                
                if (subs == 2 or subs == 3):
                    x_click = randint(880,993)
                    y_click = randint(482,582)
                    mouse.position = (x_click, y_click)
                    duree = uniform(0.06,0.1)
                    time.sleep(duree)
                    mouse.press(Button.left)
                    mouse.release(Button.left)

                if (subs == 4):
                    x_click = randint(1050,1163)
                    y_click = randint(482,578)
                    mouse.position = (x_click, y_click)
                    duree = uniform(0.06,0.1)
                    time.sleep(duree)
                    mouse.press(Button.left)
                    mouse.release(Button.left)

                time_sleep = uniform(0.32,0.34)
                time.sleep(time_sleep)

                x_click = randint(660,875)
                y_click = randint(690,765)
                mouse.position = (x_click, y_click)
                duree = uniform(0.06,0.1)
                time.sleep(duree)
                mouse.press(Button.left)
                mouse.release(Button.left)

                while (pyautogui.locateOnScreen('../img/fermer_rune.jpg', region=(766, 862, 342, 181), confidence=0.9) == None):
                    time_sleep = uniform(0.22,0.29)
                    time.sleep(time_sleep)

                time_sleep = uniform(0.32,0.34)
                time.sleep(time_sleep)

                x_click = randint(821,1059)
                y_click = randint(921,983)
                mouse.position = (x_click, y_click)
                duree = uniform(0.06,0.1)
                time.sleep(duree)
                mouse.press(Button.left)
                mouse.release(Button.left)

                
                while (pyautogui.locateOnScreen('../img/croix_rune.jpg', region=(1217, 175, 172, 133), confidence=0.9) == None):
                    time_sleep = uniform(0.22,0.29)
                    time.sleep(time_sleep)

                time_sleep = uniform(0.32,0.34)
                time.sleep(time_sleep)

                x_click = randint(1268,1298)
                y_click = randint(230,259)
                mouse.position = (x_click, y_click)
                duree = uniform(0.06,0.1)
                time.sleep(duree)
                mouse.press(Button.left)
                mouse.release(Button.left)

            x_range = x_range + 140

def select_bad_runes():

    while (pyautogui.locateOnScreen('../img/vente_selective2.png', region=(1236, 822, 307, 173)) == None):
        time_sleep = uniform(0.22,0.29)
        time.sleep(time_sleep)

    x_range = 1169
    y_range = 379
    for y in range (3):
        x_range_tmp = x_range
        for x in range (4):
            # pyautogui.moveTo(x_range_tmp, y_range, 0.45)
            # pyautogui.moveTo(x_range_tmp + 154, y_range + 167, 0.45)
            if ((pyautogui.locateOnScreen('../img/rune_heroique.jpg', region=(x_range_tmp, y_range, 154, 167), confidence=0.85)
                or pyautogui.locateOnScreen('../img/rune_legendaire.jpg', region=(x_range_tmp, y_range, 154, 167), confidence=0.85))
                and pyautogui.locateOnScreen('../img/rune_sold.jpg', region=(x_range_tmp, y_range, 154, 167), confidence=0.4) == None
                and pyautogui.locateOnScreen('../img/rune_sold2.jpg', region=(x_range_tmp, y_range, 154, 167), confidence=0.4) == None):

                x_click = x_range_tmp + 75
                y_click = y_range + 83
                x_click_add = randint(-35,35)
                y_click_add = randint(-35,35)
                x_click += x_click_add
                y_click += y_click_add
                mouse.position = (x_click, y_click)
                duree = uniform(0.06,0.1)
                time.sleep(duree)
                mouse.press(Button.left)
                mouse.release(Button.left)

                time_sleep = uniform(0.55,0.57)
                time.sleep(time_sleep)

                while (pyautogui.locateOnScreen('../img/croix_rune.jpg', region=(1057, 393, 88, 79), confidence=0.8) == None):
                    x_click = x_range_tmp + 75
                    y_click = y_range + 83
                    x_click_add = randint(-35,35)
                    y_click_add = randint(-35,35)
                    x_click += x_click_add
                    y_click += y_click_add
                    mouse.position = (x_click, y_click)
                    duree = uniform(0.06,0.1)
                    time.sleep(duree)
                    mouse.press(Button.left)
                    mouse.release(Button.left)

                    time_sleep = uniform(0.45,0.47)
                    time.sleep(time_sleep)
                
                # subs = check_sub_before()

                subs_arr = get_subs_in_dj("before")
                subs = get_good_sub(subs_arr)
                # file_name = ""
                # for i in subs_arr:
                #     file_name = file_name + i + "_"

                # print(f'status subs = {subs}')
                if (subs > 0):
                    # take_screenshot_rune_kept_before2(file_name)
                    x_click = x_range_tmp + 75
                    y_click = y_range + 83
                    x_click_add = randint(-35,35)
                    y_click_add = randint(-35,35)
                    x_click += x_click_add
                    y_click += y_click_add
                    mouse.position = (x_click, y_click)
                    duree = uniform(0.06,0.1)
                    time.sleep(duree)
                    mouse.press(Button.left)
                    mouse.release(Button.left)
                # else:
                #     take_screenshot_rune_sold_before2(file_name)
                
            # print("Je vois rien")

            x_range_tmp = x_range_tmp + 140
            if (x == 1 and y == 2):
                break
        y_range = y_range + 140
        if (x == 1 and y == 2):
            break

def up_runes(rift_status):
    while (pyautogui.locateOnScreen('../img/vente_selective.png', region=(1406, 831, 356, 135)) == None):
        time_sleep = uniform(0.22,0.29)
        time.sleep(time_sleep)

    x_range = 1169
    y_range = 379
    for y in range (3):
        x_range_tmp = x_range
        for x in range (4):
            if (rift_status == 1):
                if ((x == 0 or x == 1 or x == 2) and y == 0):
                    x_range_tmp = x_range_tmp + 140
                    continue
            # pyautogui.moveTo(x_range_tmp, y_range, 0.45)
            # pyautogui.moveTo(x_range_tmp + 154, y_range + 167, 0.45)
            if ((pyautogui.locateOnScreen('../img/rune_heroique.jpg', region=(x_range_tmp, y_range, 154, 167), confidence=0.85)
                or pyautogui.locateOnScreen('../img/rune_legendaire.jpg', region=(x_range_tmp, y_range, 154, 167), confidence=0.85))
                and pyautogui.locateOnScreen('../img/rune_sold2.jpg', region=(x_range_tmp, y_range, 154, 167), confidence=0.4) == None):
                # print("----------------------------------------------------------------------------------------")

                x_click = x_range_tmp + 75
                y_click = y_range + 83
                x_click_add = randint(-35,35)
                y_click_add = randint(-35,35)
                x_click += x_click_add
                y_click += y_click_add
                mouse.position = (x_click, y_click)
                duree = uniform(0.06,0.1)
                time.sleep(duree)
                mouse.press(Button.left)
                mouse.release(Button.left)

                time_sleep = uniform(0.34,0.36)
                time.sleep(time_sleep)
                
                while (pyautogui.locateOnScreen('../img/ameliorer.jpg', region=(931, 683, 300, 178), confidence=0.8) == None):
                    x_click = x_range_tmp + 75
                    y_click = y_range + 83
                    x_click_add = randint(-35,35)
                    y_click_add = randint(-35,35)
                    x_click += x_click_add
                    y_click += y_click_add
                    mouse.position = (x_click, y_click)
                    duree = uniform(0.06,0.1)
                    time.sleep(duree)
                    mouse.press(Button.left)
                    mouse.release(Button.left)

                    time_sleep = uniform(0.52,0.54)
                    time.sleep(time_sleep)

                # while (pyautogui.locateOnScreen('../img/ameliorer.jpg', region=(931, 683, 300, 178), confidence=0.9) == None):
                #     time_sleep = uniform(0.22,0.29)
                #     time.sleep(time_sleep)
                
                subs = check_sub_after()
                # subs_arr = get_subs_in_dj("after")
                # subs = get_good_sub(subs_arr)
                # file_name = ""
                # for i in subs_arr:
                #     file_name = file_name + i + "_"
                # take_screenshot_rune_kept_after2(file_name)

                x_click = randint(979,1191)
                y_click = randint(738,814)
                mouse.position = (x_click, y_click)
                duree = uniform(0.06,0.1)
                time.sleep(duree)
                mouse.press(Button.left)
                mouse.release(Button.left)
                
                while (pyautogui.locateOnScreen('../img/amelioration_rune.jpg', region=(303, 566, 774, 222), confidence=0.9) == None):
                    time_sleep = uniform(0.22,0.29)
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

                if (subs == 1):
                    x_click = randint(709,824)
                    y_click = randint(486,577)
                    mouse.position = (x_click, y_click)
                    duree = uniform(0.06,0.1)
                    time.sleep(duree)
                    mouse.press(Button.left)
                    mouse.release(Button.left)
                
                if (subs == 2 or subs == 3):
                    x_click = randint(880,993)
                    y_click = randint(482,582)
                    mouse.position = (x_click, y_click)
                    duree = uniform(0.06,0.1)
                    time.sleep(duree)
                    mouse.press(Button.left)
                    mouse.release(Button.left)

                if (subs == 4):
                    x_click = randint(1050,1163)
                    y_click = randint(482,578)
                    mouse.position = (x_click, y_click)
                    duree = uniform(0.06,0.1)
                    time.sleep(duree)
                    mouse.press(Button.left)
                    mouse.release(Button.left)

                time_sleep = uniform(0.32,0.34)
                time.sleep(time_sleep)

                x_click = randint(660,875)
                y_click = randint(690,765)
                mouse.position = (x_click, y_click)
                duree = uniform(0.06,0.1)
                time.sleep(duree)
                mouse.press(Button.left)
                mouse.release(Button.left)

                while (pyautogui.locateOnScreen('../img/fermer_rune.jpg', region=(766, 862, 342, 181), confidence=0.9) == None):
                    time_sleep = uniform(0.22,0.29)
                    time.sleep(time_sleep)

                time_sleep = uniform(0.32,0.34)
                time.sleep(time_sleep)

                x_click = randint(821,1059)
                y_click = randint(921,983)
                mouse.position = (x_click, y_click)
                duree = uniform(0.06,0.1)
                time.sleep(duree)
                mouse.press(Button.left)
                mouse.release(Button.left)

                
                while (pyautogui.locateOnScreen('../img/croix_rune.jpg', region=(1217, 175, 172, 133), confidence=0.9) == None):
                    time_sleep = uniform(0.22,0.29)
                    time.sleep(time_sleep)

                time_sleep = uniform(0.32,0.34)
                time.sleep(time_sleep)

                x_click = randint(1268,1298)
                y_click = randint(230,259)
                mouse.position = (x_click, y_click)
                duree = uniform(0.06,0.1)
                time.sleep(duree)
                mouse.press(Button.left)
                mouse.release(Button.left)

            x_range_tmp = x_range_tmp + 140
            if (rift_status == 0):
                if (x == 1 and y == 2):
                    break
        y_range = y_range + 140
        if (rift_status == 0):
            if (x == 1 and y == 2):
                break

def get_slot():
    pyt.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract"

    img = pyautogui.screenshot(region=(1009, 265, 536, 56)) # toutes les lignes

    img2 = np.array(img)
    
    img2 = cv2.resize(img2, (0, 0), fx=2, fy=2)

    # Convert to HSV color-space
    hsv = cv2.cvtColor(img2, cv2.COLOR_BGR2HSV)

    # Get the binary mask
    msk = cv2.inRange(hsv, np.array([0, 0, 123]), np.array([179, 255, 255]))

    text = pyt.image_to_string(msk)
    return text[-3:-2]

def get_grade():
    if (pyautogui.locateOnScreen('../img/heroic_rune.jpg', region=(1070, 269, 275, 107), confidence=0.95)):
        return "heroic"
    return "legend"

def take_screenshot_rune_kept_up(name):
    pyautogui.screenshot('../runes_gardees/' + name + str(round(randint(0, sys.maxsize), 5)) + '7' + str(round(randint(0, sys.maxsize), 5)) + '.png')

def take_screenshot_rune_sold_up(name):
    pyautogui.screenshot('../runes_vendues/' + name + str(round(randint(0, sys.maxsize), 5)) + '7' + str(round(randint(0, sys.maxsize), 5)) + '.png')

def is_subs_fully_printed():
    pyt.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract"

    img = pyautogui.screenshot(region=(1036, 464, 284, 183)) # toutes les lignes

    img2 = np.array(img)

    img2 = cv2.resize(img2, (0, 0), fx=2, fy=2)

    # Convert to HSV color-space
    hsv = cv2.cvtColor(img2, cv2.COLOR_BGR2HSV)

    # Get the binary mask
    msk = cv2.inRange(hsv, np.array([0, 0, 123]), np.array([179, 255, 255]))

    text = pyt.image_to_string(msk)

    split_text = text.split()

    nb_plus = 0
    for i in range(len(split_text)):
            if (split_text[i].find('+')):
                    nb_plus = nb_plus + 1
    if (nb_plus == 3):
            return 1
    return 0

def rune_process_new(rune_data):

    while (is_subs_fully_printed()):
        time_sleep = uniform(0.15,0.18)
        time.sleep(time_sleep)

    # time_sleep = uniform(2.8,2.9) # A CHANGER ET METTRE UN WHILE AVEC UNE CONDITION ?
    # time.sleep(time_sleep)

    # good_sub = get_good_sub(subs)
    # print(f'good sub = {good_sub}')
    subs = get_subs_new()
    amelioration = get_amelioration()
    slot = get_slot()
    # print(f'amelioration = {amelioration}')
    # print(f'slot = {slot}')
    # print(f'grade = {grade}')
    up_rune, eff = check_sell(rune_data, subs, amelioration, slot)
    name_picture = "up_rune_"
    eff_rounded = round(eff, 3)
    name_picture = name_picture + str(eff_rounded) + "_"
    name_picture = name_picture + "amel" + str(amelioration) + "_"
    name_picture = name_picture + "slot" + str(slot) + "_"
    name_picture = name_picture + str(rune_data["grade"]) + "_"
    for i in subs:
        name_picture = name_picture + i + "_"
    # print(f'name ===================== {name_picture}')
    
    if (up_rune == 1 and amelioration == 6):
        # click sur ok
        x_click = randint(1014,1252)
        y_click = randint(887,955)
        mouse.position = (x_click, y_click)
        duree = uniform(0.06,0.1)
        time.sleep(duree)
        mouse.press(Button.left)
        mouse.release(Button.left)

        while (pyautogui.locateOnScreen('../img/amelioration_rune.jpg', region=(480, 751, 438, 139), confidence=0.9) == None):
            time_sleep = uniform(0.22,0.29)
            time.sleep(time_sleep)

        while (pyautogui.locateOnScreen('../img/plus_9.jpg', region=(419, 566, 600, 133), confidence=0.95) == None):
            x_click = randint(668,757)
            y_click = randint(605,664)
            mouse.position = (x_click, y_click)
            duree = uniform(0.06,0.1)
            time.sleep(duree)
            mouse.press(Button.left)
            mouse.release(Button.left)

            time_sleep = uniform(0.37,0.41)
            time.sleep(time_sleep)

        time_sleep = uniform(0.32,0.34)
        time.sleep(time_sleep)

        x_click = randint(579,857)
        y_click = randint(789,850)
        mouse.position = (x_click, y_click)
        duree = uniform(0.06,0.1)
        time.sleep(duree)
        mouse.press(Button.left)
        mouse.release(Button.left)

        while (pyautogui.locateOnScreen('../img/resultat_amelioration.jpg', region=(705, 65, 540, 149), confidence=0.9) == None):
            time_sleep = uniform(0.22,0.29)
            time.sleep(time_sleep)

        rune_process_new(rune_data)

    elif (up_rune == 1 and amelioration == 9):
        # click sur ok
        x_click = randint(1014,1252)
        y_click = randint(887,955)
        mouse.position = (x_click, y_click)
        duree = uniform(0.06,0.1)
        time.sleep(duree)
        mouse.press(Button.left)
        mouse.release(Button.left)

        while (pyautogui.locateOnScreen('../img/amelioration_rune.jpg', region=(480, 751, 438, 139), confidence=0.9) == None):
            time_sleep = uniform(0.22,0.29)
            time.sleep(time_sleep)

        while (pyautogui.locateOnScreen('../img/plus_12.jpg', region=(419, 566, 600, 133), confidence=0.95) == None):
            x_click = randint(781,870)
            y_click = randint(606,663)
            mouse.position = (x_click, y_click)
            duree = uniform(0.06,0.1)
            time.sleep(duree)
            mouse.press(Button.left)
            mouse.release(Button.left)

            time_sleep = uniform(0.37,0.41)
            time.sleep(time_sleep)

        time_sleep = uniform(0.32,0.34)
        time.sleep(time_sleep)

        x_click = randint(579,857)
        y_click = randint(789,850)
        mouse.position = (x_click, y_click)
        duree = uniform(0.06,0.1)
        time.sleep(duree)
        mouse.press(Button.left)
        mouse.release(Button.left)


        while (pyautogui.locateOnScreen('../img/resultat_amelioration.jpg', region=(705, 65, 540, 149), confidence=0.9) == None):
            time_sleep = uniform(0.22,0.29)
            time.sleep(time_sleep)

        rune_process_new(rune_data)

    elif ((up_rune == 1 and amelioration == 12) or amelioration == 15):
        # click sur ok
        take_screenshot_rune_kept_up(name_picture)
        x_click = randint(1014,1252)
        y_click = randint(887,955)
        mouse.position = (x_click, y_click)
        duree = uniform(0.06,0.1)
        time.sleep(duree)
        mouse.press(Button.left)
        mouse.release(Button.left)

        while (pyautogui.locateOnScreen('../img/amelioration_rune.jpg', region=(480, 751, 438, 139), confidence=0.95) == None):
            time_sleep = uniform(0.22,0.29)
            time.sleep(time_sleep)

        while (pyautogui.locateOnScreen('../img/amelioration_rune.jpg', region=(480, 751, 438, 139), confidence=0.9)):
            x_click = randint(1528,1590)
            y_click = randint(109,163)
            mouse.position = (x_click, y_click)
            duree = uniform(0.06,0.1)
            time.sleep(duree)
            mouse.press(Button.left)
            mouse.release(Button.left)

            time_sleep = uniform(0.37,0.41)
            time.sleep(time_sleep)

        while (pyautogui.locateOnScreen('../img/croix_rune.jpg', region=(1217, 175, 172, 133), confidence=0.9) == None):
            time_sleep = uniform(0.22,0.29)
            time.sleep(time_sleep)

        time_sleep = uniform(0.32,0.34)
        time.sleep(time_sleep)

        x_click = randint(1268,1298)
        y_click = randint(230,259)
        mouse.position = (x_click, y_click)
        duree = uniform(0.06,0.1)
        time.sleep(duree)
        mouse.press(Button.left)
        mouse.release(Button.left)

    elif (up_rune == 0):
        take_screenshot_rune_sold_up(name_picture)
        x_click = randint(714,952)
        y_click = randint(887,958)
        mouse.position = (x_click, y_click)
        duree = uniform(0.06,0.1)
        time.sleep(duree)
        mouse.press(Button.left)
        mouse.release(Button.left)

        while (pyautogui.locateOnScreen('../img/amelioration_rune.jpg', region=(480, 751, 438, 139), confidence=0.95) == None):
            if (pyautogui.locateOnScreen('../img/vendre_rune_plus_12.jpg', region=(463, 244, 964, 346), confidence=0.9)):
                x_click = randint(673,893)
                y_click = randint(655,737)
                mouse.position = (x_click, y_click)
                duree = uniform(0.06,0.1)
                time.sleep(duree)
                mouse.press(Button.left)
                mouse.release(Button.left)
            time_sleep = uniform(0.22,0.29)
            time.sleep(time_sleep)

        while (pyautogui.locateOnScreen('../img/amelioration_rune.jpg', region=(480, 751, 438, 139), confidence=0.9)):
            x_click = randint(1528,1590)
            y_click = randint(109,163)
            mouse.position = (x_click, y_click)
            duree = uniform(0.06,0.1)
            time.sleep(duree)
            mouse.press(Button.left)
            mouse.release(Button.left)

            time_sleep = uniform(0.37,0.41)
            time.sleep(time_sleep)

def new_up_runes(data):
    while (pyautogui.locateOnScreen('../img/vente_selective.png', region=(1406, 831, 356, 135)) == None):
        time_sleep = uniform(0.22,0.29)
        time.sleep(time_sleep)

    x_range = 1169
    y_range = 379
    for y in range (3):
        x_range_tmp = x_range
        for x in range (4):
            # pyautogui.moveTo(x_range_tmp, y_range, 0.45)
            # pyautogui.moveTo(x_range_tmp + 154, y_range + 167, 0.45)
            # x_range_tmp = x_range_tmp + 140
            # continue

            if ((pyautogui.locateOnScreen('../img/rune_heroique.jpg', region=(x_range_tmp, y_range, 154, 167), confidence=0.85)
                or pyautogui.locateOnScreen('../img/rune_legendaire.jpg', region=(x_range_tmp, y_range, 154, 167), confidence=0.85))
                and pyautogui.locateOnScreen('../img/rune_sold2.jpg', region=(x_range_tmp, y_range, 154, 167), confidence=0.4) == None):

                x_click = x_range_tmp + 75
                y_click = y_range + 83
                x_click_add = randint(-35,35)
                y_click_add = randint(-35,35)
                x_click += x_click_add
                y_click += y_click_add
                mouse.position = (x_click, y_click)
                duree = uniform(0.06,0.1)
                time.sleep(duree)
                mouse.press(Button.left)
                mouse.release(Button.left)

                time_sleep = uniform(0.34,0.36)
                time.sleep(time_sleep)
                
                while (pyautogui.locateOnScreen('../img/ameliorer.jpg', region=(931, 683, 300, 178), confidence=0.8) == None):
                    x_click = x_range_tmp + 75
                    y_click = y_range + 83
                    x_click_add = randint(-35,35)
                    y_click_add = randint(-35,35)
                    x_click += x_click_add
                    y_click += y_click_add
                    mouse.position = (x_click, y_click)
                    duree = uniform(0.06,0.1)
                    time.sleep(duree)
                    mouse.press(Button.left)
                    mouse.release(Button.left)

                    if (pyautogui.locateOnScreen('../img/rune_ok.jpg', region=(775, 679, 320, 191), confidence=0.9)
                        or pyautogui.locateOnScreen('../img/reachat.jpg', region=(775, 679, 320, 191), confidence=0.9)):
                        break      

                    time_sleep = uniform(0.52,0.54)
                    time.sleep(time_sleep)
                
                if (pyautogui.locateOnScreen('../img/rune_ok.jpg', region=(775, 679, 320, 191), confidence=0.9)
                        or pyautogui.locateOnScreen('../img/reachat.jpg', region=(775, 679, 320, 191), confidence=0.9)):
                    x_click = randint(1268,1298)
                    y_click = randint(230,259)
                    mouse.position = (x_click, y_click)
                    duree = uniform(0.06,0.1)
                    time.sleep(duree)
                    mouse.press(Button.left)
                    mouse.release(Button.left)
                    x_range_tmp = x_range_tmp + 140

                    continue
                
                # subs = check_sub_after()

                data["rune_properties"]["grade"] = get_grade()
                subs_arr = get_subs_in_dj("after")
                subs = get_good_sub(subs_arr)
                # file_name = ""
                # for i in subs_arr:
                #     file_name = file_name + i + "_"
                # take_screenshot_rune_kept_after2(file_name)

                x_click = randint(979,1191)
                y_click = randint(738,814)
                mouse.position = (x_click, y_click)
                duree = uniform(0.06,0.1)
                time.sleep(duree)
                mouse.press(Button.left)
                mouse.release(Button.left)
                
                while (pyautogui.locateOnScreen('../img/amelioration_rune.jpg', region=(480, 751, 438, 139), confidence=0.9) == None):
                    time_sleep = uniform(0.22,0.29)
                    time.sleep(time_sleep)

                if (subs == 1):
                    while (pyautogui.locateOnScreen('../img/plus_6.jpg', region=(419, 566, 600, 133), confidence=0.95) == None):
                        x_click = randint(556,647)
                        y_click = randint(607,662)
                        mouse.position = (x_click, y_click)
                        duree = uniform(0.06,0.1)
                        time.sleep(duree)
                        mouse.press(Button.left)
                        mouse.release(Button.left)

                        time_sleep = uniform(0.37,0.41)
                        time.sleep(time_sleep)
                
                if (subs == 2 or subs == 3):
                    while (pyautogui.locateOnScreen('../img/plus_9.jpg', region=(419, 566, 600, 133), confidence=0.95) == None):
                        x_click = randint(668,757)
                        y_click = randint(605,664)
                        mouse.position = (x_click, y_click)
                        duree = uniform(0.06,0.1)
                        time.sleep(duree)
                        mouse.press(Button.left)
                        mouse.release(Button.left)

                        time_sleep = uniform(0.37,0.41)
                        time.sleep(time_sleep)

                if (subs == 4):
                    while (pyautogui.locateOnScreen('../img/plus_12.jpg', region=(419, 566, 600, 133), confidence=0.95) == None):
                        x_click = randint(781,870)
                        y_click = randint(606,663)
                        mouse.position = (x_click, y_click)
                        duree = uniform(0.06,0.1)
                        time.sleep(duree)
                        mouse.press(Button.left)
                        mouse.release(Button.left)

                        time_sleep = uniform(0.37,0.41)
                        time.sleep(time_sleep)

                time_sleep = uniform(0.32,0.34)
                time.sleep(time_sleep)

                x_click = randint(579,857)
                y_click = randint(789,850)
                mouse.position = (x_click, y_click)
                duree = uniform(0.06,0.1)
                time.sleep(duree)
                mouse.press(Button.left)
                mouse.release(Button.left)


                while (pyautogui.locateOnScreen('../img/resultat_amelioration.jpg', region=(705, 65, 540, 149), confidence=0.9) == None):
                    time_sleep = uniform(0.22,0.29)
                    time.sleep(time_sleep)

                rune_process_new(data["rune_properties"])

            x_range_tmp = x_range_tmp + 140
            if (x == 1 and y == 2):
                break
        y_range = y_range + 140
        if (x == 1 and y == 2):
            break