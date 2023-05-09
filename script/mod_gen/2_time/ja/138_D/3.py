def main():
    N, Q = map(int, input().split())
    # 隣接リスト
    G = [[] for _ in range(N)]
    for _ in range(N-1):
        a, b = map(int, input().split())
        G[a-1].append(b-1)
        G[b-1].append(a-1)
    # 木の根
    root = 0
    # 頂点iを根とする部分木の頂点数
    size = [0] * N
    # 頂点iの親
    parent = [0] * N
    # 頂点iの深さ
    depth = [0] * N
    # DFS
    def dfs(v, p, d):
        size[v] = 1
        parent[v] = p
        depth[v] = d
        for nv in G[v]:
            if nv == p:
                continue
            dfs(nv, v, d+1)
            size[v] += size[nv]
    dfs(root, -1, 0)
    # 頂点iの部分木に含まれる頂点のリスト
    subtree = [[] for _ in range(N)]
    for i in range(N):
        subtree[parent[i]].append(i)
    # 頂点iの部分木に含まれる頂点のリスト
    subtree = [[] for _ in range(N)]
    for i in range(N):
        subtree[parent[i]].append(i)
    # 頂点iの部分木に含まれる頂点のリスト
    subtree = [[] for _ in range(N)]
    for i in range(N):
        subtree[parent[i]].append(i)
    # カウンター
    counter = [0] * N
    # クエリ
    for _ in range(Q):
        p, x = map(int, input().split())
        counter[p-1] += x
        counter[root] -= x
        for v in subtree[p-1]:
            counter[v] += x
    # DFS
    def dfs(v, p):
        for nv in G[v]:
            if nv == p:
                continue
            counter[nv] += counter[v]
            dfs

if __name__ == '__main__':
    main()