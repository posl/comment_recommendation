def isBitAnd(a, s):
    if (a > s):
        return False
    if ((s - a) & a == 0):
        return True
    else:
        return False

if __name__ == '__main__':
    isBitAnd()