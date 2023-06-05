def main():
    s = input()
    n = len(s)
    dp = [[0 for _ in range(13)] for _ in range(n + 1)]
    dp[0][0] = 1
    for i in range(n):
        for j in range(10):
            if s[i] != '?' and int(s[i]) != j:
                continue
            for k in range(13):
                dp[i + 1][(k * 10 + j) % 13] += dp[i][k]
        for k in range(13):
            dp[i + 1][k] %= 10 ** 9 + 7
    print(dp[n][5])
