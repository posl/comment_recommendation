def main():
    N = int(input())
    dp = [0] * (N + 1)
    dp[0] = 1
    for i in range(1, N + 1):
        dp[i] += dp[i - 1] * 4
        if i >= 2:
            dp[i] += dp[i - 2] * 2
        if i >= 3:
            dp[i] += dp[i - 3] * 3
        if i >= 4:
            dp[i] += dp[i - 4] * 2
        dp[i] %= 1000000007
    print(dp[N])

if __name__ == '__main__':
    main()