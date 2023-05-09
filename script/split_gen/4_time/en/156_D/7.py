def main():
    n, a, b = map(int, input().split())
    mod = 10**9 + 7
    #nCkを求める
    def nCk(n, k, mod):
        if k > n - k:
            k = n - k
        x = 1
        y = 1
        for i in range(k):
            x = x * (n - i) % mod
            y = y * (i + 1) % mod
        return x * pow(y, mod - 2, mod) % mod
    print((pow(2, n, mod) - 1 - nCk(n, a, mod) - nCk(n, b, mod)) % mod)
