def solve(a, n):
    if n == 1:
        return 0
    if n % 2 == 0:
        return 1 + solve(a, n // 2)
    else:
        return 1 + min(solve(a, n + 1), solve(a, n - 1))

if __name__ == '__main__':
    solve()