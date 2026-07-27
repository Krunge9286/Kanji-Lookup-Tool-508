from app.enums import *; from user_input import *; from app.kana import *

class Kanji:
    def __init__(self,
                 user_input: UserInput,
                 form: str,
                 kana: Kana,
                 meaning: str,
                 unicode: str,
                 max_mora: int,
                 min_mora: int,
                 stroke_count: int,
                 max_efficiency: float,
                 min_efficiency: float,
                 user_label: UserLabel = None,
                 kunyomi_readings: list[str] = None,
                 onyomi_readings: list[str] = None,
                 nanori_readings: list[str] = None):
        self.user_input = user_input
        self.form = form
        self. kana = kana
        self. meaning = meaning
        self.unicode = unicode
        self.max_mora = max_mora
        self.min_mora = min_mora
        self.stroke_count = stroke_count
        self.max_efficiency = max_efficiency
        self.min_efficiency = min_efficiency
        self.user_label = user_label
        self.kunyomi_readings = kunyomi_readings
        self.onyomi_readings = onyomi_readings
        self.nanori_readings = nanori_readings


