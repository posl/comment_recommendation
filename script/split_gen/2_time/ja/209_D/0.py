def main():
    N, Q = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N-1)]
    CD = [list(map(int, input().split())) for _ in range(Q)]
    # 隣接リストの作成
    adj = [[] for _ in range(N+1)]
    for a, b in AB:
        adj[a].append(b)
        adj[b].append(a)
    # 頂点 1 を根とする木の構築
    parent = [0] * (N+1)
    parent[1] = -1
    stack = [1]
    while stack:
        v = stack.pop()
        for w in adj[v]:
            if parent[w] == 0:
                parent[w] = v
                stack.append(w)
    # 頂点 v から根への距離を求める
    depth = [0] * (N+1)
    for v in range(1, N+1):
        d = 0
        w = v
        while parent[w] != -1:
            d += 1
            w = parent[w]
        depth[v] = d
    # クエリの処理
    for c, d in CD:
        if depth[c] % 2 == depth[d] % 2:
            print('Town')
        else:
            print('Road')
