def main():
    N = int(input())
    # 隣接リスト
    adj_list = [[] for _ in range(N)]
    # 各辺の重み
    edge_weight = []
    # 各頂点の親
    parent = [-1] * N
    for _ in range(N - 1):
        u, v, w = map(int, input().split())
        u -= 1
        v -= 1
        adj_list[u].append((v, w))
        adj_list[v].append((u, w))
        edge_weight.append(w)
    # 各頂点の深さ
    depth = [0] * N
    # 各頂点の部分木の重みの和
    subtree_weight = [0] * N
    # 各頂点の部分木の重みの和を計算する
    def dfs(v):
        for u, w in adj_list[v]:
            if u != parent[v]:
                parent[u] = v
                depth[u] = depth[v] + 1
                dfs(u)
                subtree_weight[v] += subtree_weight[u] + w
    dfs(0)
    # 各頂点の部分木の重みの和を根に向かって伝播する
    def dfs2(v):
        for u, w in adj_list[v]:
            if u != parent[v]:
                subtree_weight[u] = subtree_weight[v] - w + (subtree_weight[0] - subtree_weight[u] - w)
                dfs2(u)
    dfs2(0)
    # 各辺の重みの和
    ans = sum(edge_weight)
    # 各頂点の部分木の重みの和の和
    ans += sum(subtree_weight)
    # 答えを出力する
    print(ans)

if __name__ == '__main__':
    main()