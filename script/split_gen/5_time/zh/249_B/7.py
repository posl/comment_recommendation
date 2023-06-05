def isWonderfulString(s):
    if s.islower() or s.isupper():
        return False
    if len(set(s)) != len(s):
        return False
    return True
