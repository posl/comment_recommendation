def solve():
    import sys
    import math
    R,X,Y = map(int, sys.stdin.readline().split())
    distance = math.sqrt(X**2 + Y**2)
    if distance % R == 0:
        print(int(distance/R))
    else:
        print(int(distance/R)+1)
