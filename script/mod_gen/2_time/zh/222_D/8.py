def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    # dp[i][j] = (dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1]) + (b[j] - a[i] + 1)
    # dp[i][j] = dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1] + (b[j] - a[i] + 1)
    # dp[i][j] = dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1] + b[j] - a[i] + 1
    # dp[i][j] = dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1] + b[j] - a[i] + 1
    # dp[i][j] = dp[i-1][j] + dp[i][j-1] + b[j] - a[i] + 1 - dp[i-1][j-1]
    # dp[i][j] = dp[i-1][j] + dp[i][j-1] + b[j] - a[i] + 1 - dp[i-1][j-1]
    # dp[i][j] = dp[i-1][j] + dp[i][j-1] + b[j] - a[i] + 1 - dp[i-1][j-1]
    # dp[i][j] = dp[i-1][j] + dp[i][j-1] + b[j] - a[i] + 1 - dp[i-1][j-1]
    # dp[i][j] = dp[i-1][j] + dp[i][j-1] + b[j] - a[i] + 1 - dp[i-1][j-1]
    # dp[i][j] = dp[i-1][j] + dp[i][j-1] + b[j] - a[i] + 1 - dp[i-1][j-1]
    # dp[i][j] = dp[i-1][j] + dp[i][j-1]

if __name__ == '__main__':
    main()