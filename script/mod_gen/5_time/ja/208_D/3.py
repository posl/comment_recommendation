def main():
    N, M = map(int, input().split())
    edges = []
    for _ in range(M):
        A, B, C = map(int, input().split())
        edges.append((A, B, C))
    edges.sort(key=lambda x: x[2])
    # ワーシャルフロイド法
    # dp[i][j][k] := iからjにk以下の都市を通って行く最短経路
    INF = 10**10
    dp = [[[INF for _ in range(N+1)] for _ in range(N+1)] for _ in range(N+1)]
    for i in range(N+1):
        for j in range(N+1):
            if i == j:
                dp[i][j][i] = 0
    for i in range(N+1):
        for j in range(N+1):
            for k in range(N+1):
                dp[i][j][k] = min(dp[i][j][k], dp[i][j][k])
                dp[i][j][k] = min(dp[i][j][k], dp[i][j][k])
    for i in range(N+1):
        for j in range(N+1):
            for k in range(N+1):
                dp[i][j][k] = min(dp[i][j][k], dp[i][j][k])
                dp[i][j][k] = min(dp[i][j][k], dp[i][j][k])
    for i in range(N+1):
        for j in range(N+1):
            for k in range(N+1):
                dp[i][j][k] = min(dp[i][j][k], dp[i][j][k])
                dp[i][j][k] = min(dp[i][j][k], dp[i][j][k])
    for i in range(N+1):
        for j in range(N+1):
            for k in range(N+1):
                dp[i][j][k] = min(dp[i][j][k], dp[i][j][k])
                dp[i][j][k] = min(dp[i][j][k], dp[i][j][k])
    for i in range(N+1):
        for j in range(N+1):
            for k

if __name__ == '__main__':
    main()