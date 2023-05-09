def main():
    S = input()
    MOD = 10**9 + 7
    # dp[i][j] := i番目までの文字列で、j文字目までの文字を選んだときの選び方
    dp = [[0 for _ in range(9)] for _ in range(len(S) + 1)]
    dp[0][0] = 1
    for i in range(len(S)):
        for j in range(9):
            if S[i] == "c" and j == 0:
                dp[i + 1][j + 1] += dp[i][j]
            elif S[i] == "h" and j == 1:
                dp[i + 1][j + 1] += dp[i][j]
            elif S[i] == "o" and j == 2:
                dp[i + 1][j + 1] += dp[i][j]
            elif S[i] == "k" and j == 3:
                dp[i + 1][j + 1] += dp[i][j]
            elif S[i] == "u" and j == 4:
                dp[i + 1][j + 1] += dp[i][j]
            elif S[i] == "d" and j == 5:
                dp[i + 1][j + 1] += dp[i][j]
            elif S[i] == "a" and j == 6:
                dp[i + 1][j + 1] += dp[i][j]
            elif S[i] == "i" and j == 7:
                dp[i + 1][j + 1] += dp[i][j]
            dp[i + 1][j] += dp[i][j]
            dp[i + 1][j] %= MOD
    print(dp[len(S)][8])

if __name__ == '__main__':
    main()