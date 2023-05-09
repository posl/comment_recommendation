def solve():
    n = int(input())
    x, y = map(int, input().split())
    ab = [list(map(int, input().split())) for _ in range(n)]
    # dp[i][j][k] := i番目までの弁当でたこ焼きをj個以上、たい焼きをk個以上にするために必要な弁当の最小個数
    dp = [[[float('inf')] * (y + 1) for _ in range(x + 1)] for _ in range(n + 1)]
    dp[0][0][0] = 0
    for i in range(n):
        a, b = ab[i]
        for j in range(x + 1):
            for k in range(y + 1):
                if dp[i][j][k] == float('inf'):
                    continue
                dp[i + 1][j][k] = min(dp[i + 1][j][k], dp[i][j][k])
                dp[i + 1][min(j + a, x)][min(k + b, y)] = min(dp[i + 1][min(j + a, x)][min(k + b, y)], dp[i][j][k] + 1)
    ans = dp[n][x][y]
    if ans == float('inf'):
        print(-1)
    else:
        print(ans)
solve()

if __name__ == '__main__':
    solve()