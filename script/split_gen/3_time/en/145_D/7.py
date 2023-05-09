def main():
    X, Y = map(int, input().split())
    if (X + Y) % 3 != 0:
        print(0)
        return
    N = (X + Y) // 3
    X -= N
    Y -= N
    if X < 0 or Y < 0:
        print(0)
        return
    MOD = 10 ** 9 + 7
    fact = [1, 1]
    fact_inv = [1, 1]
    inv = [0, 1]
    def cmb(n, r):
        if (r < 0) or (n < r):
            return 0
        r = min(r, n - r)
        return fact[n] * (fact_inv[r] * fact_inv[n - r] % MOD) % MOD
    for i in range(2, N + 1):
        fact.append((fact[-1] * i) % MOD)
        inv.append((-inv[MOD % i] * (MOD // i)) % MOD)
        fact_inv.append((fact_inv[-1] * inv[-1]) % MOD)
    print(cmb(N, X))
