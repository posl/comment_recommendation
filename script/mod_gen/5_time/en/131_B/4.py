def solve():
    n, l = map(int, input().split())
    if l > 0:
        print((2 * l + n - 1) * n // 2 - l)
    elif l + n - 1 < 0:
        print((2 * l + n - 1) * n // 2 - l - n + 1)
    else:
        print((2 * l + n - 1) * n // 2 - l)

if __name__ == '__main__':
    solve()