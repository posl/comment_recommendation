def solve():
    r, x, y = map(int, input().split())
    d = (x ** 2 + y ** 2) ** 0.5
    if d % r == 0:
        print(int(d / r))
    elif d < r:
        print(2)
    else:
        print(int(d // r) + 1)

if __name__ == '__main__':
    solve()