def main():
    n, a, b = map(int, input().split())
    mod = 10**9+7
    def modpow(a, n, mod):
        res = 1
        while n > 0:
            if n & 1:
                res = res * a % mod
            a = a * a % mod
            n >>= 1
        return res
    def comb(n, k, mod):
        if k < 0 or k > n:
            return 0
        k = min(k, n-k)
        res = 1
        for i in range(k):
            res = res * (n-i) % mod
        for i in range(k):
            res = res * modpow(i+1, mod-2, mod) % mod
        return res
    ans = modpow(2, n, mod) - 1 - comb(n, a, mod) - comb(n, b, mod)
    print(ans % mod)
