def main():
    X, Y = map(int, input().split())
    if (X + Y) % 3 != 0:
        print(0)
        return
    N = (X + Y) // 3
    if X > N or Y > N:
        print(0)
        return
    mod = 10 ** 9 + 7
    fact = [1] * (N + 1)
    for i in range(1, N + 1):
        fact[i] = (fact[i - 1] * i) % mod
    fact_inv = [1] * (N + 1)
    fact_inv[N] = pow(fact[N], mod - 2, mod)
    for i in reversed(range(N)):
        fact_inv[i] = (fact_inv[i + 1] * (i + 1)) % mod
    comb = lambda n, r: (fact[n] * fact_inv[r] * fact_inv[n - r]) % mod
    print(comb(N, X))
