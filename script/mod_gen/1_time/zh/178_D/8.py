def main():
    s = int(input())
    mod = 10**9+7
    dp = [[0]*(s+1) for _ in range(s+1)]
    dp[0][0] = 1
    for i in range(3,s+1):
        for j in range(s+1):
            for k in range(s+1):
                if j + k <= s:
                    dp[i][j+k] += dp[i-1][j]
                    dp[i][j+k] %= mod
    print(dp[s][s])

if __name__ == '__main__':
    main()