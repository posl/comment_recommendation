Synthesizing 10/10 solutions

=======
Suggestion 1

def mod_pow(x, n, mod):
    res = 1
    while n > 0:
        if n & 1:
            res = res * x % mod
        x = x * x % mod
        n >>= 1
    return res

=======
Suggestion 2

def modpow(x, n, mod):
    res = 1
    while n > 0:
        if n & 1:
            res = res * x % mod
        x = x * x % mod
        n >>= 1
    return res

=======
Suggestion 3

def modinv(a, mod=10**9+7):
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
Suggestion 4

def powmod(x, n, mod):
    if n == 0:
        return 1
    elif n % 2 == 0:
        return powmod(x * x % mod, n // 2, mod)
    else:
        return x * powmod(x, n - 1, mod) % mod

=======
Suggestion 5

def main():
    n, a, b = map(int, input().split())
    mod = 10**9 + 7
    ans = pow(2, n, mod) - 1
    ans -= comb(n, a, mod)
    ans -= comb(n, b, mod)
    ans %= mod
    print(ans)

=======
Suggestion 6

def main():
    n, a, b = map(int, input().split())
    mod = 10**9 + 7
    ans = pow(2, n, mod) - 1
    def cmb(n, r, mod):
        x, y = 1, 1
        for i in range(r):
            x = x * (n - i) % mod
            y = y * (i + 1) % mod
        return x * pow(y, mod - 2, mod) % mod
    ans = (ans - cmb(n, a, mod) - cmb(n, b, mod)) % mod
    print(ans)

=======
Suggestion 7

def modpow(a, n, mod=10**9+7):
    if n == 0:
        return 1
    elif n % 2 == 0:
        return modpow(a * a % mod, n // 2, mod)
    else:
        return a * modpow(a, n - 1, mod) % mod

=======
Suggestion 8

def main():
    n, a, b = map(int, input().split())
    mod = 10**9 + 7
    def modinv(a, mod):
        b = mod
        u, v = 1, 0
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
    def nCr(n, r, mod):
        if n < r:
            return 0
        if n < 0 or r < 0:
            return 0
        r = min(r, n - r)
        return g1[n] * g2[r] * g2[n-r] % mod
    g1 = [1, 1] # 元テーブル
    g2 = [1, 1] #逆元テーブル
    inverse = [0, 1] #逆元テーブル計算用テーブル
    for i in range( 2, n + 1 ):
        g1.append( ( g1[-1] * i ) % mod )
        inverse.append( ( -inverse[mod % i] * (mod//i) ) % mod )
        g2.append( (g2[-1] * inverse[-1]) % mod )
    ans = pow(2, n, mod) - 1 - nCr(n, a, mod) - nCr(n, b, mod)
    print(ans % mod)

=======
Suggestion 9

def combination(n, r, mod):
    # nCr
    r = min(n - r, r)
    res = 1
    for i in range(r):
        res = res * (n - i) * pow(i + 1, mod - 2, mod) % mod
    return res

=======
Suggestion 10

def modinv(a, mod):
    return pow(a, mod-2, mod)
