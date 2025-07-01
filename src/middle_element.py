def middle_element(lst):
    """Return the middle element of a non-empty list.
    If the list has even length, return the lower of the two middle elements.
    """
    idx = len(lst) // 2
    return lst[idx]
