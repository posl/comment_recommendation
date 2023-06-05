def solve(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    if n % 2 == 0:
        return (n // 2) * (n // 2 - 1)
    else:
        return (n // 2) * (n // 2 - 1) + (n // 2)
