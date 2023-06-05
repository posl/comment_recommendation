Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n,k = map(int,input().split())
    print(n,k)
    #prin

=======
Suggestion 2

def main():
    n, k = map(int, input().split())
    mod = 10 ** 9 + 7
    dp = [[0] * (k + 1) for _ in range(n + 1)]
    dp[0][0] = 1
    for i in range(1, n + 1):
        dp[i][0] = 1
        for j in range(1, min(i, k) + 1):
            dp[i][j] = (dp[i - 1][j] * j + dp[i - 1][j - 1]) % mod
    for i in range(1, k + 1):
        print(dp[n - k + i][i])

=======
Suggestion 3

def problems132_d():
    n,k = map(int,input().split())
    mod = 10**9+7
    dp = [[0 for _ in range(n+1)] for _ in range(n+1)]
    dp[0][0] = 1
    for i in range(1,n+1):
        dp[i][0] = 1
        for j in range(1,i+1):
            dp[i][j] = (dp[i-1][j-1]+dp[i-1][j])%mod
    for i in range(1,k+1):
        print((dp[n-k+1][i]*dp[k-1][i-1])%mod)

problems132_d()

=======
Suggestion 4

def main():
    n,k = map(int,input().split())
    mod = 10**9+7
    dp = [[0 for i in range(n+1)] for j in range(k+1)]
    dp[0][0] = 1
    for i in range(1,k+1):
        for j in range(n+1):
            dp[i][j] = dp[i-1][j]*(n-k+1+i-1)//(i)
            dp[i][j] %= mod
    for i in range(1,k+1):
        print(dp[i][n])

=======
Suggestion 5

def problems132_d():
    n,k = map(int,input().split())
    mod = 10**9+7
    dp = [[0 for i in range(n+1)] for j in range(k+1)]
    dp[0][0] = 1
    for i in range(1,k+1):
        for j in range(n+1):
            if j-i >= 0:
                dp[i][j] = (dp[i-1][j] + dp[i][j-1])%mod
            else:
                dp[i][j] = dp[i-1][j]
    print(dp[k][n])

=======
Suggestion 6

def problems132_d():
    pass

=======
Suggestion 7

def problems132_d():
    n,k = map(int,input().split())
    mod = 10**9+7
    #dp[i][j]表示i个球，j步走完的方案数
    dp = [[0]*(k+1) for i in range(n+1)]
    dp[0][0] = 1
    for i in range(n):
        for j in range(k):
            dp[i+1][j+1] += dp[i][j+1]
            dp[i+1][j+1] %= mod
            dp[i+1][j] += dp[i][j]*(n-k-i+j+1)
            dp[i+1][j] %= mod
    print(dp[n][k])

=======
Suggestion 8

def main():
    N, K = map(int, input().split())
    mod = 10**9 + 7
    # 有多少种方法可以安排球，使Takahashi正好需要i步棋
    dp = [[0 for _ in range(K+1)] for _ in range(N+1)]
    dp[0][0] = 1
    for i in range(1, N+1):
        for j in range(K+1):
            # 蓝球的数量
            for k in range(j+1):
                dp[i][j] += dp[i-1][j-k]
                dp[i][j] %= mod
    for i in range(1, K+1):
        res = dp[N-K][i] * dp[K][K-i]
        res %= mod
        print(res)

=======
Suggestion 9

def main():
    n,k = map(int, input().split())
    mod = 10**9+7
    dp = [[0]*(k+1) for _ in range(n+1)]
    dp[0][0] = 1
    for i in range(n):
        for j in range(k+1):
            if j == 0:
                dp[i+1][j] = dp[i][j]
            else:
                dp[i+1][j] = (dp[i][j] + dp[i][j-1]*(n-k-i))%mod
    for i in range(1,k+1):
        print(dp[n][i])

=======
Suggestion 10

def main():
    N, K = map(int, input().split())
    # N, K = 5, 3
    MOD = 10**9 + 7
    dp = [[0 for _ in range(N+1)] for _ in range(K+1)]
    dp[0][0] = 1
    for i in range(1, K+1):
        for j in range(N+1):
            if j - i >= 0:
                dp[i][j] = (dp[i][j-i] + dp[i-1][j]) % MOD
            else:
                dp[i][j] = dp[i-1][j]
    print(dp[K][N])
