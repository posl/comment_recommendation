def main():
    S = input()
    S = S[::-1]
    N = len(S)
    # 累積和
    dp = [[0] * 13 for _ in range(N + 1)]
    dp[0][0] = 1
    for i in range(N):
        for j in range(13):
            if S[i] == "?":
                for k in range(10):
                    dp[i + 1][(j + k * pow(10, i, 13)) % 13] += dp[i][j]
                    dp[i + 1][(j + k * pow(10, i, 13)) % 13] %= 10**9 + 7
            else:
                dp[i + 1][(j + int(S[i]) * pow(10, i, 13)) % 13] += dp[i][j]
                dp[i + 1][(j + int(S[i]) * pow(10, i, 13)) % 13] %= 10**9 + 7
    print(dp[N][5])
