def solve():
    R, X, Y = map(int, input().split())
    d = (X**2 + Y**2)**(1/2)
    if d < R:
        print(2)
    else:
        print(int(d//R + 1) if d%R != 0 else int(d//R))
    return 0
