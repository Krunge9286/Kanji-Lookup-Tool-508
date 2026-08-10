from db.mysql_repository import *


repo = MysqlRepository()
test_row = {
    "form": "畳",
    "meanings": "tatami mat;fold",
    "unicode_value": "7573",
    "stroke_count": 12,
    "kunyomi_readings": "たたみ;たた.む",
    "onyomi_readings": "ジョウ",
    "nanori_readings": ""
            }
test_kanji = repo.get_kanji("畳")


def test_mapper():
    kanji = repo.mapper(test_row)
    assert kanji.form == test_row["form"]
    assert kanji.meanings == test_row["meanings"].split(";")
    assert kanji.unicode_value == test_row["unicode_value"]
    assert kanji.stroke_count == test_row["stroke_count"]
    assert kanji.kunyomi_readings == test_row["kunyomi_readings"].split(";")
    assert kanji.onyomi_readings == test_row["onyomi_readings"].split(";")
    assert kanji.nanori_readings == test_row["nanori_readings"].split(";")

def test_get_kanji():
    assert test_kanji is not None
    assert test_kanji.form == "畳"
