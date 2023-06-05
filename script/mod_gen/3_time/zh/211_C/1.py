def main():
    S = input()
    chokudai = "chokudai"
    N = len(S)
    M = len(chokudai)
    mod = 10**9+7
    dp = [[0 for _ in range(N+1)] for _ in range(M+1)]
    for j in range(N+1):
        dp[0][j] = 1
    for i in range(1,M+1):
        for j in range(1,N+1):
            if chokudai[i-1] == S[j-1]:
                dp[i][j] = dp[i-1][j-1] + dp[i][j-1]
            else:
                dp[i][j] = dp[i][j-1]
    print(dp[M][N]%mod)

if __name__ == '__main__':
    main()