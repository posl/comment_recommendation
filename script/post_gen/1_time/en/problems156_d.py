Synthesizing 10/10 solutions

=======
Suggestion 1

def modinv(a, m):
    b = m
    u = 1
    v = 0
    while b:
        t = a // b
        a -= t * b
        a, b = b, a
        u -= t * v
        u, v = v, u
    u %= m
    if u < 0:
        u += m
    return u

=======
Suggestion 2

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

=======
Suggestion 3

def modpow(x, n, mod):
    res = 1
    while n > 0:
        if n & 1:
            res = res * x % mod
        x = x * x % mod
        n >>= 1
    return res

=======
Suggestion 4

def comb(n, r, mod):
    if r < 0 or r > n:
        return 0
    r = min(r, n - r)
    return g1[n] * g2[r] * g2[n - r] % mod

=======
Suggestion 5

def modpow(x, n, mod):
    if n == 0:
        return 1
    elif n % 2 == 0:
        return modpow(x * x % mod, n / 2, mod)
    else:
        return x * modpow(x, n - 1, mod) % mod

=======
Suggestion 6

def main():
    n, a, b = map(int, input().split())
    mod = 10**9 + 7
    ans = pow(2, n, mod) - 1
    ans -= comb(n, a, mod)
    ans -= comb(n, b, mod)
    ans %= mod
    print(ans)

=======
Suggestion 7

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

=======
Suggestion 8

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

=======
Suggestion 9

def main():
    MOD = 1000000007
    n, a, b = map(int, input().split())
    def comb(n, r):
        x = 1
        y = 1
        for i in range(r):
            x = x * (n - i) % MOD
            y = y * (i + 1) % MOD
        return x * pow(y, MOD - 2, MOD) % MOD
    ans = pow(2, n, MOD) - 1 - comb(n, a) - comb(n, b)
    print(ans % MOD)

=======
Suggestion 10

def calcMod(x):
    return x % (10**9 + 7)
