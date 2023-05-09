def solve(n, a, b):
    MOD = 10 ** 9 + 7
    count = pow(2, n, MOD) - 1
    for i in range(1, n):
        count -= comb(n, i, MOD)
    return count % MOD
