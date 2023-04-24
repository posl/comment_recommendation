Synthesizing 10/10 solutions

=======
Suggestion 1

def modpow(a, n, mod):
    if n == 0:
        return 1
    if n % 2 == 0:
        return modpow(a * a % mod, n // 2, mod)
    return a * modpow(a, n - 1, mod) % mod

=======
Suggestion 2

def modpow(a, b, m):
    if b == 0:
        return 1
    elif b % 2 == 0:
        return modpow(a * a % m, b / 2, m)
    else:
        return a * modpow(a, b - 1, m) % m

=======
Suggestion 3

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

=======
Suggestion 4

def modpow(a, b, mod):
    if b == 0:
        return 1
    if b % 2 == 0:
        return modpow(a * a % mod, b // 2, mod)
    return a * modpow(a, b - 1, mod) % mod

=======
Suggestion 5

def combination(n, r, mod):
    if r < 0 or n < r:
        return 0
    if n - r < r:
        r = n - r
    if r == 0:
        return 1
    if r == 1:
        return n
    numerator = 1
    denominator = 1
    for i in range(1, r + 1):
        numerator = numerator * (n - i + 1) % mod
        denominator = denominator * i % mod
    return numerator * pow(denominator, mod - 2, mod) % mod

=======
Suggestion 6

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

=======
Suggestion 7

def modpow(a, n, mod): #a^n mod
    if n == 0:
        return 1
    elif n % 2 == 0:
        return modpow(a, n // 2, mod)**2 % mod
    else:
        return a * modpow(a, n - 1, mod) % mod

=======
Suggestion 8

def main():
    import sys
    input = sys.stdin.readline
    from collections import Counter
    from itertools import accumulate
    n, a, b = map(int, input().split())
    MOD = 10**9 + 7
    def cmb(n, r, mod):
        if r > n - r:
            r = n - r
        if r == 0:
            return 1
        if r == 1:
            return n
        numer = reduce(lambda x, y: x * y % mod, range(n, n - r, -1))
        denom = reduce(lambda x, y: x * y % mod, range(1, r + 1))
        return numer * pow(denom, mod - 2, mod) % mod
    def cmb2(n, r, mod):
        numer = reduce(lambda x, y: x * y % mod, range(n, n - r, -1))
        denom = reduce(lambda x, y: x * y % mod, range(1, r + 1))
        return numer * pow(denom, mod - 2, mod) % mod
    def cmb3(n, r, mod):
        numer = reduce(lambda x, y: x * y % mod, range(n, n - r, -1))
        denom = reduce(lambda x, y: x * y % mod, range(1, r + 1))
        return numer * pow(denom, mod - 2, mod) % mod
    def cmb4(n, r, mod):
        numer = reduce(lambda x, y: x * y % mod, range(n, n - r, -1))
        denom = reduce(lambda x, y: x * y % mod, range(1, r + 1))
        return numer * pow(denom, mod - 2, mod) % mod
    def cmb5(n, r, mod):
        numer = reduce(lambda x, y: x * y % mod, range(n, n - r, -1))
        denom = reduce(lambda x, y: x * y % mod, range(1, r + 1))
        return numer * pow(denom, mod - 2, mod) % mod
    def cmb6(n, r, mod):
        numer = reduce(lambda x, y: x * y %

=======
Suggestion 9

def main():
    n, a, b = map(int, input().split())
    mod = 10**9 + 7
    #nCk
    def comb(n, k):
        if n < k or k < 0:
            return 0
        if k == 0:
            return 1
        if k == 1:
            return n
        if k == n:
            return 1
        if k > n - k:
            k = n - k
        return comb(n - 1, k - 1) + comb(n - 1, k)
    #nPk
    def perm(n, k):
        if n < k or k < 0:
            return 0
        if k == 0:
            return 1
        if k == 1:
            return n
        if k == n:
            return 1
        return n * perm(n - 1, k - 1)
    #nHk
    def hom(n, k):
        return comb(n + k - 1, k)
    print((pow(2, n, mod) - 1 - comb(n, a) - comb(n, b)) % mod)

=======
Suggestion 10

def getModulo(n, a, b):
    MOD = 10**9 + 7
    def powModulo(x, n):
        if n == 0: return 1
        elif n == 1: return x
        elif n % 2 == 0:
            return powModulo(x*x%MOD, n//2)
        else:
            return powModulo(x*x%MOD, n//2) * x % MOD
    def combModulo(n, r):
        if r == 0: return 1
        elif r == 1: return n
        else:
            return combModulo(n, r-1) * (n-r+1) * powModulo(r, MOD-2) % MOD
    return (powModulo(2, n) - 1 - combModulo(n, a) - combModulo(n, b)) % MOD

n, a, b = map(int, input().split())
print(getModulo(n, a, b))
