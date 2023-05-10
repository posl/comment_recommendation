def main():
    S = input()
    S_len = len(S)
    dp = [[0 for i in range(13)] for j in range(S_len + 1)]
    dp[0][0] = 1
    for i in range(S_len):
        if S[i] == '?':
            for j in range(10):
                for k in range(13):
                    dp[i + 1][(k * 10 + j) % 13] += dp[i][k]
                    dp[i + 1][(k * 10 + j) % 13] %= 1000000007
        else:
            for k in range(13):
                dp[i + 1][(k * 10 + int(S[i])) % 13] += dp[i][k]
                dp[i + 1][(k * 10 + int(S[i])) % 13] %= 1000000007
    print(dp[S_len][5])

if __name__ == '__main__':
    main()