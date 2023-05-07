def main():
    n, a, b = map(int, input().split())
    mod = 10 ** 9 + 7
    def comb(n, r):
        x = 1
        y = 1
        for i in range(r):
            x = x * (n - i) % mod
            y = y * (i + 1) % mod
        return x * pow(y, mod - 2, mod) % mod
    def powmod(x, n):
        res = 1
        while n > 0:
            if n & 1:
                res = res * x % mod
            x = x * x % mod
            n >>= 1
        return res
    ans = powmod(2, n) - 1 - comb(n, a) - comb(n, b)
    print(ans % mod)
