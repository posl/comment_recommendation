def main():
    n, a, b = map(int, input().split())
    MOD = 10 ** 9 + 7
    def comb(n, r, mod):
        x = 1
        y = 1
        for i in range(r):
            x = x * (n - i) % mod
            y = y * (i + 1) % mod
        return x * pow(y, mod - 2, mod) % mod
    def pow(a, b, mod):
        x = 1
        while b > 0:
            if b & 1:
                x = x * a % mod
            a = a * a % mod
            b >>= 1
        return x
    ans = pow(2, n, MOD) - 1
    ans -= comb(n, a, MOD)
    ans -= comb(n, b, MOD)
    ans %= MOD
    print(ans)
