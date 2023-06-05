def isBitwiseAnd(a, s):
    if a > s:
        return False
    if a == s:
        return True
    if a == 0:
        return False
    if s - a == a:
        return False
    if a & (s - a) == 0:
        return False
    return True
