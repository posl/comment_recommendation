def main():
    N, M = map(int, input().split())
    # 都市間の距離
    dist = [[float('inf')] * N for _ in range(N)]
    for i in range(N):
        dist[i][i] = 0
    for _ in range(M):
        a, b = map(int, input().split())
        dist[a-1][b-1] = dist[b-1][a-1] = 1
    # ワーシャルフロイド法
    for k in range(N):
        for i in range(N):
            for j in range(N):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    # 経路の数
    route = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if dist[i][j] == 2:
                route[i][j] = 1
    for k in range(N):
        for i in range(N):
            for j in range(N):
                if route[i][k] > 0 and route[k][j] > 0:
                    route[i][j] += route[i][k] * route[k][j]
    print(route[0][N-1] % (10**9+7))

if __name__ == '__main__':
    main()