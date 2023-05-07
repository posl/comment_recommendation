def main():
    N, Q = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(N - 1)]
    operations = [list(map(int, input().split())) for _ in range(Q)]
    # グラフの構築
    graph = [[] for _ in range(N)]
    for a, b in edges:
        graph[a - 1].append(b - 1)
        graph[b - 1].append(a - 1)
    # グラフの構築
    # graph = [[] for _ in range(N)]
    # for a, b in edges:
    #     graph[a - 1].append(b - 1)
    #     graph[b - 1].append(a - 1)
    # 木の根から各頂点への距離を計算
    dist = [0] * N
    stack = [0]
    while stack:
        v = stack.pop()
        for u in graph[v]:
            if dist[u] == 0:
                dist[u] = dist[v] + 1
                stack.append(u)
    # 頂点ごとの操作回数を計算
    cnt = [0] * N
    for p, x in operations:
        cnt[p - 1] += x
    # 頂点ごとの操作回数を計算
    # cnt = [0] * N
    # for p, x in operations:
    #     cnt[p - 1] += x
    # 木の根から順に操作回数を加算
    stack = [0]
    while stack:
        v = stack.pop()
        for u in graph[v]:
            if dist[u] > dist[v]:
                cnt[u] += cnt[v]
                stack.append(u)
    # 木の根から順に操作回数を加算
    # stack = [0]
    # while stack:
    #     v = stack.pop()
    #     for u in graph[v]:
    #         if dist[u] > dist[v]:
    #             cnt[u] += cnt[v]
    #             stack.append(u)
    print(*cnt)
