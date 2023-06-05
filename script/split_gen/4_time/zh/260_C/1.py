def calcBlue(n, x, y):
    if n == 1:
        return 1
    if n == 2:
        return x
    return calcBlue(n-1, x, y) + calcBlue(n-2, x, y)*y
