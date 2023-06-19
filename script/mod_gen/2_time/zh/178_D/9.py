def main():
    s = int(input())
    mod = 1000000007
    # dp[i][j]表示前i个数中和为j的序列的个数
    dp = [[0 for _ in range(s+1)] for _ in range(s+1)]
    dp[0][0] = 1
    for i in range(1, s+1):
        for j in range(s+1):
            dp[i][j] = dp[i-1][j]
            if j >= i:
                dp[i][j] += dp[i][j-i]
                dp[i][j] %= mod
    print(dp[s][s])

if __name__ == '__main__':
    main()