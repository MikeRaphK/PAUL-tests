from src.middle_element import middle_element

def test_odd_length():
    assert middle_element([1, 2, 3]) == 2
    assert middle_element([0, 5, 9, 7, 3]) == 9

def test_even_length():
    assert middle_element([10, 20, 30, 40]) == 20   # lower of [20, 30]
    assert middle_element([8, 4, 2, 0, -2, -4]) == 2  # lower of [2, 0]

def test_single_element():
    assert middle_element([42]) == 42
