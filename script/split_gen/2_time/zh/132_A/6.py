def isTwoChar(s):
    if len(s) != 4:
        return False
    if len(set(s)) != 2:
        return False
    for c in set(s):
        if s.count(c) != 2:
            return False
    return True
