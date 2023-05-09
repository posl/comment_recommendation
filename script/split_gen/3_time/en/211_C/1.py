def main():
    S = input()
    MOD = 10**9 + 7
    dp = [[0] * 9 for _ in range(len(S) + 1)]
    dp[0][0] = 1
    for i in range(len(S)):
        for j in range(9):
            if j == 8:
                dp[i + 1][j] = dp[i][j]
            else:
                if S[i] == 'chokudai'[j]:
                    dp[i + 1][j + 1] = dp[i][j + 1] + dp[i][j]
                else:
                    dp[i + 1][j + 1] = dp[i][j + 1]
    print(dp[len(S)][8] % MOD)
