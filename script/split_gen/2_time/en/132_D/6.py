def main():
    N, K = map(int, input().split())
    # dp[i][j] := i個のボールからj個の青いボールを選ぶ場合の数
    dp = [[0] * (K + 1) for _ in range(N + 1)]
    dp[0][0] = 1
    for i in range(1, N + 1):
        for j in range(0, K + 1):
            if j == 0:
                dp[i][j] = 1
            else:
                dp[i][j] = (dp[i - 1][j - 1] + dp[i - 1][j]) % (10 ** 9 + 7)
    for i in range(1, K + 1):
        print(dp[N - K + 1][i] * dp[K - 1][i - 1] % (10 ** 9 + 7))
