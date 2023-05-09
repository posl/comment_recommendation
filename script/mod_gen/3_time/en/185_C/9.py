def main():
    L = int(input())
    # dp[i][j]: i個の棒をjの長さに分割する方法の数
    dp = [[0] * (L + 1) for _ in range(L + 1)]
    dp[1][1] = 1
    for i in range(2, L + 1):
        for j in range(1, L + 1):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
    print(dp[L][L])

if __name__ == '__main__':
    main()