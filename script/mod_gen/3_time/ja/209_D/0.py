def main():
    n, q = map(int, input().split())
    ab = [list(map(int, input().split())) for _ in range(n - 1)]
    cd = [list(map(int, input().split())) for _ in range(q)]
    # 隣接リスト
    adj = [[] for _ in range(n)]
    for a, b in ab:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    # 深さ
    depth = [-1] * n
    depth[0] = 0
    # 幅優先探索
    que = [0]
    while que:
        v = que.pop(0)
        for nv in adj[v]:
            if depth[nv] == -1:
                depth[nv] = depth[v] + 1
                que.append(nv)
    # 二人の深さが同じならTown
    for c, d in cd:
        if depth[c - 1] == depth[d - 1]:
            print('Town')
        else:
            print('Road')

if __name__ == '__main__':
    main()