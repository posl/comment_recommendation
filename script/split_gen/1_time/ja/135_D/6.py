def main():
    S = input()
    S = S[::-1]
    dp = [[0] * 13 for _ in range(len(S) + 1)]
    dp[0][0] = 1
    for i, s in enumerate(S):
        if s == '?':
            for j in range(13):
                for k in range(10):
                    dp[i + 1][(j * 10 + k) % 13] += dp[i][j]
        else:
            for j in range(13):
                dp[i + 1][(j * 10 + int(s)) % 13] += dp[i][j]
        for j in range(13):
            dp[i + 1][j] %= 1000000007
    print(dp[len(S)][5])
