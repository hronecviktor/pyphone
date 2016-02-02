# Keypad 1-8 connected to Y1 - Y8
# 1-4 columns from left
# 5-8 rows from top

from pyb import Pin, udelay, delay


class Keypad(object):

    def __init__(self, row_pins, col_pins, mapping, set_udelay=15):
        self._row_pins = []
        for row_pin in row_pins:
            pin = Pin(row_pin, mode=Pin.OUT_PP)
            pin.init(mode=Pin.OUT_PP)
            pin.low()
            self._row_pins.append(pin)
        self._col_pins = []
        for col_pin in col_pins:
            pin = Pin(col_pin, mode=Pin.IN)
            pin.init(mode=Pin.IN, pull=Pin.PULL_DOWN)
            self._col_pins.append(pin)
        self._udelay = set_udelay
        self._mapping = mapping

    def get(self):
        for row_index, row_pin in enumerate(self._row_pins):
            row_pin.high()
            udelay(self._udelay)
            for col_index, col_pin in enumerate(self._col_pins):
                if col_pin.value():
                    row_pin.low()
                    return self._mapping[row_index][col_index]
            row_pin.low()
            udelay(self._udelay)
        return None



