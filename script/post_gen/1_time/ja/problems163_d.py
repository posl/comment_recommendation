Synthesizing 10/10 solutions

=======
Suggestion 1

def cmb(n, r, mod):
    if (r < 0 or r > n):
        return 0
    r = min(r, n - r)
    return fact[n] * factinv[r] * factinv[n-r] % mod

mod = 10**9+7
N, K = map(int, input().split())
fact = [1, 1] # fact[n] = (n! mod p)
factinv = [1, 1] # factinv[n] = ((n!)^(-1) mod p)
inv = [0, 1] # factinv 計算用
for i in range(2, N+K+1):
    fact.append((fact[-1] * i) % mod)
    inv.append((-inv[mod % i] * (mod//i)) % mod)
    factinv.append((factinv[-1] * inv[-1]) % mod)
ans = 0
for i in range(min(K, N+1)):
    ans += cmb(N, i, mod) * cmb(N-1, i, mod)
    ans %= mod
print(ans)

=======
Suggestion 2

def solve():
    n, k = map(int, input().split())
    mod = 10**9 + 7
    ans = 0
    for i in range(k, n+2):
        ans += (n-i+1)*i + 1
        ans %= mod
    print(ans)

=======
Suggestion 3

def main():
    N, K = map(int, input().split())
    mod = 10**9+7
    ans = 0
    for i in range(K, N+2):
        ans += i*N-i*(i-1)+1
        ans %= mod
    print(ans)

=======
Suggestion 4

def main():
    n,k = map(int, input().split())
    mod = 10**9+7
    ans = 0
    for i in range(k,n+2):
        ans += (i*(2*n-i+1)//2 - i*(i-1)//2 + 1)%mod
    print(ans%mod)

=======
Suggestion 5

def main():
    n,k = map(int,input().split())
    ans = 0
    for i in range(k,n+2):
        ans += i*n - i*(i-1) + 1
        ans = ans % (10**9+7)
    print(ans)

=======
Suggestion 6

def main():
    n,k = map(int,input().split())

    ans = 0
    mod = 10**9+7
    for i in range(k,n+2):
        ans += (n-i+1)*i+1
        ans %= mod
    print(ans)

=======
Suggestion 7

def main():
    N, K = map(int, input().split())

    mod = 10**9+7
    ans = 0
    for i in range(K, N+2):
        ans += (i*(N+1-i)+1)%mod
        ans %= mod

    print(ans)

=======
Suggestion 8

def main():
    n,k = map(int, input().split())
    mod = 10**9+7
    ans = 0
    for i in range(k,n+2):
        tmp = (i*(i-1)//2)%mod
        tmp2 = (n*(n+1)//2)%mod
        tmp3 = ((n-i+1)*(n-i+2)//2)%mod
        ans += tmp*tmp2 - tmp*tmp3
        ans %= mod
    print(ans)

=======
Suggestion 9

def get_input():
    N, K = map(int, input().split())
    return N, K

=======
Suggestion 10

def calc(x, y):
    return x * y % MOD
