def main():
    N = int(input())
    MOD = 10 ** 9 + 7
    # dp[i][j][k][l]: i文字目まで見たとき、
    # 末尾3文字がj, k, lのときの文字列の個数
    dp = [[[[""] * 4 for _ in range(4)] for _ in range(4)] for _ in range(N + 1)]
    # 初期化
    for i in range(4):
        for j in range(4):
            for k in range(4):
                dp[3][i][j][k] = 1
    # 答えを求める
    for i in range(3, N):
        for j in range(4):
            for k in range(4):
                for l in range(4):
                    for m in range(4):
                        if (j == 0 and k == 2 and m == 1) or (j == 0 and k == 1 and m == 2):
                            continue
                        if (j == 0 and k == 2 and l == 1) or (j == 0 and l == 2 and m == 1):
                            continue
                        if (j == 2 and k == 0 and l == 1) or (k == 0 and l == 2 and m == 1):
                            continue
                        dp[i + 1][k][l][m] += dp[i][j][k][l]
                        dp[i + 1][k][l][m] %= MOD
    # 答えを出力
    ans = 0
    for i in range(4):
        for j in range(4):
            for k in range(4):
                ans += dp[N][i][j][k]
    print(ans % MOD)

if __name__ == '__main__':
    main()