def remove_nth(lst, n):
    """Remove the nth element (0-based index) from the list."""
    return lst[:n+1] + lst[n+2:]
