def isBitwiseSum(a, s):
    if a > s:
        return False
    if (s - a) & a == 0:
        return True
    return False
