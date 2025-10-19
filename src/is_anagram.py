def is_anagram(s1, s2):
    """Check if two strings are anagrams, ignoring spaces and case."""
    s1 = s1.replace(" ", "").lower()  # Remove spaces and convert to lower case
    s2 = s2.replace(" ", "").lower()  # Remove spaces and convert to lower case
    return sorted(s1) == sorted(s2)  # Compare sorted characters
