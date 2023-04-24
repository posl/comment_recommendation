Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, K = map(int, input().split())
    MOD = 10 ** 9 + 7
    ans = 0
    for i in range(K, N + 2):
        ans += (i * (N + 1) - i * (i - 1) // 2) - (i * (i - 1) // 2 - (i - 1) * (i - 2) // 2) + 1
    print(ans % MOD)

=======
Suggestion 2

def main():
    N, K = map(int, input().split())
    MOD = 10**9+7
    ans = 0
    for i in range(K, N+2):
        ans += (N-i+1)*i+1
        ans %= MOD
    print(ans)

=======
Suggestion 3

def main():
    N, K = map(int, input().split())
    MOD = 10**9+7
    ans = 0
    for i in range(K, N+2):
        mn = (i-1)*i//2
        mx = i*(2*N-i+1)//2
        ans += mx-mn+1
        ans %= MOD
    print(ans)

=======
Suggestion 4

def main():
    N,K = map(int,input().split())
    MOD = 10**9+7
    ans = 0
    for i in range(K,N+2):
        a = (i-1)*i//2
        b = (N+i-1)*N//2
        ans += b-a+1
        ans %= MOD
    print(ans)

=======
Suggestion 5

def main():
    N, K = map(int, input().split())
    MOD = 10**9 + 7
    ans = 0
    for i in range(K, N + 2):
        max = i * (2 * N - i + 1) // 2
        min = i * (i - 1) // 2
        ans += max - min + 1
    print(ans % MOD)

=======
Suggestion 6

def solve(N, K):
    mod = 10**9 + 7
    ans = 0
    for i in range(K, N+2):
        min = i*(i-1)//2
        max = i*(2*N-i+1)//2
        ans += max - min + 1
        ans %= mod
    print(ans)

=======
Suggestion 7

def main():
    #input
    N, K = map(int, input().split())

    #compute
    ans = 0
    for i in range(K, N+2):
        ans += i*(N-i+1)+1

    #output
    print(ans%(10**9+7))

=======
Suggestion 8

def main():
    N, K = map(int, input().split())
    print((N-K+2)*(K-1) % (10**9+7))

=======
Suggestion 9

def solve(n, k):
    mod = 10 ** 9 + 7
    return (n + 1 - k) * (n + 2) * k // 2 % mod

=======
Suggestion 10

def main():
    N, K = map(int, input().split())
    MOD = 10 ** 9 + 7

    # 1. 1回目のループ
    #   1.1. 1回目のループの条件
    #       1.1.1. 2回目のループの条件
    #
