from src.list_deduplicator import deduplicate

def test_deduplicate_basic():
    assert deduplicate([1,2,2,3,1,4]) == [1,2,3,4]

def test_deduplicate_empty():
    assert deduplicate([]) == []

def test_deduplicate_strings():
    assert deduplicate(['a','b','a','c','b']) == ['a','b','c']
