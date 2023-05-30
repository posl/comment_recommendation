def solve():
    R, X, Y = map(int, input().split())
    if (X**2 + Y**2) % R**2 == 0:
        print((X**2 + Y**2) // R**2)
    else:
        print((X**2 + Y**2) // R**2 + 1)
solve()
