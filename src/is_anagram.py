def is_anagram(s1, s2):
    """Check if two strings are anagrams, ignoring spaces and case."""
    # Normalize the strings: remove spaces and convert to lowercase
    s1_normalized = ''.join(s1.lower().split())
    s2_normalized = ''.join(s2.lower().split())
    return sorted(s1_normalized) == sorted(s2_normalized)
