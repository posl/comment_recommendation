def main():
    N, Q = map(int, input().split())
    # 木を隣接リストで表現する
    # adj[i]: 頂点iの隣接頂点のリスト
    adj = [[] for _ in range(N)]
    for _ in range(N-1):
        a, b = map(int, input().split())
        adj[a-1].append(b-1)
        adj[b-1].append(a-1)
    # 各頂点の親を記録する
    # par[i]: 頂点iの親
    par = [-1]*N
    # 各頂点の深さを記録する
    # depth[i]: 頂点iの深さ
    depth = [0]*N
    # 根からの距離を記録する
    # dist[i]: 根から頂点iまでの距離
    dist = [0]*N
    # 各頂点の子を記録する
    # children[i]: 頂点iの子のリスト
    children = [[] for _ in range(N)]
    # 親を記録しながら幅優先探索で木を辿る
    q = [0]
    while q:
        v = q.pop(0)
        for w in adj[v]:
            if par[v] != w:
                par[w] = v
                depth[w] = depth[v] + 1
                dist[w] = dist[v] + 1
                children[v].append(w)
                q.append(w)
    # 各頂点のカウンターの値を記録する
    # counter[i]: 頂点iのカウンターの値
    counter = [0]*N
    # 各操作のあとのカウンターの値を記録する
    # counter[i]: 頂点iのカウンターの値
    ans = [0]*N
    # 各操作を処理する
    for _ in range(Q):
        p, x = map(int, input
