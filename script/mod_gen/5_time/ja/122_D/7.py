def main():
    N = int(input())
    mod = 1000000007
    dp = [0] * (N + 1)
    dp[0] = 1
    for i in range(N):
        dp[i + 1] += dp[i] * 3
        if i > 0:
            dp[i + 1] += dp[i - 1] * 2
        if i > 1:
            dp[i + 1] += dp[i - 2] * 2
        dp[i + 1] %= mod
    print(dp[N])

if __name__ == '__main__':
    main()