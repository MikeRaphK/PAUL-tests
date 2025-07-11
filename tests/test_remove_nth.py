from src.remove_nth import remove_nth

def test_remove_middle():
    assert remove_nth([10,20,30,40], 2) == [10,20,40]

def test_remove_first():
    assert remove_nth([5,6,7], 0) == [6,7]

def test_remove_last():
    assert remove_nth([1,2,3], 2) == [1,2]
