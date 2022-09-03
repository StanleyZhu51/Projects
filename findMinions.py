import numpy as np
import cv2 as cv
import pyautogui
from Numbers import Num
import os

def find_minion_2():
    # templates = [cv.imread('templates/62.png'), cv.imread('templates/61.png'), cv.imread('templates/60.png')]
    image = pyautogui.screenshot()
    image.save(r'C:\Users\stanl\PycharmProjects\CSTrainer\image.png')

    image = cv.imread('image.png')
    temp = cv.imread('tinyTemp.png')

    threshold = 0.99
    result = cv.matchTemplate(image, temp, cv.TM_CCOEFF_NORMED)
    minionLoc = np.where(result >= threshold)
    return len(minionLoc[0]), image


def findCS(templates, image):
    # finding cs
    threshold = 0.99
    digit = 0
    counter = 0
    a = Num()
    b = Num()
    c = Num()
    abc = [a, b, c]

    for number in templates:
        x = 0
        result = cv.matchTemplate(image, number, cv.TM_CCOEFF_NORMED)
        csLoc = np.where(result >= threshold)
        # fill abc out
        locList = csLoc[1].tolist()
        if len(locList) != 0:
            for y in abc:
                if counter == len(locList):
                    counter = 0
                    break
                if not y.get_TF():
                    y.set_number(digit)
                    y.set_coord(locList[x])
                    y.set_TF(True)
                    x = x + 1
                    counter = counter + 1
        digit = digit + 1

    smallCoord = 1000000
    smallVal = 0
    bigCoord = 0
    bigVal = 0
    digitCount = 0
    # 100ths place
    for y in abc:
        if y.get_TF():
            digitCount = digitCount + 1
            if y.get_coord() < smallCoord:
                smallCoord = y.get_coord()
                bigVal = y.get_number()

    # ones place
    for y in abc:
        if y.get_TF():
            if y.get_coord() > bigCoord:
                bigCoord = y.get_coord()
                smallVal = y.get_number()
    # tens place
    middleVal = 0
    for y in abc:
        if y.get_coord() != smallCoord and y.get_coord() != bigCoord:
            middleVal = y.get_number()
    # return CS value
    if digitCount == 1:
        return smallVal
    elif digitCount == 2:
        return smallVal + 10 * bigVal
    else:
        return smallVal + middleVal * 10 + bigVal * 100

