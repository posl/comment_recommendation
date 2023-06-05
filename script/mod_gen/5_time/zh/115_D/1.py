def solve(N, X):
    if N == 0:
        return 0
    elif X == 1:
        return 0
    elif X <= 1 + 2 * solve(N - 1, (1 << (N - 1)) - 1):
        return solve(N - 1, X - 1)
    else:
        return 1 + 2 * solve(N - 1, (1 << (N - 1)) - 1)

if __name__ == '__main__':
    solve()