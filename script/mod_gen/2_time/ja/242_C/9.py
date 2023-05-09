def main():
    N = int(input())
    # dp[i][j][k] = i 桁目まで決めて、j=0: 0 が含まれる, j=1: 0 が含まれない, k=0: 1 が含まれる, k=1: 1 が含まれない
    dp = [[[0]*2 for _ in range(2)] for _ in range(N)]
    # 初期条件
    dp[0][0][0] = 1
    dp[0][1][0] = 8
    dp[0][1][1] = 1
    # DP
    for i in range(1, N):
        for j in range(2):
            for k in range(2):
                if j == 0:
                    dp[i][j][0] += dp[i-1][j][k]
                else:
                    dp[i][j][0] += dp[i-1][j][k]
                    dp[i][j][1] += dp[i-1][j][k]
                if k == 0:
                    dp[i][j][0] += dp[i-1][j][k]
                else:
                    dp[i][j][0] += dp[i-1][j][k]
                    dp[i][j][1] += dp[i-1][j][k]
    # 答え
    ans = dp[N-1][0][0] + dp[N-1][1][0] + dp[N-1][1][1]
    ans %= 998244353
    print(ans)

if __name__ == '__main__':
    main()