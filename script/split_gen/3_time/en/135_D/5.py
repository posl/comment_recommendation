def main():
    S = input()
    N = len(S)
    dp = [[0] * 13 for _ in range(N + 1)]
    dp[0][0] = 1
    for i, s in enumerate(S):
        for j in range(10):
            if s == '?' or s == str(j):
                for k in range(13):
                    dp[i + 1][(k * 10 + j) % 13] += dp[i][k]
        for j in range(13):
            dp[i + 1][j] %= 10 ** 9 + 7
    print(dp[N][5])
