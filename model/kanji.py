from app.enums import *

class Kanji:
    def __init__(self,
                 form: str,
                 meanings: list[str],
                 unicode_value: str,
                 stroke_count: int,
                 kunyomi_readings: list[str] = None,
                 onyomi_readings: list[str] = None,
                 nanori_readings: list[str] = None):
        self.form = form
        self.meanings = meanings
        self.unicode_value = unicode_value
        self.stroke_count = stroke_count
        self.kunyomi_readings = kunyomi_readings
        self.onyomi_readings = onyomi_readings
        self.nanori_readings = nanori_readings


