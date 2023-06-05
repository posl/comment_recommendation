def main():
    n = int(input())
    mod = 998244353
    dp = [[0 for _ in range(10)] for _ in range(n + 1)]
    dp[1] = [1 for _ in range(10)]
    for i in range(2, n + 1):
        dp[i][0] = dp[i - 1][1]
        for j in range(1, 9):
            dp[i][j] = (dp[i - 1][j - 1] + dp[i - 1][j + 1]) % mod
        dp[i][9] = dp[i - 1][8]
    print(sum(dp[n]) % mod)
