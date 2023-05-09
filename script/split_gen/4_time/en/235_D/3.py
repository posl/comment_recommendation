def solve(a, n):
    if n < 10:
        return 1 if a == n else -1
    if n % 10 == 0:
        return solve(a, n // 10) + 1
    return min(solve(a, n // 10) + 1, solve(a, n * a))
