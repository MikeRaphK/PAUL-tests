def remove_nth(lst, n):
    """Remove the nth element (1-based index) from the list."""
    return lst[:n] + lst[n+1:]
