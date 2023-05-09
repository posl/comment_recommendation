def main():
    H, W, A, B = map(int, input().split())
    MOD = 10**9 + 7
    def comb(n, r):
        x = 1
        y = 1
        for i in range(r):
            x = x * (n - i) % MOD
            y = y * (i + 1) % MOD
        return x * pow(y, MOD - 2, MOD) % MOD
    ans = 0
    for i in range(H - B):
        ans += comb(A + i, i) * comb(W - A + H - B - i - 1, H - B - i - 1)
        ans %= MOD
    print(ans)
