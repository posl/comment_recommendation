def main():
    N, M = map(int, input().split())
    # 隣接リスト
    adj = [[] for _ in range(N)]
    for _ in range(M):
        a, b = map(int, input().split())
        adj[a - 1].append(b - 1)
    # 頂点1からの最短経路長
    dist = [0] * N
    # 頂点1からの最短経路数
    count = [0] * N
    count[0] = 1
    # 幅優先探索
    from collections import deque
    que = deque([0])
    while que:
        v = que.popleft()
        for nv in adj[v]:
            if dist[nv] == 0:
                dist[nv] = dist[v] + 1
                que.append(nv)
            if dist[nv] == dist[v] + 1:
                count[nv] += count[v]
                count[nv] %= 10 ** 9 + 7
    print(count[N - 1])
