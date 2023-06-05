def main():
    X, Y = map(int, input().split())
    MOD = 10**9 + 7
    dp = [[0 for _ in range(Y+1)] for _ in range(X+1)]
    dp[0][0] = 1
    for i in range(X+1):
        for j in range(Y+1):
            if i+1<=X and j+2<=Y:
                dp[i+1][j+2] += dp[i][j]
                dp[i+1][j+2] %= MOD
            if i+2<=X and j+1<=Y:
                dp[i+2][j+1] += dp[i][j]
                dp[i+2][j+1] %= MOD
    print(dp[X][Y])

if __name__ == '__main__':
    main()