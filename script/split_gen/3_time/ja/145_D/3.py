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
    fac = [1, 1]
    finv = [1, 1]
    inv = [0, 1]
    for i in range(2, N + 1):
        fac.append(fac[i - 1] * i % mod)
        inv.append(mod - inv[mod % i] * (mod // i) % mod)
        finv.append(finv[i - 1] * inv[i] % mod)
    def nCr(n, r):
        if n < r:
            return 0
        if n < 0 or r < 0:
            return 0
        return fac[n] * (finv[r] * finv[n - r] % mod) % mod
    print(nCr(N, X))
