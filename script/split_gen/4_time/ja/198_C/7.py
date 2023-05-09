def solve():
    import sys
    R,X,Y = map(int, sys.stdin.readline().split())
    import math
    d = math.sqrt(X**2+Y**2)
    if d < R:
        print(2)
    else:
        print(math.ceil(d/R))
