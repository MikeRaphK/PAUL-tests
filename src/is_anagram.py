def is_anagram(s1, s2):
    """Check if two strings are anagrams, ignoring spaces and case."""
    return sorted(s1) == sorted(s2)