import machine

import time
from machine import UART

serial = UART(0, baudrate=115200)

serial.init(bits=8, parity=None, stop=1)

while True:
    time.sleep(0.2)
    if serial.any():
        data = serial.read()
        if data == b'a':
            print("data on")
        elif data == b'b':
            print("data off")