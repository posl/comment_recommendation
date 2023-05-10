def solve():
    N, K = map(int, input().split())
    mod = 10**9+7
    fact = [1] * (N+1)
    for i in range(1, N+1):
        fact[i] = fact[i-1] * i % mod
    fact_inv = [1] * (N+1)
    fact_inv[N] = pow(fact[N], mod-2, mod)
    for i in range(N, 0, -1):
        fact_inv[i-1] = fact_inv[i] * i % mod
    def comb(n, k):
        return fact[n] * fact_inv[n-k] * fact_inv[k] % mod
    for i in range(1, K+1):
        if N-K+1 < i:
            print(0)
        else:
            print(comb(N-K+1, i) * comb(K-1, i-1) % mod)
