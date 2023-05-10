def solve():
    X, Y = map(int, input().split())
    MOD = 10**9 + 7
    if (X+Y)%3 != 0:
        return 0
    n = (X+Y)//3
    m = n - X
    if m < 0:
        return 0
    def comb(n, r, mod):
        if r < 0 or n < r:
            return 0
        r = min(r, n-r)
        return fac[n] * finv[r] * finv[n-r] % mod
    fac = [0] * (n+1)
    finv = [0] * (n+1)
    inv = [0] * (n+1)
    fac[0] = fac[1] = 1
    finv[0] = finv[1] = 1
    inv[1] = 1
    for i in range(2, n+1):
        fac[i] = fac[i-1] * i % MOD
        inv[i] = MOD - inv[MOD%i] * (MOD//i) % MOD
        finv[i] = finv[i-1] * inv[i] % MOD
    return comb(n, m, MOD)
