def main():
    N, Q = map(int, input().split())
    # 隣接リスト
    adj = [[] for _ in range(N)]
    for _ in range(N - 1):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        adj[a].append(b)
        adj[b].append(a)
    # 頂点の深さ
    depth = [-1] * N
    depth[0] = 0
    # 頂点の親
    parent = [-1] * N
    # 深さ優先探索
    stack = [0]
    while stack:
        v = stack.pop()
        for u in adj[v]:
            if depth[u] == -1:
                depth[u] = depth[v] + 1
                parent[u] = v
                stack.append(u)
    # 各クエリについて
    for _ in range(Q):
        c, d = map(int, input().split())
        c -= 1
        d -= 1
        # 同じ深さにする
        while depth[c] > depth[d]:
            c = parent[c]
        while depth[d] > depth[c]:
            d = parent[d]
        # 共通の親を探す
        while c != d:
            c = parent[c]
            d = parent[d]
        # 答えを出力
        if depth[c] % 2 == 0:
            print('Town')
        else:
            print('Road')

if __name__ == '__main__':
    main()