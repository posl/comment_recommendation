def is_wonderful_string(s):
    if len(s) < 2:
        return False
    if s[0].islower() or s[-1].islower():
        return False
    if s[0].isupper() and s[1].isupper():
        return False
    if s[-1].isupper() and s[-2].isupper():
        return False
    for i in range(1, len(s) - 1):
        if s[i].isupper() and s[i + 1].isupper():
            return False
        if s[i].islower() and s[i + 1].islower():
            return False
    return True
