def main():
    n = int(input())
    s = [input() for _ in range(n)]
    dp = [[0, 0] for _ in range(n+1)]
    dp[0][0] = 1
    dp[0][1] = 1
    MOD = 10**9 + 7
    for i in range(n):
        if s[i] == "AND":
            dp[i+1][0] = dp[i][0] * 2 + dp[i][1]
            dp[i+1][1] = dp[i][1]
        else:
            dp[i+1][0] = dp[i][0]
            dp[i+1][1] = dp[i][0] + dp[i][1] * 2
        dp[i+1][0] %= MOD
        dp[i+1][1] %= MOD
    print(dp[n][1])

if __name__ == '__main__':
    main()