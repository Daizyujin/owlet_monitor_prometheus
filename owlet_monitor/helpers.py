def safe_get(p: dict, keys: [], default: any) -> any:
    """Safely traverses nested dictionary using the keys given.
    If key does not exist at any point, returns default value given
    Args:
        p(dict): Dictionary
        keys([]): Keys in order
        default(any): Default value if key is missing
    """
    length = len(keys)
    last_value = p
    for i, key in enumerate(keys):
        is_last = i + 1 == length
        if key in last_value:
            last_value = last_value[key]
        elif is_last:
            return default
    return last_value