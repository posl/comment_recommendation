def isMatch(s):
    if len(s) != 12:
        return False
    if s[0:5] != "Hello":
        return False
    if s[5:6] != ",":
        return False
    if s[6:12] != "World!":
        return False
    return True
