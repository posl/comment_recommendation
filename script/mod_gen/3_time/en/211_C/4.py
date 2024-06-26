def main():
    S = input()
    N = len(S)
    MOD = 10**9+7
    dp = [[0] * 9 for _ in range(N+1)]
    dp[0][0] = 1
    for i in range(N):
        for j in range(9):
            dp[i+1][j] += dp[i][j]
            dp[i+1][j] %= MOD
            if j < 8 and S[i] == 'chokudai'[j]:
                dp[i+1][j+1] += dp[i][j]
                dp[i+1][j+1] %= MOD
    print(dp[N][8])

if __name__ == '__main__':
    main()