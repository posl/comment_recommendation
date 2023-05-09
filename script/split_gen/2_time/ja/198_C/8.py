def solve():
    import sys
    input = sys.stdin.readline
    from math import ceil
    r, x, y = map(int, input().split())
    dist = (x**2 + y**2) ** 0.5
    if dist < r:
        print(2)
    else:
        print(ceil(dist/r))
