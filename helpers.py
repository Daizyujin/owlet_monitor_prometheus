def safe_get(p: dict, keys: [], default: any) -> any:
    length = len(keys)
    last_value = p
    for i, key in enumerate(keys):
        is_last = i + 1 == length
        if key in last_value:
            last_value = last_value[key]
        elif is_last:
            return default
    return last_value