def solve(n, k):
    mod = 10 ** 9 + 7
    return (n + 1 - k) * (n + 2) * k // 2 % mod
