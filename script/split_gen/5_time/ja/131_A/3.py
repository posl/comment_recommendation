def is_same_number(s):
    if s[0] == s[1] and s[1] == s[2]:
        return True
    elif s[1] == s[2] and s[2] == s[3]:
        return True
    return False
