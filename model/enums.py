from enum import Enum


class UserLabel(Enum):
    LEARNED          = 1
    HAVE_NOT_LEARNED = 2
    LEARNING         = 3

class Kana(Enum):
     HIRAGANA = 1
     KATAKANA = 2
     ROMAJI   = 3
     LETTERS  = 4
