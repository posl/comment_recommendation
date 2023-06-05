def main():
    S = input()
    S = S[::-1]
    mod = 10 ** 9 + 7
    dp = [[0 for _ in range(13)] for _ in range(len(S) + 1)]
    dp[0][0] = 1
    for i in range(len(S)):
        for j in range(13):
            if S[i] == '?':
                for k in range(10):
                    dp[i + 1][(k * pow(10, i, 13) + j) % 13] += dp[i][j]
                    dp[i + 1][(k * pow(10, i, 13) + j) % 13] %= mod
            else:
                dp[i + 1][(int(S[i]) * pow(10, i, 13) + j) % 13] += dp[i][j]
                dp[i + 1][(int(S[i]) * pow(10, i, 13) + j) % 13] %= mod
    print(dp[len(S)][5])

if __name__ == '__main__':
    main()