def main():
    n, a, b = map(int, input().split())
    MOD = 10**9 + 7
    def modinv(a, mod):
        b = mod
        u = 1
        v = 0
        while b:
            t = a // b
            a -= t * b
            a, b = b, a
            u -= t * v
            u, v = v, u
        u %= mod
        if u < 0:
            u += mod
        return u
    def comb(n, r, mod):
        if r < 0 or r > n:
            return 0
        r = min(r, n - r)
        return g1[n] * g2[r] * g2[n - r] % mod
    g1 = [1, 1]
    g2 = [1, 1]
    inverse = [0, 1]
    for i in range(2, n + 1):
        g1.append((g1[-1] * i) % MOD)
        inverse.append((-inverse[MOD % i] * (MOD // i)) % MOD)
        g2.append((g2[-1] * inverse[-1]) % MOD)
    ans = pow(2, n, MOD) - 1 - comb(n, a, MOD) - comb(n, b, MOD)
    ans %= MOD
    print(ans)

if __name__ == '__main__':
    main()