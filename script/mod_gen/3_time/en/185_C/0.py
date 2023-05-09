def main():
    L = int(input())
    dp = [[0] * (L + 1) for _ in range(L + 1)]
    dp[0][0] = 1
    for i in range(L):
        for j in range(L):
            dp[i + 1][j + 1] += dp[i][j]
            dp[i + j + 1][i] += dp[i][j]
    print(dp[L][L])

if __name__ == '__main__':
    main()