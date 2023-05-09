def isFullHouse(a, b, c, d, e):
    if a == b and b == c and d == e:
        return True
    elif a == b and c == d and d == e:
        return True
    else:
        return False
