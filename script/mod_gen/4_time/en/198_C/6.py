def solve():
    R,X,Y = map(int,input().split())
    import math
    d = math.sqrt(X*X+Y*Y)
    if d < R:
        return 2
    else:
        return math.ceil(d/R)
print(solve())
