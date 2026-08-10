from app.services import *
from db.mysql_repository import *
import pytest


services = Services()
repo = MysqlRepository()

info = services.get_kanji_info("畳")

def test_get_kanji_info_valid():
    assert info.form == '畳'
    assert info.stroke_count == 12
    assert info.unicode_value == '7573'
    assert info.onyomi_readings == ['ジョウ', 'チョウ']
    assert info.kunyomi_readings == ['たた.む', 'たたみ', 'かさ.なる']
    assert info.nanori_readings == ['']
    assert info.meanings == ['tatami mat', 'counter for tatami mats', 'fold', 'shut up', 'do away with']

def test_get_kanji_info_invalid():
    with pytest.raises(ValueError):
        services.get_kanji_info('あ')
    with pytest.raises(ValueError):
        services.get_kanji_info('ア')
    with pytest.raises(ValueError):
        services.get_kanji_info('a')
    with pytest.raises(ValueError):
        services.get_kanji_info('A')
    with pytest.raises(ValueError):
        services.get_kanji_info('海流')

def test_get_efficiency_scores():
    scores = services.get_efficiency_scores(info)
    assert scores == 'Minimum Efficiency: 0.167; Maximum Efficiency: 0.25'
  
