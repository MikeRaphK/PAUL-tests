def is_anagram(s1, s2):
    """Check if two strings are anagrams, ignoring spaces and case."""
    # Remove spaces and convert to lowercase
    s1 = ''.join(s1.split()).lower()
    s2 = ''.join(s2.split()).lower()
    return sorted(s1) == sorted(s2)