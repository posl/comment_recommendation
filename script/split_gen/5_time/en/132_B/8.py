def check_if_two_chars_appear_twice_in_str(str):
    if len(str) != 4:
        return False
    if len(set(str)) != 2:
        return False
    for char in set(str):
        if str.count(char) != 2:
            return False
    return True
