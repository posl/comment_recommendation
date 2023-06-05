def check(s):
    if int(s[:2]) > 12:
        return False
    if int(s[2:]) > 12:
        return False
    return True
