Synthesizing 10/10 solutions (Duplicates hidden)

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

def modpow(a, n, mod):
    res = 1
    while n > 0:
        if n & 1:
            res = res * a % mod
        a = a * a % mod
        n >>= 1
    return res

=======
Suggestion 3

def mod_pow(a, n, mod):
    res = 1
    while n > 0:
        if n & 1:
            res = res * a % mod
        a = a * a % mod
        n >>= 1
    return res

=======
Suggestion 4

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

=======
Suggestion 5

def main():
    N, A, B = map(int, input().split())
    MOD = 10**9 + 7
    ans = pow(2, N, MOD) - 1
    ans -= comb(N, A, MOD)
    ans -= comb(N, B, MOD)
    ans %= MOD
    print(ans)

=======
Suggestion 6

def main():
    n, a, b = map(int, input().split())
    MOD = 10**9 + 7
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
    def comb(n, r, mod):
        if r < 0 or r > n:
            return 0
        r = min(r, n - r)
        return g1[n] * g2[r] * g2[n - r] % mod
    g1 = [1, 1]
    g2 = [1, 1]
    inverse = [0, 1]
    for i in range(2, n + 1):
        g1.append((g1[-1] * i) % MOD)
        inverse.append((-inverse[MOD % i] * (MOD // i)) % MOD)
        g2.append((g2[-1] * inverse[-1]) % MOD)
    ans = pow(2, n, MOD) - 1 - comb(n, a, MOD) - comb(n, b, MOD)
    ans %= MOD
    print(ans)

=======
Suggestion 7

def main():
    n, a, b = map(int, input().split())
    mod = 10**9+7
    ans = pow(2, n, mod) - 1
    for i in range(a, b+1):
        ans -= comb(n, i, mod)
        ans %= mod
    print(ans)

=======
Suggestion 8

def modpow(x, n, mod):
    """x^nをmodで割った余りを求める"""
    res = 1
    while n > 0:
        if n & 1:
            res = res * x % mod
        x = x * x % mod
        n >>= 1
    return res

=======
Suggestion 9

def main():
    n, a, b = map(int, input().split())

    # aとbは互いに素なので、
    # aとbのLCMはa*bになる。
    # また、n以下のaとbの倍数の個数は
    # n//a + n//b - n//(a*b)で求められる。
    # ここで、n//(a*b)はaとbのLCMの倍数の個数である。
    # したがって、n以下のaとbの倍数の個数は
    # n//a + n//b - n//(a*b)で求められる。
    # ここで、n//(a*b)はaとbのLCMの倍数の個数である。
    # したがって、n以下のaとbの倍数の個数は
    # n//a + n//b - n//(a*b)で求められる。
    # ここで、n//(a*b)はaとbのLCMの倍数の個数である。
    # したがって、n以下のaとbの倍数の個数は
    # n//a + n//b - n//(a*b)で求められる。
    # ここで、n//(a*b)はaとbのLCMの倍数の個数である。
    # したがって、n以下のaとbの倍数の個数は
    # n//a + n//b - n//(a*b)で求められる。
    # ここで、n//(a*b)はaとbのLCMの倍数の個数である。
    # したがって、n以下のaとbの倍数の個数は
    # n//a + n//b - n//(a*b)で求められる。
    # ここで、n//(a*b)はaとbのLCMの倍数の個数である。
    # したがって、n以下のa
