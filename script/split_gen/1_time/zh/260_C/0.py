def getBlueNum(n, x, y):
    if n == 1:
        return 0
    if n == 2:
        return x
    if n == 3:
        return x + y
    if n > 3:
        return getBlueNum(n-1, x, y) + getBlueNum(n-2, x, y)
