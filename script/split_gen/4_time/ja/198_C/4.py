def solve():
    R, X, Y = map(int, input().split())
    D = (X**2 + Y**2)**0.5
    if D < R:
        print(2)
    else:
        print(int(D//R + (D%R != 0)))
solve()
