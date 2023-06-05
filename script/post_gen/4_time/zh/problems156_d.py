Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

=======
Suggestion 2

def main():
    n,a,b=map(int,input().split())
    mod=10**9+7
    ans=pow(2,n,mod)-1
    for i in range(a,b+1):
        ans-=comb(n,i,mod)
    print(ans%mod)

=======
Suggestion 3

def getGCD(a,b):
    if a < b:
        a,b = b,a
    while b != 0:
        a,b = b,a%b
    return a

=======
Suggestion 4

def comb(n, r, mod=10**9+7):
    if r > n - r:
        r = n - r
    if r == 0:
        return 1
    if r == 1:
        return n % mod
    numerator = [n - r + k + 1 for k in range(r)]
    denominator = [k + 1 for k in range(r)]
    for p in range(2, r + 1):
        pivot = denominator[p - 1]
        if pivot > 1:
            offset = (n - r) % p
            for k in range(p - 1, r, p):
                numerator[k - offset] // = pivot
                denominator[k] // = pivot
    result = 1
    for k in range(r):
        if numerator[k] > 1:
            result = result * numerator[k] % mod
    return result

n, a, b = map(int, input().split())
mod = 10**9+7
print((pow(2, n, mod) - 1 - comb(n, a, mod) - comb(n, b, mod)) % mod)

=======
Suggestion 5

def f(a,b,n):
    MOD = 10**9 + 7
    ans = pow(n,2,MOD)
    ans -= n
    ans -= n
    ans += 1
    ans %= MOD
    ans -= n-a+1
    ans %= MOD
    ans -= n-b+1
    ans %= MOD
    ans += n-a-b+2
    ans %= MOD
    return ans

n,a,b = map(int,input().split())
print(f(a,b,n))

=======
Suggestion 6

def main():
    n, a, b = map(int, input().split())
    if a > b:
        a, b = b, a
    if b - a == 1:
        print(n*(n-1) % (10**9+7))
    else:
        print((n-a-b+1)*(n-a-b+2) % (10**9+7))

=======
Suggestion 7

def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b,a%b)

n,a,b = map(int,input().split())

=======
Suggestion 8

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

=======
Suggestion 9

def main():
    N, A, B = map(int, input().split())
    MOD = 10**9 + 7

    t = pow(2, N, MOD) - 1
    c = 1
    for i in range(N, N - A, -1):
        c = c * i % MOD
    for i in range(1, A + 1):
        c = c * pow(i, MOD - 2, MOD) % MOD
    t -= c

    c = 1
    for i in range(N, N - B, -1):
        c = c * i % MOD
    for i in range(1, B + 1):
        c = c * pow(i, MOD - 2, MOD) % MOD
    t -= c

    print((t % MOD + MOD) % MOD)
