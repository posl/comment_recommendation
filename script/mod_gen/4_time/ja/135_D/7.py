def main():
    S = input()
    S = S[::-1]
    ans = 0
    dp = [[0] * 13 for _ in range(len(S) + 1)]
    dp[0][0] = 1
    for i in range(len(S)):
        if S[i] == "?":
            for j in range(10):
                for k in range(13):
                    dp[i + 1][(k * 10 + j) % 13] += dp[i][k]
        else:
            for k in range(13):
                dp[i + 1][(k * 10 + int(S[i])) % 13] += dp[i][k]
        for j in range(13):
            dp[i + 1][j] %= 10 ** 9 + 7
    print(dp[len(S)][5])

if __name__ == '__main__':
    main()