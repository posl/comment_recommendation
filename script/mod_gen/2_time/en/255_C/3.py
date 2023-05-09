def solve(x, a, d, n):
    if d == 0:
        if x == a:
            return 0
        else:
            return 1
    if n == 1:
        return 0
    if x < a:
        if d < 0:
            return 1 + solve(x, a, -d, n)
        else:
            return 1 + solve(x, a, d, n)
    if x > a + (n - 1) * d:
        if d < 0:
            return 1 + solve(x, a, d, n)
        else:
            return 1 + solve(x, a, -d, n)
    if x == a:
        return 0
    if d < 0:
        return 1 + solve(x, a, -d, n)
    else:
        return min(1 + solve(x, a, -d, n), 1 + solve(x, a, d, n))

if __name__ == '__main__':
    solve()