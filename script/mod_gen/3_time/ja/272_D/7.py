def main():
    N, M = map(int, input().split())
    # (i, j) に移動するために必要な操作回数を dp[i][j] に格納
    dp = [[-1] * N for _ in range(N)]
    # (1, 1) に駒があるので、dp[0][0] = 0
    dp[0][0] = 0
    # (1, 1) から (i, j) に移動するには、
    # (1, 1) から (x, y) に移動する必要がある
    # (x, y) から (i, j) に移動する必要がある
    # ということになる
    # このとき、(i, j) と (x, y) の距離は
    # ((i - x) ** 2 + (j - y) ** 2) ** 0.5
    # となる
    # この値を M で割った余りが 0 になるような (x, y) を全て探す
    # このとき、(x, y) から (i, j) に移動するために必要な操作回数は
    # dp[x][y] + 1
    # となる
    for i in range(N):
        for j in range(N):
            for x in range(N):
                for y in range(N):
                    if ((i - x) ** 2 + (j - y) ** 2) % M == 0:
                        if dp[x][y] != -1:
                            if dp[i][j] == -1:
                                dp[i][j] = dp[x][y] + 1
                            else:
                                dp[i][j] = min(dp[i][j], dp[x][y] + 1)
    for i in range(N):
        print(*dp[i])

if __name__ == '__main__':
    main()