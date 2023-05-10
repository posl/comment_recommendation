def solve():
    N = int(input())
    x = []
    y = []
    P = []
    for _ in range(N):
        x_i, y_i, P_i = map(int, input().split())
        x.append(x_i)
        y.append(y_i)
        P.append(P_i)
    # print(N, x, y, P)
    # print()
    # ダイクストラ法
    dist = [[float('inf')] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            if P[i] * abs(x[i] - x[j]) + P[i] * abs(y[i] - y[j]) >= P[j]:
                dist[i][j] = 1
    # print(dist)
    for k in range(N):
        for i in range(N):
            for j in range(N):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    # print(dist)
    # 1つのトランポリンから全てのトランポリンに行けるか
    for i in range(N):
        for j in range(N):
            if dist[i][j] == float('inf'):
                print(-1)
                return
    # トランポリンから全てのトランポリンに行ける場合の最小の訓練回数
    ans = 0
    for i in range(N):
        for j in range(N):
            ans = max(ans, dist[i][j])
    print(ans)
