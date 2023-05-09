def main():
    N, Q = map(int, input().split())
    # 隣接リスト
    graph = [[] for _ in range(N)]
    for _ in range(N-1):
        a, b = map(int, input().split())
        graph[a-1].append(b-1)
        graph[b-1].append(a-1)
    # クエリ
    query = [list(map(int, input().split())) for _ in range(Q)]
    # 隣接リストを隣接行列に変換
    adj = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in graph[i]:
            adj[i][j] = 1
    # 1からの距離を求める
    dist = [0] * N
    stack = [0]
    while stack:
        i = stack.pop()
        for j in graph[i]:
            if dist[j] == 0:
                dist[j] = dist[i] + 1
                stack.append(j)
    # クエリを処理
    for c, d in query:
        if dist[c-1] % 2 == dist[d-1] % 2:
            print('Town')
        else:
            print('Road')
