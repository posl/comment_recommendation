Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n, k = map(int, input().split())
    mod = 10 ** 9 + 7
    ans = 0
    for i in range(k, n + 2):
        ans += (n + n - i + 1) * i // 2 - (n - i + 1) * i + 1
        ans %= mod
    print(ans)

=======
Suggestion 2

def main():
    n, k = map(int, input().split())
    mod = 10**9+7
    ans = 0
    for i in range(k, n+2):
        #print(i)
        ans += i*(n+1-i+1)+1
        ans %= mod
    print(ans)

=======
Suggestion 3

def comb(n, r):
    if n < r:
        return 0
    if n == r:
        return 1
    if n - r < r:
        r = n - r
    over = 1
    under = 1
    for i in range(r):
        over *= n - i
        under *= i + 1
    return over // under

N, K = map(int, input().split())
mod = 10 ** 9 + 7
ans = 0
for i in range(K, N + 2):
    ans += comb(N + 1, i)
    ans %= mod
print(ans)

=======
Suggestion 4

def calc(n,k):
    if k == 1:
        return n+1
    elif k == n+1:
        return 1
    else:
        return n+1

n,k=map(int,input().split())
ans = 0
for i in range(1,k+1):
    ans += calc(n,i)
    ans %= 10**9+7
print(ans)

=======
Suggestion 5

def main():
    n, k = map(int, input().split())
    mod = 10**9+7
    ans = 0
    for i in range(k, n+2):
        ans += (n+1-i)*i+1
    print(ans%mod)

=======
Suggestion 6

def main():
    n,k = map(int,input().split())
    mod = 10**9+7
    ans = 0
    for i in range(k,n+2):
        ans += (n+1-i)*i+1
        ans %= mod
    print(ans)

=======
Suggestion 7

def main():
    N, K = map(int, input().split())
    mod = 10**9+7
    ans = 0

    for i in range(K, N+2):
        ans += (N+1)*i - i*(i-1) + 1
        ans %= mod

    print(ans)

main()

=======
Suggestion 8

def comb(n, r, mod):
    if (r < 0) or (n < r):
        return 0
    r = min(r, n - r)
    return fact[n] * factinv[r] * factinv[n-r] % mod

N, K = map(int, input().split())
mod = 10**9+7
N += 1
fact = [1, 1] # 階乗を格納するリスト
factinv = [1, 1] # 階乗の逆元を格納するリスト
inv = [0, 1] # 逆元を計算するためのリスト
for i in range(2, N+K+1):
    fact.append((fact[-1] * i) % mod)
    inv.append((-inv[mod % i] * (mod//i)) % mod)
    factinv.append((factinv[-1] * inv[-1]) % mod)
result = 0
for i in range(K, N+1):
    result += comb(N, i, mod) * comb(N-1, i-1, mod)
    result %= mod
print(result)

=======
Suggestion 9

def main():
    n,k = map(int, input().split())

    mod = 10**9+7

    ans = 0
    for i in range(k,n+2):
        ans += i*n - i*(i-1) + 1
        ans %= mod

    print(ans)

=======
Suggestion 10

def main():
    n,k = map(int,input().split())
    mod = 10**9+7
    ans = 0
    for i in range(k,n+2):
        ans += (n-i+1)*i+1
        ans %= mod
    print(ans)
