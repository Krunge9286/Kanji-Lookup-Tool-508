import db.mysql_repository
from model.kana import *


class Services:
    def __init__(self):
        self.repo = db.mysql_repository.MysqlRepository()

    # Use case 1: the app takes a kanji character
    # and returns information about that kanji
    def get_kanji_info(self, input_form):
        if len(input_form) != 1:
            raise ValueError("Input must be a single kanji character.")
        if input_form in hiragana:
           raise ValueError("Input must be a kanji character, not a hiragana character")
        if input_form in katakana:
           raise ValueError("Input must be a kanji character, not a katakana character")
        if input_form.lower() in letters:
           raise ValueError("Input must be a kanji character, not a roman character")
        kanji = self.repo.get_kanji(input_form)
        return kanji

    # use case 3: return the maximum and minimum "efficiency" scores of a kanji
    def get_efficiency_scores(self, kanji):
        readings = (
                kanji.onyomi_readings
                + kanji.kunyomi_readings
                + kanji.nanori_readings
        )
        valid_readings = [reading for reading in readings if reading != ""]
        shortened_readings = [reading.split(".")[0] for reading in valid_readings]
        max_mora = max(len(reading) for reading in shortened_readings)
        min_mora = min(len(reading) for reading in shortened_readings)
        max_efficiency = round((max_mora / kanji.stroke_count), 3)
        min_efficiency = round((min_mora / kanji.stroke_count), 3)
        return f"Minimum Efficiency: {min_efficiency}; Maximum Efficiency: {max_efficiency}"
      
