Synthesizing 10/10 solutions

=======
Suggestion 1

def comb(n, r, mod):
    if (r < 0) or (n < r):
        return 0
    r = min(r, n-r)
    return fact[n] * factinv[r] * factinv[n-r] % mod

mod = 10**9+7
N = 2*10**5+1
fact = [1, 1]
factinv = [1, 1]
inv = [0, 1]

for i in range(2, N+1):
    fact.append((fact[-1] * i) % mod)
    inv.append((-inv[mod%i] * (mod//i)) % mod)
    factinv.append((factinv[-1] * inv[-1]) % mod)

n, a, b = map(int, input().split())
ans = pow(2, n, mod) - 1 - comb(n, a, mod) - comb(n, b, mod)
print(ans%mod)

=======
Suggestion 2

def main():
    n, a, b = map(int, input().split())
    mod = 10 ** 9 + 7
    ans = pow(2, n, mod) - 1
    nCa = 1
    nCb = 1
    for i in range(b):
        nCa = nCa * (n - i) % mod
        nCb = nCb * (i + 1) % mod
    ans -= nCa * pow(nCb, mod - 2, mod) % mod
    nCa = 1
    nCb = 1
    for i in range(a):
        nCa = nCa * (n - i) % mod
        nCb = nCb * (i + 1) % mod
    ans -= nCa * pow(nCb, mod - 2, mod) % mod
    print(ans % mod)

=======
Suggestion 3

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

=======
Suggestion 4

def main():
    n, a, b = map(int, input().split())
    mod = 10**9 + 7
    ans = pow(2, n, mod) - 1
    for i in range(n - a + 1, n - b + 1):
        ans -= nCr(n, i)
    print(ans % mod)

=======
Suggestion 5

def main():
    n, a, b = map(int, input().split())
    if a + b > n:
        print(0)
    else:
        ans = pow(2, n, 10 ** 9 + 7) - 1
        c1 = 1
        c2 = 1
        for i in range(a):
            c1 = c1 * (n - i) % (10 ** 9 + 7)
            c2 = c2 * (a - i) % (10 ** 9 + 7)
        ans -= c1 * pow(c2, 10 ** 9 + 5, 10 ** 9 + 7)
        c1 = 1
        c2 = 1
        for i in range(b):
            c1 = c1 * (n - i) % (10 ** 9 + 7)
            c2 = c2 * (b - i) % (10 ** 9 + 7)
        ans -= c1 * pow(c2, 10 ** 9 + 5, 10 ** 9 + 7)
        print(ans % (10 ** 9 + 7))

=======
Suggestion 6

def nCk(n, k):
    if n < k:
        return 0
    if k == 0:
        return 1
    return n * nCk(n-1, k-1) // k

n, a, b = map(int, input().split())

mod = 10**9 + 7

print((pow(2, n, mod) - 1 - nCk(n, a) - nCk(n, b)) % mod)

=======
Suggestion 7

def solve(n, a, b):
    MOD = 10**9 + 7
    def comb(n, r):
        if n < r: return 0
        if n - r < r: r = n - r
        if r == 0: return 1
        if r == 1: return n
        numerator = [n - r + k + 1 for k in range(r)]
        denominator = [k + 1 for k in range(r)]
        for p in range(2, r + 1):
            pivot = denominator[p - 1]
            if pivot > 1:
                offset = (n - r) % p
                for k in range(p - 1, r, p):
                    numerator[k - offset] //= pivot
                    denominator[k] //= pivot
        result = 1
        for k in range(r):
            if numerator[k] > 1: result = result * numerator[k] % MOD
        return result
    return (pow(2, n, MOD) - 1 - comb(n, a) - comb(n, b)) % MOD

=======
Suggestion 8

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

=======
Suggestion 9

def solve(n, a, b):
    MOD = 10 ** 9 + 7
    count = pow(2, n, MOD) - 1
    for i in range(1, n):
        count -= comb(n, i, MOD)
    return count % MOD

=======
Suggestion 10

def calc(n, a, b):
    if a > b:
        a, b = b, a
    if a + 1 == b:
        return n - 2
    else:
        return (n - 2) * (n - 2) % 1000000007

n, a, b = map(int, input().split())
print(calc(n, a, b))
