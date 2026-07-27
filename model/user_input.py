from app.enums import *
from app.kana import *


class UserInput:
    def __init__(self,
                 user_input: str,
                 kana: Kana = None,
                 user_label: UserLabel = None):
        self.user_input = user_input
        self.kana = kana
        self.user_label = user_label
        self.get_kana()

    def get_kana(self):
        if all(character in hiragana for character in self.user_input):
            self.kana = Kana.HIRAGANA
        elif all(character in katakana for character in self.user_input):
            self.kana = Kana.KATAKANA
        elif all(character in letters for character in self.user_input):
            self.kana = Kana.ROMAJI
        else:
            raise ValueError("Not a valid search string.")


