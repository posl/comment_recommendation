def solve():
    X, Y, Z = map(int, input().split())
    if Y > Z:
        print(-1)
    else:
        print((X * Z) // (Z - Y))
solve()
