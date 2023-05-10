def main():
    s = int(input())
    mod = 10**9 + 7
    dp = [[0] * (s+1) for _ in range(s+1)]
    dp[0][0] = 1
    for i in range(s+1):
        for j in range(s+1):
            if i >= 3 and j >= 3:
                dp[i][j] = (dp[i-3][j-3] + dp[i-1][j]) % mod
            elif i >= 3:
                dp[i][j] = dp[i-3][j]
    print(dp[s][s])

if __name__ == '__main__':
    main()