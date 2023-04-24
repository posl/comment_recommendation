Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n, m = map(int, input().split())
    a = [int(input()) for _ in range(m)]
    dp = [0] * (n+1)
    dp[0] = 1
    for i in range(1, n+1):
        if i in a:
            continue
        dp[i] = dp[i-1] + dp[i-2]
    print(dp[-1] % (10**9+7))

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    A = [int(input()) for _ in range(M)]
    MOD = 10**9 + 7
    dp = [0] * (N+1)
    dp[0] = 1
    for i in range(1, N+1):
        if i not in A:
            dp[i] = (dp[i-1] + dp[i-2]) % MOD
    print(dp[N])

=======
Suggestion 3

def main():
    N, M = map(int, input().split())
    A = [int(input()) for _ in range(M)]
    MOD = 1000000007
    dp = [0] * (N + 1)
    dp[0] = 1
    for i in range(1, N + 1):
        if i in A:
            dp[i] = 0
        else:
            dp[i] = dp[i - 1] + dp[i - 2]
            dp[i] %= MOD
    print(dp[N])

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    a = [int(input()) for _ in range(M)]
    dp = [0] * (N+1)
    dp[0] = 1
    dp[1] = 1
    for i in range(2, N+1):
        if i in a:
            continue
        dp[i] = dp[i-1] + dp[i-2]
        dp[i] %= 1000000007
    print(dp[N])

=======
Suggestion 5

def main():
    N, M = map(int, input().split())
    A = set([int(input()) for _ in range(M)])
    mod = 10**9 + 7
    dp = [0] * (N+1)
    dp[0] = 1
    for i in range(1, N+1):
        if i in A:
            dp[i] = 0
        else:
            dp[i] = (dp[i-1] + dp[i-2]) % mod
    print(dp[N])

=======
Suggestion 6

def main():
    # input
    N, M = map(int, input().split())
    As = [int(input()) for _ in range(M)]

    # compute
    """WRITE BELOW"""
    dp = [0] * (N+1)
    dp[0] = 1
    for i in range(N):
        if i not in As:
            dp[i+1] += dp[i]
            dp[i+1] %= 10**9 + 7
        if i+1 not in As:
            dp[i+2] += dp[i]
            dp[i+2] %= 10**9 + 7

    # output
    print(dp[-1])

=======
Suggestion 7

def main():
    N, M = map(int, input().split())
    A = [int(input()) for i in range(M)]
    A.append(N)
    A = [0] + A
    dp = [0] * (N+1)
    dp[0] = 1
    dp[1] = 1
    for i in range(1, N+1):
        if i in A:
            continue
        dp[i] = dp[i-1] + dp[i-2]
        dp[i] %= 1000000007
    print(dp[N])

=======
Suggestion 8

def main():
    #input
    N, M = map(int, input().split())
    a = [0] * M
    for i in range(M):
        a[i] = int(input())
    a.append(N)

    #compute
    dp = [0] * (N+1)
    dp[0] = 1
    dp[1] = 1
    for i in range(2, N+1):
        if i in a:
            dp[i] = 0
        else:
            dp[i] = (dp[i-1] + dp[i-2]) % 1000000007

    #output
    print(dp[N])

=======
Suggestion 9

def main():
    #read
    N, M = map(int, input().split())
    A = [int(input()) for _ in range(M)]
    MOD = 10**9+7
    
    #solve
    dp = [0] * N
    dp[0] = 1
    for i in range(N):
        if i+1 not in A:
            dp[i+1] += dp[i]
        if i+2 not in A:
            dp[i+2] += dp[i]
        dp[i+1] %= MOD
        dp[i+2] %= MOD
    
    #print
    print(dp[N-1])

=======
Suggestion 10

def main():
    #入力
    N, M = map(int, input().split())
    a = [int(input()) for _ in range(M)]

    #dp[i] := i段目に到達する方法の数
    dp = [0]*(N+1)
    dp[0] = 1
    for i in range(1, N+1):
        if i in a:
            dp[i] = 0
        else:
            dp[i] = dp[i-1] + dp[i-2]
    print(dp[N] % 1000000007)
