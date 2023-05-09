Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, K = map(int, input().split())
    MOD = 10**9 + 7
    ans = 0
    for i in range(K, N+2):
        ans += i*(N-i+1)+1
        ans %= MOD
    print(ans)

=======
Suggestion 2

def main():
    n, k = map(int, input().split())
    mod = 10**9+7
    ans = 0
    for i in range(k, n+2):
        ans += (i*(n-i+1)+1)%mod
        ans %= mod
    print(ans)

=======
Suggestion 3

def main():
    n, k = map(int, input().split())
    mod = 10**9+7
    ans = 0
    for i in range(k, n+2):
        ans += (n+2-i)*i+1
        ans %= mod
    print(ans)

=======
Suggestion 4

def solve(n, k):
    mod = 10**9+7
    ans = 0
    for i in range(k, n+2):
        ans += (n-i+1)*i+1
        ans %= mod
    return ans

=======
Suggestion 5

def solve():
    #import sys
    #input = sys.stdin.readline
    n, k = map(int, input().split())
    mod = 10**9 + 7
    ans = 0
    for i in range(k, n+2):
        ans += (n-i+1)*i + 1
        ans %= mod
    print(ans)

solve()

=======
Suggestion 6

def main():
    N, K = map(int, input().split())
    MOD = 10**9+7
    if K == 1:
        print(N+1)
        exit()
    if K == N+1:
        print(1)
        exit()
    ans = 0
    for i in range(K, N+2):
        ans += (N+1-i+1)*i + 1
        ans %= MOD
    print(ans)

=======
Suggestion 7

def solve(N,K):
    MOD = 10**9+7
    ans = 0
    for i in range(K,N+2):
        ans += (N+1)*i - i*(i-1) + 1
        ans %= MOD
    return ans

=======
Suggestion 8

def main():
    N, K = map(int, input().split())
    MOD = 10**9 + 7

    if N == K:
        print(1)
        exit()

    if K == 1:
        print((N+1)*(N+1))
        exit()

    ans = 0
    for i in range(K, N+2):
        ans += i*(N+1-i+1) + 1
        ans %= MOD

    print(ans)

=======
Suggestion 9

def main():
    n, k = map(int, input().split())
    mod = 10**9 + 7
    a = [i for i in range(n+1)]
    b = [i for i in range(n, -1, -1)]

    # print(a)
    # print(b)

    ans = 0
    for i in range(k, n+2):
        # print(i)
        # print(a[i])
        # print(b[i])
        ans += b[i] - a[i] + 1
        ans %= mod

    print(ans)

=======
Suggestion 10

def solve():
    N, K = map(int, input().split())

    if K == 1:
        print(N + 1)
        return

    if K == N + 1:
        print(1)
        return

    MOD = 10 ** 9 + 7

    def modpow(a, n):
        if n == 0:
            return 1
        if n % 2 == 0:
            return modpow(a * a % MOD, n // 2)
        else:
            return a * modpow(a, n - 1) % MOD

    def modinv(a):
        return modpow(a, MOD - 2)

    def modcomb(n, r):
        if n < 0 or r < 0 or n < r:
            return 0
        return fact[n] * modinv(fact[r]) * modinv(fact[n - r]) % MOD

    fact = [1] * (N + 1)
    for i in range(1, N + 1):
        fact[i] = fact[i - 1] * i % MOD

    ans = 0
    for i in range(min(N, K - 1) + 1):
        ans += modcomb(N, i) * modcomb(N - 1, i) % MOD
        ans %= MOD

    print(ans)

solve()
