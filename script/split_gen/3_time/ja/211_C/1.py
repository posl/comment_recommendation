def main():
    S = input()
    mod = 10**9 + 7
    dp = [[0] * 9 for _ in range(len(S) + 1)]
    dp[0][0] = 1
    for i in range(len(S)):
        for j in range(9):
            if j == 0:
                dp[i+1][j] = dp[i][j] * 2
            else:
                dp[i+1][j] = dp[i][j] + dp[i][j-1] * (S[i] == "chokudai"[j])
    print(dp[-1][-1] % mod)
