def main():
    N = int(input())
    X, Y = map(int, input().split())
    takoyaki = [0]
    taiyaki = [0]
    for _ in range(N):
        a, b = map(int, input().split())
        takoyaki.append(a)
        taiyaki.append(b)
    dp = [[[float("inf")] * (Y + 1) for _ in range(X + 1)] for _ in range(N + 1)]
    dp[0][0][0] = 0
    for i in range(N):
        for j in range(X + 1):
            for k in range(Y + 1):
                dp[i + 1][j][k] = min(dp[i + 1][j][k], dp[i][j][k])
                if j + takoyaki[i + 1] <= X and k + taiyaki[i + 1] <= Y:
                    dp[i + 1][j + takoyaki[i + 1]][k + taiyaki[i + 1]] = min(dp[i + 1][j + takoyaki[i + 1]][k + taiyaki[i + 1]], dp[i][j][k] + 1)
    print(dp[N][X][Y] if dp[N][X][Y] != float("inf") else -1)
