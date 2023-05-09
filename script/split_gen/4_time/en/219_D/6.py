def main():
    n = int(input())
    x, y = map(int, input().split())
    a = []
    b = []
    for i in range(n):
        a_i, b_i = map(int, input().split())
        a.append(a_i)
        b.append(b_i)
    # dp[i][j][k] = (i番目までの弁当で、j個以上のたこ焼きを、k個以上のたい焼きを作るための弁当の最小個数)
    dp = [[[float('inf') for _ in range(y+1)] for _ in range(x+1)] for _ in range(n+1)]
    dp[0][0][0] = 0
    for i in range(n):
        for j in range(x+1):
            for k in range(y+1):
                if dp[i][j][k] == float('inf'):
                    continue
                dp[i+1][j][k] = min(dp[i+1][j][k], dp[i][j][k])
                dp[i+1][min(x, j+a[i])][min(y, k+b[i])] = min(dp[i+1][min(x, j+a[i])][min(y, k+b[i])], dp[i][j][k] + 1)
    if dp[n][x][y] == float('inf'):
        print(-1)
    else:
        print(dp[n][x][y])
