def main():
    N = int(input())
    edges = []
    for _ in range(N - 1):
        u, v, w = map(int, input().split())
        edges.append((u, v, w))
    # 隣接リストを作成
    adj = [[] for _ in range(N + 1)]
    for u, v, w in edges:
        adj[u].append((v, w))
        adj[v].append((u, w))
    # BFSで各頂点の色を決める
    color = [None] * (N + 1)
    color[1] = 0
    q = [1]
    while q:
        u = q.pop()
        for v, w in adj[u]:
            if color[v] is None:
                color[v] = color[u] ^ (w % 2)
                q.append(v)
    # 答えを出力
    for i in range(1, N + 1):
        print(color[i])
