def main():
    s = input()
    chokudai = "chokudai"
    mod = 10 ** 9 + 7
    dp = [[0] * (len(s) + 1) for _ in range(len(chokudai) + 1)]
    for i in range(len(s) + 1):
        dp[0][i] = 1
    for i in range(len(chokudai)):
        for j in range(len(s)):
            if chokudai[i] == s[j]:
                dp[i + 1][j + 1] = (dp[i][j] + dp[i + 1][j]) % mod
            else:
                dp[i + 1][j + 1] = dp[i + 1][j]
    print(dp[len(chokudai)][len(s)])
