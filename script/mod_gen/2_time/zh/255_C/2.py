def solve(x, a, d, n):
    if d == 0:
        if x == a:
            return 0
        else:
            return -1
    if n == 1:
        if x == a:
            return 0
        else:
            return -1
    if d > 0:
        if x < a:
            return -1
        if x > a + (n - 1) * d:
            return -1
        if x == a:
            return 0
        if (x - a) % d == 0:
            return (x - a) // d
        else:
            return -1
    if d < 0:
        if x > a:
            return -1
        if x < a + (n - 1) * d:
            return -1
        if x == a:
            return 0
        if (x - a) % d == 0:
            return (x - a) // d
        else:
            return -1

if __name__ == '__main__':
    solve()