def solve():
    H, W, A, B = map(int, input().split())
    MOD = 10 ** 9 + 7
    fact = [1] * (H + W + 1)
    for i in range(1, H + W + 1):
        fact[i] = fact[i - 1] * i % MOD
    def inv(x):
        return pow(x, MOD - 2, MOD)
    def comb(n, r):
        return fact[n] * inv(fact[n - r]) * inv(fact[r]) % MOD
    ans = 0
    for i in range(B + 1):
        ans += comb(H - A + i - 1, i) * comb(A + W - i - 2, A - 1)
        ans %= MOD
    print(ans)
solve()
