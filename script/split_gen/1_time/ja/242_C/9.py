def main():
    N = int(input())
    #dp[i][j] は i 桁目まで決めて、j で終わる数の個数とする
    dp = [[0] * 10 for _ in range(N + 1)]
    dp[0][0] = 1
    for i in range(N):
        for j in range(10):
            if j == 0:
                dp[i + 1][j] = dp[i][j + 1]
            elif j == 9:
                dp[i + 1][j] = dp[i][j - 1]
            else:
                dp[i + 1][j] = dp[i][j - 1] + dp[i][j + 1]
            dp[i + 1][j] %= 998244353
    print(sum(dp[N]) % 998244353)
