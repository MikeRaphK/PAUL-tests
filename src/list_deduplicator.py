def deduplicate(items):
    """Remove duplicates but preserve original order."""
    seen = set()
    result = []
    for i in range(len(items)):
        if items[i] not in seen:
            seen.add(i)
            result.append(items[i])
    return result
