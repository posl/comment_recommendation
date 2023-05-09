def solve(n, x):
    if n == 0:
        return 1 if x <= 0 else 0
    if x <= 1 + 2 ** (n - 1):
        return solve(n - 1, x - 1)
    else:
        return 2 ** n + solve(n - 1, x - 2 - 2 ** (n - 1))

if __name__ == '__main__':
    solve()