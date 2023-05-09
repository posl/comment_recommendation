def main():
    L = int(input())
    dp = [[0 for i in range(L+1)] for j in range(L+1)]
    dp[0][0] = 1
    for i in range(1,L+1):
        for j in range(0,L+1):
            if j == 0:
                dp[i][j] = dp[i-1][j+1]
            elif j == L:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]
    print(dp[L][0] % (10**9+7))

if __name__ == '__main__':
    main()