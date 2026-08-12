import pytest
from string_utils import StringUtils

utils = StringUtils()

def test_capitalize_positive():
    assert utils.capitalize("skypro") == "Skypro"

def test_capitalize_empty():
    assert utils.capitalize("") == ""

def test_capitalize_with_spaces():
    assert utils.capitalize("  skypro") == "Skypro"

def test_trim_pozitive():
    assert utils.trim("   skypro") == "skypro"

def test_trim_empty():
    assert utils.trim("") == ""

def test_trim_no_spaces():
    assert utils.trim("skypro") == "skypro"

def test_contains_pozitive():
    assert utils.contains("SkyPro", "S") == True

def test_contains_negative():
    assert utils.contains("SkyPro", "U") == False

def test_contains_empty_string():
    assert utils.contains("", "a") == False

def test_contains_empty_symbo():
    assert utils.contains("SkyPro", "") == False

def test_delete_symbol_positive():
    assert utils.delete_symbol("SkyPro", "k") == "SyPro"

def test_delete_symbol_substring():
    assert utils.delete_symbol("SkyPro", "Pro") == "Sky"

def test_delete_symbol_not_found():
    assert utils.delete_symbol("SkyPro", "z") == "SkyPro"

def test_delete_symbol_empty_string():
    assert utils.delete_symbol("", "a") == ""

def test_delete_symbol_empty_symbo():
    assert utils.delete_symbol("SkyPro", "") == "SkyPro"
    