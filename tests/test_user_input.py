from app.user_input import *
import pytest


def test_user_input_kana():
    hir_1 = UserInput("か")
    kat_1 = UserInput("カ")
    rom_1 = UserInput("ka")
    assert hir_1.kana == Kana.HIRAGANA
    assert kat_1.kana == Kana.KATAKANA
    assert rom_1.kana == Kana.ROMAJI

def test_bad_user_input():
    try:
        UserInput("qx")
        assert False, "Expected ValueError to be raised."
    except ValueError as e:
        assert str(e) == "Not a valid search string."


