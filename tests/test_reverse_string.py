from src.reverse_string import reverse_string

def test_reverse_regular():
    assert reverse_string("hello") == "olleh"

def test_reverse_empty():
    assert reverse_string("") == ""

def test_reverse_single():
    assert reverse_string("a") == "a"

def test_reverse_palindrome():
    assert reverse_string("madam") == "madam"