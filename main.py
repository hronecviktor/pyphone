# main.py -- put your code here!

from machine import SPI, Pin
import pyb
import upcd8544
import bar

import pyb
import upcd8544
import bar
from keypad import Keypad


SPI    = SPI(1)
RST    = Pin('X4')
CE     = Pin('X5')
DC     = Pin('X7')
LIGHT  = Pin('X3')

lcd = upcd8544.PCD8544(SPI, RST, CE, DC, LIGHT)

bar.bat_disp(lcd, level=3)
pyb.delay(500)
bar.sig_disp(lcd, level=3)

kp = Keypad(('Y5', 'Y6', 'Y7', 'Y8'), ('Y1', 'Y2', 'Y3', 'Y4'))
while True:
    data = kp.get()
    if data:
        bt = data[0] * data[1] * 16
        print(bt)
        lcd.data([bt])