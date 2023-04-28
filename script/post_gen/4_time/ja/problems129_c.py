Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    a = [int(input()) for _ in range(M)]
    mod = 1000000007
    dp = [0] * (N + 1)
    dp[0] = 1
    dp[1] = 1 if 1 not in a else 0
    for i in range(2, N + 1):
        if i in a:
            continue
        dp[i] = (dp[i - 1] + dp[i - 2]) % mod
    print(dp[N])

=======
Suggestion 2

def main():
    n, m = map(int, input().split())
    a = [int(input()) for _ in range(m)]
    mod = 10**9+7
    dp = [0]*(n+1)
    dp[0] = 1
    for i in range(n):
        if i+1 in a:
            continue
        if i+1 <= n:
            dp[i+1] += dp[i]
            dp[i+1] %= mod
        if i+2 <= n:
            dp[i+2] += dp[i]
            dp[i+2] %= mod
    print(dp[-1])

=======
Suggestion 3

def main():
    N, M = map(int, input().split())
    A = [int(input()) for _ in range(M)]
    MOD = 10 ** 9 + 7
    dp = [0] * (N + 1)
    dp[0] = 1
    for i in range(N):
        for j in range(1, 3):
            if i + j in A:
                continue
            if i + j > N:
                continue
            dp[i + j] += dp[i]
            dp[i + j] %= MOD
    print(dp[N])

=======
Suggestion 4

def main():
    n, m = map(int, input().split())
    a = [int(input()) for i in range(m)]
    mod = 1000000007
    dp = [0] * (n + 1)
    dp[0] = 1
    for i in range(1, n + 1):
        if i in a:
            continue
        dp[i] = dp[i - 1] + dp[i - 2]
        dp[i] %= mod
    print(dp[n])

=======
Suggestion 5

def main():
    N, M = map(int, input().split())
    A = [int(input()) for _ in range(M)]
    mod = 10**9 + 7
    dp = [0] * (N + 1)
    dp[0] = 1
    for i in range(1, N + 1):
        if i in A:
            continue
        dp[i] = (dp[i - 1] + dp[i - 2]) % mod
    print(dp[N])

=======
Suggestion 6

def main():
    N, M = map(int, input().split())
    a = [int(input()) for _ in range(M)]
    mod = 10**9+7
    dp = [0]*(N+1)
    dp[0] = 1
    for i in range(1, N+1):
        if i not in a:
            if i == 1:
                dp[i] = dp[i-1]
            else:
                dp[i] = (dp[i-1] + dp[i-2]) % mod
    print(dp[N])

=======
Suggestion 7

def main():
    N, M = map(int, input().split())
    a = [int(input()) for i in range(M)]
    mod = 10**9 + 7
    dp = [0] * (N+1)
    dp[0] = 1
    dp[1] = 1
    for i in range(2, N+1):
        if i in a:
            continue
        dp[i] = (dp[i-1] + dp[i-2]) % mod
    print(dp[N])

=======
Suggestion 8

def main():
    N,M = map(int,input().split())
    A = [0]*(N+1)
    for i in range(M):
        A[int(input())] = 1
    mod = 10**9+7
    dp = [0]*(N+1)
    dp[0] = 1
    for i in range(1,N+1):
        if A[i] == 1:
            dp[i] = 0
        else:
            dp[i] = (dp[i-1] + dp[i-2])%mod
    print(dp[N])

=======
Suggestion 9

def main():
    pass
    n,m = map(int,input().split())
    a = [int(input()) for _ in range(m)]
    mod = 10**9+7
    dp = [0]*(n+1)
    dp[0] = 1
    for i in range(1,n+1):
        if i in a:
            continue
        dp[i] = dp[i-1] + dp[i-2]
        dp[i] %= mod
    print(dp[n])

=======
Suggestion 10

def main():
    N,M = map(int, input().split())
    a = []
    for i in range(M):
        a.append(int(input()))
    a.append(N+1)
    d = [0]*(N+2)
    d[0] = 1
    for i in range(N+1):
        for j in range(M+1):
            if a[j] == i+1:
                break
            d[i+1] += d[i-j]
            d[i+1] %= 1000000007
    print(d[N])

main()
