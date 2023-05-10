def main():
    S = input()
    N = len(S)
    dp = [[0, 0] for i in range(N + 1)]
    dp[0][0] = 1
    for i in range(N):
        for j in range(2):
            if j == 1:
                dp[i + 1][j] += dp[i][j] * 8
            else:
                dp[i + 1][j] += dp[i][j]
                if S[i] == "1":
                    dp[i + 1][j + 1] += dp[i][j]
                elif S[i] != "0":
                    dp[i + 1][j] += dp[i][j]
                else:
                    dp[i + 1][j + 1] += dp[i][j]
    print(dp[N][0] + dp[N][1])
