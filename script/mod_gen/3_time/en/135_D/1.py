def main():
    S = input()
    N = len(S)
    dp = [[0] * 13 for _ in range(N + 1)]
    dp[0][0] = 1
    for i in range(N):
        if S[i] == '?':
            for j in range(10):
                for k in range(13):
                    dp[i + 1][(k * 10 + j) % 13] += dp[i][k]
        else:
            for k in range(13):
                dp[i + 1][(k * 10 + int(S[i])) % 13] += dp[i][k]
    print(dp[N][5] % (10 ** 9 + 7))

if __name__ == '__main__':
    main()