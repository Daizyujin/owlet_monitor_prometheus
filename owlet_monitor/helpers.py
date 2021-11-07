import json


def safe_get(p: dict, keys_list: [], default: any) -> any:
    """Safely traverses nested dictionary using the keys given.
    If key does not exist at any point, returns default value given
    Args:
        p(dict): Dictionary
        keys_list([]): Keys in order
        default(any): Default value if key is missing
    """
    for keys in keys_list:
        all_keys_found = True
        last_value = p

        for i, key in enumerate(keys):
            if isinstance(last_value, str):
                last_value = json.loads(last_value)

            if key in last_value:
                last_value = last_value[key]
            else:
                all_keys_found = False

        if all_keys_found:
            return last_value

    return default
