def main():
    s = input()
    t = "chokudai"
    mod = 10 ** 9 + 7
    dp = [[0] * (len(t) + 1) for _ in range(len(s) + 1)]
    for i in range(len(s) + 1):
        dp[i][0] = 1
    for i in range(len(s)):
        for j in range(len(t)):
            if s[i] == t[j]:
                dp[i + 1][j + 1] = (dp[i][j + 1] + dp[i][j]) % mod
            else:
                dp[i + 1][j + 1] = dp[i][j + 1]
    print(dp[len(s)][len(t)])
