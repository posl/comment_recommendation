def main():
    N, Q = map(int, input().split())
    ab = [list(map(int, input().split())) for _ in range(N-1)]
    cd = [list(map(int, input().split())) for _ in range(Q)]
    # グラフの隣接リスト表現
    edge = [[] for _ in range(N)]
    for a, b in ab:
        edge[a-1].append(b-1)
        edge[b-1].append(a-1)
    # 各頂点の深さ
    depth = [-1] * N
    depth[0] = 0
    # 各頂点の親
    parent = [-1] * N
    # DFS
    stack = [0]
    while stack:
        v = stack.pop()
        for nv in edge[v]:
            if depth[nv] == -1:
                depth[nv] = depth[v] + 1
                parent[nv] = v
                stack.append(nv)
    # 1. 高橋君が青木君より先に目的地に到着する場合
    # 2. 青木君が高橋君より先に目的地に到着する場合
    # 3. 高橋君と青木君が同時に目的地に到着する場合
    # 4. 高橋君と青木君が街中で出会う場合
    # 5. 高橋君と青木君が道路上で出会う場合
    # 各頂点の深さを求める
    depth = [-1] * N
    depth[0] = 0
    stack = [0]
    while stack:
        v = stack.pop()
        for nv in edge[v]:
            if depth[nv] == -1:
                depth[nv] = depth[v] + 1
                stack.append(nv)
    # 各頂点の親を求める
    parent = [-1] * N
    stack = [0]
    while stack:

if __name__ == '__main__':
    main()