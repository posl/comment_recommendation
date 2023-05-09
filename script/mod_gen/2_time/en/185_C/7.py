def main():
    L = int(input())
    dp = [[0 for _ in range(L + 1)] for _ in range(L + 1)]
    for l in range(1, L + 1):
        dp[l][l] = 1
    for l in range(1, L + 1):
        for i in range(1, L - l + 1):
            for j in range(i, L - l + 1):
                dp[i][i + l] += dp[i][j] * dp[j + 1][i + l]
    print(dp[1][L])

if __name__ == '__main__':
    main()