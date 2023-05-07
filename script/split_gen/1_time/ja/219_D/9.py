def main():
    N = int(input())
    X, Y = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]
    # dp[i][a][b] := i番目までの弁当を買って、たこ焼きa個、たい焼きb個を手に入れるために必要な最小の弁当の個数
    # 1 <= i <= N, 0 <= a <= X, 0 <= b <= Y
    dp = [[[float('inf')] * (Y + 1) for _ in range(X + 1)] for _ in range(N + 1)]
    dp[0][0][0] = 0
    for i in range(N):
        for a in range(X + 1):
            for b in range(Y + 1):
                # i番目の弁当を買わない場合
                dp[i + 1][a][b] = min(dp[i + 1][a][b], dp[i][a][b])
                # i番目の弁当を買う場合
                if a + AB[i][0] <= X and b + AB[i][1] <= Y:
                    dp[i + 1][a + AB[i][0]][b + AB[i][1]] = min(dp[i + 1][a + AB[i][0]][b + AB[i][1]], dp[i][a][b] + 1)
    ans = dp[N][X][Y]
    if ans == float('inf'):
        ans = -1
    print(ans)
