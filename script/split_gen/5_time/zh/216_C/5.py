def solve(n):
    if n == 0:
        return ""
    if n % 2 == 0:
        return solve(n // 2) + "B"
    else:
        return solve(n - 1) + "A"
