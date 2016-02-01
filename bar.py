# Module to sort out the upper status bar

# Battery level bitmaps
bat = [
    [126, 66, 66, 66, 66, 66, 66, 66, 126, 60, 0],
    [126, 66, 90, 66, 66, 66, 66, 66, 126, 60, 0],
    [126, 66, 90, 66, 90, 66, 66, 66, 126, 60, 0],
    [126, 66, 90, 66, 90, 66, 90, 66, 126, 60, 0]
    ]

# Signal level bitmaps
sig = [
    [66, 66, 36, 24, 24, 36, 66, 66, 0],
    [96, 96, 0, 0, 0, 0, 0, 0, 0],
    [96, 96, 0, 120, 120, 0, 0, 0, 0],
    [96, 96, 0, 120, 120, 0, 126, 126, 0]
]


def bat_disp(lcd, level=3):
    lcd.position(74, 0)
    lcd.data(bat[level])
    lcd.position(0, 0)

def sig_disp(lcd, level=3):
    lcd.position(64, 0)
    lcd.data(sig[level])
    lcd.position(0, 0)

