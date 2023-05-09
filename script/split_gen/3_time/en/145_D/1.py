def main():
    X, Y = map(int, input().split())
    if (X + Y) % 3 != 0:
        print(0)
        return
    n = (X + Y) // 3
    if not (0 <= X <= n and 0 <= Y <= n):
        print(0)
        return
    MOD = 10 ** 9 + 7
    fac = [1] * (n + 1)
    finv = [1] * (n + 1)
    for i in range(1, n + 1):
        fac[i] = fac[i - 1] * i % MOD
        finv[i] = finv[i - 1] * pow(i, MOD - 2, MOD) % MOD
    comb = lambda n, r: fac[n] * finv[r] * finv[n - r] % MOD
    print(comb(n, X))
