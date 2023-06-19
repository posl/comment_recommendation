def main():
    S = input()
    chokudai = "chokudai"
    mod = 10**9+7
    dp = [[0 for _ in range(len(S)+1)] for _ in range(len(chokudai)+1)]
    for i in range(len(S)+1):
        dp[0][i] = 1
    for i in range(1, len(chokudai)+1):
        for j in range(1, len(S)+1):
            if chokudai[i-1] == S[j-1]:
                dp[i][j] = (dp[i-1][j-1] + dp[i][j-1]) % mod
            else:
                dp[i][j] = dp[i][j-1]
    print(dp[-1][-1])

if __name__ == '__main__':
    main()