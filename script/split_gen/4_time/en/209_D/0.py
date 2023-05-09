def main():
    N, Q = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N-1)]
    CD = [list(map(int, input().split())) for _ in range(Q)]
    # 隣接リストを作成
    # 1-indexedなので、N+1
    adj = [[] for _ in range(N+1)]
    for a, b in AB:
        adj[a].append(b)
        adj[b].append(a)
    # 根からの深さを記録する
    # 1-indexedなので、N+1
    depth = [0] * (N+1)
    depth[1] = 1
    # 根を1として、深さを記録する
    # 1-indexedなので、N+1
    def dfs(u, p):
        for v in adj[u]:
            if v == p:
                continue
            depth[v] = depth[u] + 1
            dfs(v, u)
    dfs(1, -1)
    # 各クエリに対して、深さを比較して、同じならTown、異なるならRoad
    for c, d in CD:
        if (depth[c] + depth[d]) % 2 == 0:
            print("Town")
        else:
            print("Road")
