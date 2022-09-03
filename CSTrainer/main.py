from findMinions import findCS
from findMinions import find_minion_2
from Arduino import send
import keyboard
import cv2 as cv
import timeit, functools
import serial
from playsound import playsound

#arduino = serial.Serial(port='COM4', baudrate=115200, timeout=.1)
zeroCS = cv.imread('zero.png')
oneCS = cv.imread('one.png')
twoCS = cv.imread('two.png')
threeCS = cv.imread('three.png')
fourCS = cv.imread('four.png')
fiveCS = cv.imread('five.png')
sixCS = cv.imread('six.png')
sevenCS = cv.imread('seven.png')
eightCS = cv.imread('eight.png')
nineCS = cv.imread('nine.png')
numbersTemp = [zeroCS, oneCS, twoCS, threeCS, fourCS, fiveCS, sixCS, sevenCS, eightCS, nineCS]
oldMinion = 0
newMinion = 0
oldCS = 0
newCS = 0
# start program via keypress
while True:
    if keyboard.read_key() == "s":
        print('start')
        break

while True:
    oldMinion = newMinion
    oldCS = newCS
    # obtain new var values
    newMinion, image = find_minion_2()
    newCS = findCS(numbersTemp, image)
    #tme = timeit.Timer(functools.partial(findCS, numbersTemp, image))
    #print(tme.timeit(1))
    #tme = timeit.Timer(functools.partial(send, arduino))
    #print(tme.timeit(1))
    if newMinion < oldMinion:
        if newCS > oldCS:
            print('good')
        else:
            print('bad')
            playsound(r'C:\Users\stanl\PycharmProjects\CSTrainer\damage.wav')
            #print(send(arduino))

