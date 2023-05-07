def main():
    N, M = map(int, input().split())
    # (i, j) に移動できる最小の操作回数
    dp = [[float("inf")] * N for _ in range(N)]
    dp[0][0] = 0
    for i in range(N):
        for j in range(N):
            # (i, j) に移動できるマスの候補
            for k in range(N):
                for l in range(N):
                    # (i, j) に移動できるか
                    if (i - k) ** 2 + (j - l) ** 2 == M:
                        dp[i][j] = min(dp[i][j], dp[k][l] + 1)
    for i in range(N):
        print(*dp[i])

if __name__ == '__main__':
    main()