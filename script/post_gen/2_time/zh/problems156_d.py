Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def gcd(a,b):
    if a%b==0:
        return b
    else:
        return gcd(b,a%b)

=======
Suggestion 2

def main():
    n,a,b = map(int,input().split())
    if a%2==0 and b%2==0:
        print(0)
        return
    if a%2==0:
        a,b = b,a
    if a==1:
        print(0)
        return
    if b%a==0:
        print(0)
        return
    if n > 2*a-1:
        print((n-2*a+1)*(n-a+1)-(n-b+1)*(n-b+1))
    else:
        print(n-a+1)

=======
Suggestion 3

def main():
    n,a,b = map(int,input().split())
    if a+b>n:
        print(0)
    else:
        ans = pow(2,n,10**9+7)-1
        for i in range(n-a+1,n-b+1):
            ans -= comb(n,i,10**9+7)
        print(ans%(10**9+7))

=======
Suggestion 4

def main():
    n, a, b = map(int, input().split())
    mod = 10**9+7
    ans = pow(2, n, mod) - 1
    nca = 1
    ncb = 1
    for i in range(a):
        nca *= n-i
        nca %= mod
        nca *= pow(i+1, mod-2, mod)
        nca %= mod
    for i in range(b):
        ncb *= n-i
        ncb %= mod
        ncb *= pow(i+1, mod-2, mod)
        ncb %= mod
    ans -= nca
    ans -= ncb
    print(ans%mod)

=======
Suggestion 5

def calc(n,a,b):
    mod = 10**9+7
    ans = pow(n,2,mod)
    ans -= comb(n,a,mod)
    ans -= comb(n,b,mod)
    ans %= mod
    return ans

=======
Suggestion 6

def main():
    n, a, b = map(int, input().split())
    MOD = 10**9 + 7
    ans = pow(2, n, MOD) - 1
    c, d = 1, 1
    for i in range(b):
        c *= n - i
        c %= MOD
        d *= i + 1
        d %= MOD
    ans -= c * pow(d, MOD - 2, MOD)
    c, d = 1, 1
    for i in range(a):
        c *= n - i
        c %= MOD
        d *= i + 1
        d %= MOD
    ans -= c * pow(d, MOD - 2, MOD)
    ans %= MOD
    print(ans)

=======
Suggestion 7

def main():
    n,a,b = map(int,input().split())
    if a>b:
        a,b = b,a
    ans = n*(n-1)
    ans = ans % (10**9+7)
    ans = ans - (n-a)*(n-b)
    ans = ans % (10**9+7)
    print(ans)

=======
Suggestion 8

def func(n,a,b):
    mod = 10**9+7
    if a+b>n+1:
        return 0
    else:
        return pow(2,n,mod) - (comb(n,a,mod)+comb(n,b,mod))%mod
