def solve():
    R, X, Y = map(int, input().split())
    if R*R == X*X + Y*Y:
        print(1)
        return
    if R*R > X*X + Y*Y:
        print(2)
        return
    if R*R < X*X + Y*Y:
        import math
        print(math.ceil((X*X + Y*Y)**(1/2) / R))
        return

if __name__ == '__main__':
    solve()