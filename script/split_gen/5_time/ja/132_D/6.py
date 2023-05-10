def main():
    N, K = map(int, input().split())
    # dp[i][j] := i個のボールを並べるとき、j回操作する必要があるボールの並べ方
    dp = [[0 for _ in range(N+1)] for _ in range(K+1)]
    dp[0][0] = 1
    for i in range(1, K+1):
        for j in range(N+1):
            if j >= i:
                dp[i][j] = dp[i-1][j] + dp[i][j-1] - dp[i-1][j-i]
            else:
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
    print(dp[K][N] % (10**9+7))
