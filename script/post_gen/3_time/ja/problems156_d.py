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

def cmb(n, r, mod):
    if (r < 0) or (n < r):
        return 0
    r = min(r, n - r)
    return g1[n] * g2[r] * g2[n - r] % mod

mod = 10**9 + 7  # 出力の制限
N = 2 * 10**5 + 1
g1 = [1, 1]  # 元テーブル
g2 = [1, 1]  # 逆元テーブル
inverse = [0, 1]  # 逆元テーブル計算用テーブル

for i in range(2, N + 1):
    g1.append((g1[-1] * i) % mod)
    inverse.append((-inverse[mod % i] * (mod // i)) % mod)
    g2.append((g2[-1] * inverse[-1]) % mod)

n, a, b = map(int, input().split())
print((pow(2, n, mod) + mod - 1 - cmb(n, a, mod) - cmb(n, b, mod)) % mod)

=======
Suggestion 4

def modpow(x, n, mod):
    res = 1
    while n > 0:
        if n & 1:
            res = res * x % mod
        x = x * x % mod
        n >>= 1
    return res

=======
Suggestion 5

def modpow(a, n, mod):
    if n == 0:
        return 1
    elif n % 2 == 0:
        return modpow(a * a % mod, n // 2, mod)
    else:
        return a * modpow(a, n - 1, mod) % mod

=======
Suggestion 6

def main():
    n, a, b = map(int, input().split())
    mod = 10 ** 9 + 7
    ans = pow(2, n, mod) - 1
    ans -= comb(n, a, mod)
    ans -= comb(n, b, mod)
    ans %= mod
    print(ans)

=======
Suggestion 7

def main():
    n, a, b = map(int, input().split())
    MOD = 10**9 + 7
    x = pow(2, n, MOD) - 1
    y = 1
    for i in range(1, a + 1):
        y = y * (n - i + 1) * pow(i, MOD - 2, MOD) % MOD
    z = 1
    for i in range(1, b + 1):
        z = z * (n - i + 1) * pow(i, MOD - 2, MOD) % MOD
    print((x - y - z) % MOD)

=======
Suggestion 8

def main():
    n, a, b = map(int, input().split())
    MOD = 10**9 + 7

    def calc(n, r):
        if n < r:
            return 0
        if n - r < r:
            r = n - r
        res = 1
        for i in range(r):
            res = res * (n - i) % MOD
        for i in range(r):
            res = res * pow(i + 1, MOD - 2, MOD) % MOD
        return res

    ans = pow(2, n, MOD) - 1 - calc(n, a) - calc(n, b)
    print(ans % MOD)
