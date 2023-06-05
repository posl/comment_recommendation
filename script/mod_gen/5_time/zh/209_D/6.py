def main():
    n, q = map(int, input().split())
    ab = [list(map(int, input().split())) for _ in range(n-1)]
    cd = [list(map(int, input().split())) for _ in range(q)]
    # 木構造を作る
    tree = [[] for _ in range(n+1)]
    for a, b in ab:
        tree[a].append(b)
        tree[b].append(a)
    # 木の根を求める
    root = 1
    for i in range(1, n+1):
        if len(tree[i]) == 1:
            root = i
            break
    # 木の深さを求める
    depth = [0] * (n+1)
    def dfs(u, p):
        for v in tree[u]:
            if v != p:
                depth[v] = depth[u] + 1
                dfs(v, u)
    dfs(root, -1)
    # 各クエリについて、高橋と青木の位置関係を調べる
    for c, d in cd:
        # 木の深さが同じなら Town
        if depth[c] == depth[d]:
            print('Town')
        # 違うなら Road
        else:
            print('Road')

if __name__ == '__main__':
    main()