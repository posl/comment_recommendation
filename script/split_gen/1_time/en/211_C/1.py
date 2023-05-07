def main():
    S = input()
    mod = 10**9 + 7
    dp = [[0 for i in range(9)] for j in range(len(S) + 1)]
    dp[0][0] = 1
    for i in range(len(S)):
        for j in range(9):
            if j == 8:
                dp[i + 1][j] = dp[i][j]
            elif S[i] == 'chokudai'[j]:
                dp[i + 1][j + 1] = dp[i][j + 1] + dp[i][j]
                dp[i + 1][j + 1] %= mod
            else:
                dp[i + 1][j + 1] = dp[i][j + 1]
    print(dp[len(S)][8])
