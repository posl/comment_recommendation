def main():
    s = input()
    n = len(s)
    dp = [[0] * 13 for _ in range(n + 1)]
    dp[0][0] = 1
    for i in range(n):
        for j in range(13):
            if s[i] == "?":
                for k in range(10):
                    dp[i + 1][(j * 10 + k) % 13] += dp[i][j]
            else:
                dp[i + 1][(j * 10 + int(s[i])) % 13] += dp[i][j]
    print(dp[n][5] % (10**9 + 7))
