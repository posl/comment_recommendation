def main():
    N = int(input())
    U = []
    V = []
    W = []
    for _ in range(N - 1):
        u, v, w = map(int, input().split())
        U.append(u)
        V.append(v)
        W.append(w)
    # 頂点1を根としたときの、各頂点の親を格納する配列
    parent = [-1] * (N + 1)
    # 各頂点の深さを格納する配列
    depth = [-1] * (N + 1)
    # 各頂点の重みの総和を格納する配列
    weight = [0] * (N + 1)
    # 隣接リストを作成
    edge = [[] for _ in range(N + 1)]
    for i in range(N - 1):
        edge[U[i]].append((V[i], W[i]))
        edge[V[i]].append((U[i], W[i]))
    # 木を幅優先探索で探索
    # 1を根とする
    parent[1] = 0
    depth[1] = 0
    q = [1]
    while q:
        v = q.pop(0)
        for nv, w in edge[v]:
            if parent[nv] != -1:
                continue
            parent[nv] = v
            depth[nv] = depth[v] + 1
            weight[nv] = weight[v] + w
            q.append(nv)
    # 各頂点の重みの総和の最大値を格納する配列
    max_weight = [0] * (N + 1)
    # 重みの総和の最大値を求める
    for i in range(N, 0, -1):
        max_weight[i] = max(max_weight[i], weight[i])
        max_weight[parent[i]] = max(max_weight[parent[i]], max_weight[i])
    # 各頂点の重みの総和の最大値の差を格納する配列
    diff_weight =
