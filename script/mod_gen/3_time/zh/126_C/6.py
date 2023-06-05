def solve(n, k):
    if n >= k:
        return 1.0
    elif n * 2 >= k:
        return (n + 1.0) / (2 * n)
    else:
        return 1.0 * (n + 1 - k) / (n - k + 1) + (k - 1) * 2.0 / (n - k + 1)

if __name__ == '__main__':
    solve()