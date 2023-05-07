def solve():
    import sys
    input = sys.stdin.readline
    from math import ceil
    R, X, Y = map(int, input().split())
    if R**2 == X**2 + Y**2:
        print(1)
    elif R**2 > X**2 + Y**2:
        print(2)
    else:
        print(ceil((X**2 + Y**2)**0.5 / R))
