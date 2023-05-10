def solve():
    R, X, Y = map(int, input().split())
    d = (X**2 + Y**2)**0.5
    if d == R:
        print(1)
    elif d <= 2*R:
        print(2)
    else:
        print(int(d//R + (d%R != 0)))
