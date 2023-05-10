def main():
    n = int(input())
    ab = [list(map(int, input().split())) for _ in range(n-1)]
    # グラフを隣接リストで表現する
    adj = [[] for _ in range(n)]
    for a, b in ab:
        adj[a-1].append(b-1)
        adj[b-1].append(a-1)
    # 1 からスタートして、到達できる頂点を調べる
    visited = [False] * n
    visited[0] = True
    q = [0]
    while q:
        v = q.pop()
        for u in adj[v]:
            if visited[u]:
                continue
            visited[u] = True
            q.append(u)
    # 1 から到達できない頂点があれば No
    if not all(visited):
        print('No')
        return
    # 1 から到達できる頂点のうち、1 からの距離が 1 以外の頂点があれば No
    dist = [-1] * n
    dist[0] = 0
    q = [0]
    while q:
        v = q.pop()
        for u in adj[v]:
            if dist[u] != -1:
                continue
            dist[u] = dist[v] + 1
            q.append(u)
    if not all(d == 1 for d in dist[1:]):
        print('No')
        return
    print('Yes')
