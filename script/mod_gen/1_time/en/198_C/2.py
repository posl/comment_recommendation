def solve():
    R, X, Y = map(int, input().split())
    if R*R == X*X + Y*Y:
        print(1)
    elif R*R > X*X + Y*Y:
        print(2)
    else:
        print(int((X*X + Y*Y)**0.5//R) + 1)
    return 0

if __name__ == '__main__':
    solve()