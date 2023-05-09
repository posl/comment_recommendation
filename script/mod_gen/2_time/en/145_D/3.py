def solve():
    X, Y = map(int, input().split())
    if (X + Y) % 3 != 0:
        print(0)
        return
    N = (X + Y) // 3
    if X > N or Y > N:
        print(0)
        return
    MOD = 10**9 + 7
    fac = [1] * (N + 1)
    for i in range(1, N + 1):
        fac[i] = fac[i - 1] * i % MOD
    ifac = [1] * (N + 1)
    ifac[N] = pow(fac[N], MOD - 2, MOD)
    for i in range(N - 1, -1, -1):
        ifac[i] = ifac[i + 1] * (i + 1) % MOD
    def comb(n, k):
        return fac[n] * ifac[k] % MOD * ifac[n - k] % MOD
    print(comb(N, X))
    return

if __name__ == '__main__':
    solve()