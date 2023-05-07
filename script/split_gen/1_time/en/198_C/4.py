def solve():
    import math
    R, X, Y = map(int, input().split())
    d = math.sqrt(X*X + Y*Y)
    if d == R:
        print(1)
    elif d <= 2*R:
        print(2)
    else:
        print(math.ceil(d/R))
