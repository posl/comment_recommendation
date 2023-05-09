def solve():
    x, a, d, n = map(int, input().split())
    if d == 0:
        if x == a:
            return 0 if n == 1 else -1
        else:
            return -1
    if n == 1:
        return 0
    if d > 0:
        if x < a:
            return -1
        if x > a + (n - 1) * d:
            return -1
        if (x - a) % d == 0:
            return 0
        else:
            return 1
    else:
        if x > a:
            return -1
        if x < a + (n - 1) * d:
            return -1
        if (x - a) % d == 0:
            return 0
        else:
            return 1
print(solve())

if __name__ == '__main__':
    solve()