def solve(n, edges):
    # i番目の頂点に隣接する頂点のリスト
    adj = [[] for _ in range(n)]
    # 1番目の頂点からの距離
    dist = [0] * n
    # 1番目の頂点からの距離をBFSで求める
    que = [0]
    while que:
        v = que.pop()
        for u in adj[v]:
            if dist[u] == 0:
                dist[u] = dist[v] + 1
                que.append(u)
    # 頂点の距離が偶数ならば、その頂点から出る辺の色は0, 1, 2, ...と割り当てる
    # 頂点の距離が奇数ならば、その頂点から出る辺の色は1, 2, 3, ...と割り当てる
    # 割り当てられた色を出力する
    colors = [0] * (n - 1)
    for i, (v, u) in enumerate(edges):
        v -= 1
        u -= 1
        if dist[v] % 2 == 0:
            colors[i] = dist[u]
        else:
            colors[i] = dist[u] - 1
    return colors

if __name__ == '__main__':
    solve()