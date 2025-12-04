from task1 import Alphabet, EngAlphabet
import pytest

def test_alphabet_print():
    a = Alphabet()
    assert a.letters_num() == 33

def test_eng_letters_num():
    e = EngAlphabet()
    assert e.letters_num() == 26

def test_ua_lang_true():
    ua = Alphabet()
    assert ua.is_ua_lang("Привіт") is True

def test_ua_lang_false():
    ua = Alphabet()
    assert ua.is_ua_lang("Hello") is False

def test_en_letter():
    e = EngAlphabet()
    assert e.is_en_letter("H") is True
    assert e.is_en_letter("Ж") is False
