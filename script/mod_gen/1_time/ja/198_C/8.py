def solve():
    # R, X, Y = map(int, input().split())
    # # R, X, Y = 5, 11, 0
    # # R, X, Y = 5, 15, 0
    # # R, X, Y = 3, 4, 4
    # if R*R > X*X + Y*Y:
    #     print(2)
    # else:
    #     print(1 + (X*X + Y*Y) // (R*R))
    R, X, Y = map(int, input().split())
    d = X*X + Y*Y
    if d < R*R:
        print(2)
    elif d == R*R:
        print(1)
    else:
        print((d + R*R - 1) // (R*R))

if __name__ == '__main__':
    solve()