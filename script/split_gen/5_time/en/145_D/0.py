def main():
    X, Y = map(int, input().split())
    mod = 10 ** 9 + 7
    if (X + Y) % 3 != 0:
        print(0)
        return
    n = (X + Y) // 3
    m = (2 * X - Y) // 3
    if n < 0 or m < 0:
        print(0)
        return
    def comb(n, r, mod):
        if r == 0:
            return 1
        if n < r:
            return 0
        return fact[n] * fact_inv[r] * fact_inv[n-r] % mod
    fact = [1, 1]
    fact_inv = [1, 1]
    inv = [0, 1]
    for i in range(2, n + m + 1):
        fact.append((fact[-1] * i) % mod)
        inv.append((-inv[mod % i] * (mod // i)) % mod)
        fact_inv.append((fact_inv[-1] * inv[-1]) % mod)
    print(comb(n + m, n, mod))
