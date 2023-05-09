def main():
    S = input()
    MOD = 10**9 + 7
    n = len(S)
    # dp[i][j] = S[0:i]の中からj個選んだ時の組み合わせの数
    dp = [[0] * 9 for _ in range(n+1)]
    dp[0][0] = 1
    for i in range(n):
        for j in range(9):
            if j == 0:
                dp[i+1][j] = 1
            else:
                if S[i] == "chokudai"[j-1]:
                    dp[i+1][j] = (dp[i][j] + dp[i][j-1]) % MOD
                else:
                    dp[i+1][j] = dp[i][j]
    print(dp[n][8])

if __name__ == '__main__':
    main()