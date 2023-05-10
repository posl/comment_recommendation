def solve():
    R, X, Y = map(int, input().split())
    d = (X*X+Y*Y)**(1/2)
    if d < R:
        print(2)
    else:
        print(int(d//R) + int(d%R != 0))
