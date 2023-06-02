Synthesizing 10/10 solutions

=======
Suggestion 1

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

=======
Suggestion 2

def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)

=======
Suggestion 3

def gcd(a,b):
    if a<b:
        a,b=b,a
    while b!=0:
        a,b=b,a%b
    return a

=======
Suggestion 4

def gcd(a, b):
    while b:
        a, b = b, a%b
    return a

=======
Suggestion 5

def main():
    n,a,b = map(int,input().split())
    mod = 10**9+7
    if a+b>n:
        print(0)
        return
    ans = pow(2,n,mod)-1
    def cmb(n,r,mod):
        if r==0:return 1
        if r<0:return 0
        if (n-r)<r:r=n-r
        num = den = 1
        for i in range(r):
            num = num*(n-i)%mod
            den = den*(i+1)%mod
        return num*pow(den,mod-2,mod)%mod
    print((ans-cmb(n,a,mod)-cmb(n,b,mod))%mod)

=======
Suggestion 6

def main():
    n, a, b = map(int, input().split())
    if a > b:
        a, b = b, a
    MOD = 10 ** 9 + 7
    ans = pow(n, 2, MOD)
    ans -= (n - a + 1) ** 2
    ans -= (n - b + 1) ** 2
    ans += (n - a - b + 2) ** 2
    ans %= MOD
    ans *= pow(2, MOD - 2, MOD)
    print(ans)

=======
Suggestion 7

def solve(n, a, b):
    MOD = 10**9 + 7
    ans = pow(n, 2, MOD)
    ans -= pow(n - a, 2, MOD)
    ans -= pow(n - b, 2, MOD)
    ans += pow(n - a - b, 2, MOD)
    ans %= MOD
    ans = ans * (n - 2) % MOD
    ans = ans * (n - 1) % MOD
    ans = ans * 500000004 % MOD
    return ans

n, a, b = map(int, input().split())
print(solve(n, a, b))

=======
Suggestion 8

def main():
    n, a, b = map(int, input().split())
    mod = 10**9 + 7
    ans = pow(2, n, mod) - 1
    c = 1
    for i in range(a):
        c *= n - i
        c %= mod
        c *= pow(a - i, mod - 2, mod)
        c %= mod
    for i in range(b):
        c *= n - i
        c %= mod
        c *= pow(b - i, mod - 2, mod)
        c %= mod
    ans -= c
    ans %= mod
    print(ans)

=======
Suggestion 9

def main():
    n, a, b = map(int, input().split())
    if n < a or n < b:
        print(0)
        return
    if a + b > n:
        print(0)
        return
    if a == b:
        print(1)
        return
    if a > n/2:
        a = n - a
    if b > n/2:
        b = n - b
    if a == 1:
        print(n)
        return
    if b % a == 0:
        print(2)
        return
    if a == 2:
        print(n - b)
        return
    if b % a == 1:
        print(2)
        return
    print(1)

=======
Suggestion 10

def main():
    pass
