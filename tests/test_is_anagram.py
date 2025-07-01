from src.is_anagram import is_anagram

def test_basic_true():
    assert is_anagram("listen", "silent") is True

def test_basic_false():
    assert is_anagram("apple", "paper") is False

def test_spaces_and_case():
    assert is_anagram("Dormitory", "Dirty room") is True

def test_empty_strings():
    assert is_anagram("", "") is True

def test_one_empty():
    assert is_anagram("", "a") is False

def test_symbols():
    assert is_anagram("a!b@c", "c!b@a") is True