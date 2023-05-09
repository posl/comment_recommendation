def main():
    S = input()
    MOD = 10**9+7
    dp = [[0]*9 for _ in range(len(S)+1)]
    dp[0][0] = 1
    for i in range(len(S)):
        for j in range(9):
            if S[i] == 'c':
                if j == 0:
                    dp[i+1][j] = dp[i][j] + dp[i][j+1]
                elif j == 1:
                    dp[i+1][j] = dp[i][j] + dp[i][j+1]
                else:
                    dp[i+1][j] = dp[i][j]
            elif S[i] == 'h':
                if j == 2:
                    dp[i+1][j] = dp[i][j] + dp[i][j+1]
                elif j == 3:
                    dp[i+1][j] = dp[i][j] + dp[i][j+1]
                else:
                    dp[i+1][j] = dp[i][j]
            elif S[i] == 'o':
                if j == 4:
                    dp[i+1][j] = dp[i][j] + dp[i][j+1]
                elif j == 5:
                    dp[i+1][j] = dp[i][j] + dp[i][j+1]
                else:
                    dp[i+1][j] = dp[i][j]
            elif S[i] == 'k':
                if j == 6:
                    dp[i+1][j] = dp[i][j] + dp[i][j+1]
                elif j == 7:
                    dp[i+1][j] = dp[i][j] + dp[i][j+1]
                else:
                    dp[i+1][j] = dp[i][j]
            elif S[i] == 'u':
                if j == 8:
                    dp[i+1][j] = dp[i][j] + dp[i][j+1]
                elif j == 9:
                    dp[i+1][j] = dp[i][j] + dp[i][j+1]
                else:
                    dp[i+1][j] = dp[i][j]
            elif S[i] == 'd':
                if j == 10:
                    dp[i+

if __name__ == '__main__':
    main()