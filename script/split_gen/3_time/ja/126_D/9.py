def main():
    N = int(input())
    # 木の構造を保持する
    # 1-indexedで保持する
    tree = [[] for _ in range(N+1)]
    for _ in range(N-1):
        u, v, w = map(int, input().split())
        tree[u].append((v, w))
        tree[v].append((u, w))
    # 木をDFSで探索する
    # 1-indexedで保持する
    # 0: 白, 1: 黒
    color = [0] * (N+1)
    # 1-indexedで保持する
    # 0: 未探索, 1: 探索済み
    visited = [0] * (N+1)
    # 1-indexedで保持する
    # 0: 未探索, 1: 探索済み
    # 頂点1からの距離を保持する
    dist = [0] * (N+1)
    stack = [1]
    while stack:
        now = stack.pop()
        visited[now] = 1
        for next, w in tree[now]:
            if visited[next] == 1:
                continue
            stack.append(next)
            dist[next] = dist[now] + w
            color[next] = color[now] if w % 2 == 0 else 1 - color[now]
    for c in color[1:]:
        print(c)
