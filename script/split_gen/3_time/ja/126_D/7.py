def main():
    N = int(input())
    uvw = [[int(i) for i in input().split()] for i in range(N - 1)]
    # 隣接リスト
    adj = [[] for i in range(N + 1)]
    for u, v, w in uvw:
        adj[u].append((v, w))
        adj[v].append((u, w))
    # 頂点1からの距離を記録する配列
    dist = [-1] * (N + 1)
    dist[1] = 0
    # 頂点1からの距離を計算
    stack = [1]
    while stack:
        v = stack.pop()
        for nv, w in adj[v]:
            if dist[nv] == -1:
                dist[nv] = dist[v] + w
                stack.append(nv)
    # 頂点1からの距離が偶数なら0、奇数なら1
    for i in range(1, N + 1):
        print(dist[i] % 2)
