def main():
    X, Y = map(int, input().split())
    if (X + Y) % 3 != 0:
        print(0)
        return
    N = (X + Y) // 3
    if X > N or Y > N:
        print(0)
        return
    MOD = 10 ** 9 + 7
    fac = [1, 1]
    finv = [1, 1]
    inv = [0, 1]
    def COMinit():
        for i in range(2, N + 1):
            fac.append((fac[i - 1] * i) % MOD)
            inv.append((-inv[MOD % i] * (MOD // i)) % MOD)
            finv.append((finv[i - 1] * inv[i]) % MOD)
    def COM(n, k):
        if n < k:
            return 0
        if n < 0 or k < 0:
            return 0
        return fac[n] * (finv[k] * finv[n - k] % MOD) % MOD
    COMinit()
    print(COM(N, X))

if __name__ == '__main__':
    main()