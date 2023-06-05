def solve(n):
    if n == 1:
        return 0
    elif n == 2:
        return 2
    else:
        return (10 * 9 * (pow(10, n-2, 10**9+7) - pow(9, n-2, 10**9+7)) + 10 * pow(9, n-2, 10**9+7)) % (10**9+7)
