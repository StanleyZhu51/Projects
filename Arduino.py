import serial
import time


def send(arduino):
    arduino.write(bytes('1', 'utf-8'))
    time.sleep(0.05)
    data = arduino.readline()
    return data

