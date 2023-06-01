Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def problems132_d():
    pass

=======
Suggestion 2

def main():
    n, k = map(int, input().split())
    mod = 10 ** 9 + 7
    dp = [[0 for i in range(k + 1)] for j in range(n + 1)]
    dp[0][0] = 1
    for i in range(1, n + 1):
        dp[i][0] = 1
        for j in range(1, k + 1):
            dp[i][j] = (dp[i - 1][j - 1] + dp[i - 1][j] * (j + 1)) % mod
    for i in range(1, k + 1):
        print(dp[n][i])

=======
Suggestion 3

def main():
    n, k = map(int, input().split())
    mod = 10 ** 9 + 7
    dp = [[0 for j in range(n + 1)] for i in range(k + 1)]
    dp[0][0] = 1
    for i in range(1, k + 1):
        s = 0
        for j in range(n + 1):
            s += dp[i - 1][j]
            s %= mod
            dp[i][j] = s
            if j >= i:
                s -= dp[i - 1][j - i]
                s %= mod
    print(dp[k][n])

=======
Suggestion 4

def main():
    n,k = map(int,input().split())
    mod = 10**9+7
    dp = [[0 for _ in range(n+1)] for _ in range(n+1)]
    dp[0][0] = 1
    for i in range(n):
        for j in range(i+1):
            dp[i+1][j] += dp[i][j]
            dp[i+1][j] %= mod
            dp[i+1][j+1] += dp[i][j]
            dp[i+1][j+1] %= mod
    for i in range(1,k+1):
        ans = dp[n-k][i]*dp[k][i]%mod
        print(ans)

=======
Suggestion 5

def main():
    # 读取输入
    n, k = map(int, input().split())

    # 生成组合数表
    comb = [[0 for _ in range(k + 1)] for _ in range(n + 1)]
    for i in range(n + 1):
        comb[i][0] = 1
        for j in range(1, k + 1):
            comb[i][j] = (comb[i - 1][j] + comb[i - 1][j - 1]) % (10 ** 9 + 7)

    # 计算答案
    ans = [0 for _ in range(k + 1)]
    for i in range(1, k + 1):
        for j in range(1, n + 1):
            if i * j <= n:
                ans[i] = (ans[i] + comb[n - (i - 1) * j][j]) % (10 ** 9 + 7)

    # 输出
    for i in range(1, k + 1):
        print(ans[i])

=======
Suggestion 6

def C(n, r):
    if n == 0 or r == 0:
        return 1
    if r > n:
        return 0
    if n == r:
        return 1
    if n - r < r:
        r = n - r
    return C(n - 1, r - 1) * n // r

n, k = map(int, input().split())
MOD = 10**9 + 7
for i in range(1, k + 1):
    ans = C(n - k + 1, i) * C(k - 1, i - 1) % MOD
    print(ans)

=======
Suggestion 7

def main():
    n,k = map(int,input().split())
    mod = 10**9+7
    dp = [[0]*(n+1) for _ in range(k+1)]
    dp[0][0] = 1
    for i in range(k):
        for j in range(n+1):
            dp[i+1][j] = (dp[i+1][j-1] + dp[i][j]) % mod
            if j >= i+1:
                dp[i+1][j] -= dp[i][j-i-1]
                dp[i+1][j] %= mod
    print(dp[k][n])

=======
Suggestion 8

def func(n, k):
    # dp[i][j]表示前i个球中有j个蓝球的方案数
    dp = [[0 for i in range(k+1)] for j in range(n+1)]
    dp[1][1] = 1
    dp[1][0] = 1
    for i in range(2, n+1):
        for j in range(k+1):
            if j == 0:
                dp[i][j] = dp[i-1][j+1]
            elif j == k:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = dp[i-1][j+1] + dp[i-1][j-1]
    return dp[n][k]

=======
Suggestion 9

def main():
    n,k = map(int,input().split())
    mod = 10**9+7
    dp = [[0]*(k+1) for _ in range(n+1)]
    dp[0][0] = 1
    for i in range(1,n+1):
        for j in range(k+1):
            if j == 0:
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i-1][j] + dp[i-1][j-1]*(k-j+1)
                dp[i][j] %= mod
    for i in range(1,k+1):
        print(dp[n][i])
