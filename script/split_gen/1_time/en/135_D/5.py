def main():
    s = input()
    mod = 10**9 + 7
    dp = [[0] * 13 for i in range(len(s) + 1)]
    dp[0][0] = 1
    for i, c in enumerate(s):
        if c == "?":
            for j in range(10):
                for k in range(13):
                    dp[i + 1][(k * 10 + j) % 13] += dp[i][k]
                    dp[i + 1][(k * 10 + j) % 13] %= mod
        else:
            for k in range(13):
                dp[i + 1][(k * 10 + int(c)) % 13] += dp[i][k]
                dp[i + 1][(k * 10 + int(c)) % 13] %= mod
    print(dp[-1][5])
