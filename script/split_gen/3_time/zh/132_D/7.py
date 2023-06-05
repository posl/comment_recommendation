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
