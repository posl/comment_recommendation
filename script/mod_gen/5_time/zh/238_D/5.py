def isBitwiseAnd(a, s):
    if a > s:
        return False
    if (a & s) == a:
        return True
    return False

if __name__ == '__main__':
    isBitwiseAnd()