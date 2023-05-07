def solve(n, a, b, c, d, e):
    m = min(a, b, c, d, e)
    if n <= m:
        return 5
    return 4 + (n + m - 1) // m

if __name__ == '__main__':
    solve()