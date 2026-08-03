from db.mysql_repository import *

# repo = MysqlRepository()
# test_kanji = '畳'

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
    assert kanji.form == "畳"
    assert kanji.meanings == ["tatami mat", "fold"]
    assert kanji.kunyomi_readings == ["たたみ", "たた.む"]
    assert kanji.onyomi_readings == ["ジョウ"]

def test_get_kanji():
    assert test_kanji is not None
    assert test_kanji.form == "畳"
