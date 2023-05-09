def is_wonderful_string(s):
    if len(s) < 2:
        return False
    elif len(s) == 2:
        return s[0] != s[1]
    else:
        return s[0] != s[1] and is_wonderful_string(s[1:])
