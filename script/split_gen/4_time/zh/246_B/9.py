def solve():
    import math
    A, B = map(int, input().split())
    x = 0
    y = 0
    d = math.sqrt(A**2 + B**2)
    x = x + A/d
    y = y + B/d
    print("{0:.12f} {1:.12f}".format(x, y))
