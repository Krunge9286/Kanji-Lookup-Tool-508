from model.enums import *

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

    def get_json(self) -> dict:
        return {
            "form": self.form,
            "meanings": self.meanings,
            "unicode_value": self.unicode_value,
            "stroke_count": self.stroke_count,
            "kunyomi_readings": self.kunyomi_readings,
            "onyomi_readings": self.onyomi_readings,
            "nanori_readings": self.nanori_readings
        }

