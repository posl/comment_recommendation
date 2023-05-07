def main():
    n, a, b = map(int, input().split())
    MOD = 10 ** 9 + 7
    def comb(n, r):
        x = 1
        y = 1
        for i in range(r):
            x = x * (n - i) % MOD
            y = y * (i + 1) % MOD
        return x * pow(y, MOD - 2, MOD) % MOD
    ans = pow(2, n, MOD) - 1 - comb(n, a) - comb(n, b)
    print(ans % MOD)
