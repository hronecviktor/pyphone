from machine import SPI, Pin

SPI    = SPI(1)
RST    = Pin('X4')
CE     = Pin('X5')
DC     = Pin('X7')
LIGHT  = Pin('X3')

import upcd8544

lcd = upcd8544.PCD8544(SPI, RST, CE, DC, LIGHT)

lcd.data([0xff])