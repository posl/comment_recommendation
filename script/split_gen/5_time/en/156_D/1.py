def main():
    n, a, b = map(int, input().split())
    mod = 10**9 + 7
    def comb(n, r):
        x, y = 1, 1
        for i in range(r):
            x = x * (n - i) % mod
            y = y * (i + 1) % mod
        return x * pow(y, mod - 2, mod) % mod
    print((pow(2, n, mod) - 1 - comb(n, a) - comb(n, b)) % mod)
