def is_wonderful_string(s):
    if len(s) < 2:
        return False
    if len(s) == 2:
        if s[0].isupper() and s[1].islower():
            return True
        else:
            return False
    if len(s) > 2:
        if s[0].isupper() and s[1].islower():
            for i in range(2, len(s)):
                if s[i].isupper() and s[i-1].islower():
                    return True
                else:
                    continue
        else:
            return False
    return False
