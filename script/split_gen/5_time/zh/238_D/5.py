def isBitwiseAnd(a, s):
    if a > s:
        return False
    if (a & s) == a:
        return True
    return False
