def main():
    S = input()
    S = S.replace('?', '0')
    mod = 10**9 + 7
    dp = [[0 for _ in range(13)] for _ in range(len(S) + 1)]
    dp[0][0] = 1
    for i in range(len(S)):
        for j in range(13):
            for k in range(10):
                if S[i] != '?' and int(S[i]) != k:
                    continue
                dp[i + 1][(j * 10 + k) % 13] += dp[i][j]
                dp[i + 1][(j * 10 + k) % 13] %= mod
    print(dp[len(S)][5])

if __name__ == '__main__':
    main()