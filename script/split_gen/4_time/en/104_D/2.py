def main():
    s = input()
    mod = 10**9 + 7
    n = len(s)
    dp = [[0] * 4 for _ in range(n + 1)]
    dp[0][0] = 1
    for i in range(n):
        for j in range(4):
            if s[i] == "?":
                dp[i + 1][j] = (dp[i + 1][j] + dp[i][j] * 3) % mod
            else:
                dp[i + 1][j] = (dp[i + 1][j] + dp[i][j]) % mod
            if j < 3 and (s[i] == "?" or s[i] == "ABC"[j]):
                dp[i + 1][j + 1] = (dp[i + 1][j + 1] + dp[i][j]) % mod
    print(dp[n][3])
