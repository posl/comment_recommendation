Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, K = map(int, input().split())
    mod = 10**9 + 7
    ans = 0
    for i in range(K, N + 2):
        ans += (N - i + 1) * (N + i) // 2 + 1
        ans %= mod
    print(ans)

=======
Suggestion 2

def solve():
    N, K = map(int, input().split())
    mod = 10**9+7
    ans = 0
    for i in range(K, N+2):
        ans += (N-i+1)*i+1
        ans %= mod
    return ans

=======
Suggestion 3

def main():
    N, K = map(int, input().split())
    MOD = 10**9 + 7
    ans = 0
    for i in range(K, N+2):
        ans += (N - i + 1) * (N + i) // 2 + 1
        ans %= MOD
    print(ans)

=======
Suggestion 4

def main():
    n, k = map(int, input().split())
    ans = 0
    mod = 10**9+7
    for i in range(k, n+2):
        ans += i*n-i*(i-1)+1
        ans %= mod
    print(ans)

=======
Suggestion 5

def main():
    N, K = map(int, input().split())
    if K == 1:
        print(N+1)
    else:
        ans = 0
        for i in range(K, N+2):
            ans += (i*(N-i+1)+1)
        print(ans%1000000007)

=======
Suggestion 6

def main():
    N,K = map(int,input().split())
    mod = 10**9+7
    ans = 0
    for i in range(K,N+2):
        ans += (i*(2*N-i+1)//2) - (i*(i-1)//2) + 1
        ans = ans % mod
    print(ans)

=======
Suggestion 7

def main():
    n, k = map(int, input().split())
    mod = 10**9+7
    ans = 0
    for i in range(k, n+2):
        ans += n * i + 1 - (i-1) * i // 2
        ans %= mod
    print(ans)

=======
Suggestion 8

def comb(n, r):
    if n < r:
        return 0
    if r == 0:
        return 1
    if r > n / 2:
        return comb(n, n - r)
    return comb(n, r - 1) * (n - r + 1) // r

=======
Suggestion 9

def main():
    N, K = map(int, input().split())
    mod = 10**9 + 7
    res = 0
    for i in range(K, N+2):
        res += (i * (2 * N - i + 1)) // 2 - (i * (i - 1)) // 2 + 1
        res = res % mod
    print(res)

=======
Suggestion 10

def main():
    pass
