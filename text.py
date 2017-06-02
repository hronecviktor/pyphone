__all__ = ["chars", "TextWriter"]
chars = {
    "a": [240, 40, 40, 240, 0],
    "b": [248, 168, 168, 80, 0],
    "c": [112, 136, 136, 136, 0],
    "d": [248, 136, 136, 112, 0],
    "e": [248, 168, 168, 0],
    "f": [248, 40, 8, 0],
    "g": [112, 136, 168, 232, 0],
    "h": [248, 32, 32, 248, 0],
    "i": [248, 0],
    "j": [64, 128, 128, 120, 0],
    "k": [248, 32, 80, 136, 0],
    "l": [248, 128, 128, 0],
    "m": [248, 16, 32, 16, 248, 0],
    "n": [248, 16, 32, 248, 0],
    "o": [112, 136, 136, 112, 0],
    "p": [248, 40, 40, 16, 0],
    "q": [112, 136, 72, 176, 0],
    "r": [248, 40, 104, 144, 0],
    "s": [144, 168, 168, 72, 0],
    "t": [8, 8, 248, 8, 8, 0],
    "u": [120, 128, 128, 120, 0],
    "v": [24, 96, 128, 96, 24, 0],
    "w": [56, 192, 56, 192, 56, 0],
    "x": [216, 32, 32, 216, 0],
    "y": [184, 160, 160, 120, 0],
    "z": [200, 168, 168, 152, 0],
    "0": [112, 136, 136, 112, 0],
    "1": [136, 248, 128, 0],
    "2": [144, 200, 168, 144, 0],
    "3": [136, 168, 168, 80, 0],
    "4": [96, 80, 72, 248, 0],
    "5": [184, 168, 168, 104, 0],
    "6": [112, 168, 168, 64, 0],
    "7": [8, 8, 232, 24, 0],
    "8": [80, 168, 168, 80, 0],
    "9": [16, 168, 168, 112, 0],
    "(": [112, 136, 0],
    ")": [136, 112, 0],
    ".": [192, 192, 0],
    ",": [128, 96, 0],
    "!": [184, 0],
    "?": [8, 168, 24, 0],
    "+": [32, 112, 32, 0],
    "-": [32, 32, 0],
    ":": [80, 0],
    "*": [80, 32, 80, 0],
    "'": [24, 0],
    "`": [40, 24, 0],
    "#": [80, 248, 80, 248, 80, 0],
    " ": [0, 0, 0]
}


class TextWriter(object):
    # consts for vertical positioning withing line
    POS_LOW = 0
    POS_MID = 2
    POS_HIGH = 3

    # consts for text over/underlining
    DECO_UNDERLINE = 128
    DECO_OVERLINE = 1

    def __init__(self, lcd):
        self.lcd = lcd

    def _write_raw(self, text, raise_=False):
        text = text.lower()
        if not raise_:
            characters = [chars.get(ch, chars["#"]) for ch in text]
        else:
            characters = [chars[ch] for ch in text]
        self.lcd.data(*characters)

    def write(self, text, row=0, offset=0, position=POS_MID):
        self.lcd.position(offset, row)
        # check for non-defined characters
        for char in text:
            assert char in chars
        length = 0
        for char in text:
            length += len(chars[char])
        # stub
