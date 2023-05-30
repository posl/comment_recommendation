def C(n, r):
    if n < r:
        return 0
    if n == r:
        return 1
    if r == 0:
        return 1
    return (fac[n] * inv[r] * inv[n-r]) % MOD
MOD = 10**9 + 7
N, K = map(int, input().split())
fac = [1] * (N+1)
inv = [1] * (N+1)
for i in range(2, N+1):
    fac[i] = (fac[i-1] * i) % MOD
    inv[i] = pow(fac[i], MOD-2, MOD)
for i in range(1, K+1):
    print(C(N-K+1, i) * C(K-1, i-1) % MOD)
