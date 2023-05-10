def main():
    N = int(input())
    dp = [[0 for i in range(10)] for i in range(N + 1)]
    dp[0][0] = 1
    for i in range(1, N + 1):
        for j in range(1, 9):
            dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j + 1]
        dp[i][0] = dp[i - 1][1]
        dp[i][9] = dp[i - 1][8]
    print(sum(dp[N]) % 998244353)
