def main():
    n = int(input())
    x, y = map(int, input().split())
    a = []
    b = []
    for i in range(n):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)
    # dp[i][j][k] := i 番目までの弁当を使って、たこ焼きを j 個以上、たい焼きを k 個以上手に入れるために必要な弁当の個数の最小値
    dp = [[[float('inf') for _ in range(y+1)] for _ in range(x+1)] for _ in range(n+1)]
    dp[0][0][0] = 0
    for i in range(n):
        for j in range(x+1):
            for k in range(y+1):
                dp[i+1][min(j+a[i], x)][min(k+b[i], y)] = min(dp[i+1][min(j+a[i], x)][min(k+b[i], y)], dp[i][j][k] + 1)
                dp[i+1][j][k] = min(dp[i+1][j][k], dp[i][j][k])
    if dp[n][x][y] == float('inf'):
        print(-1)
    else:
        print(dp[n][x][y])

if __name__ == '__main__':
    main()