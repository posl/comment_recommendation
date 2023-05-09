def main():
    N,Q = map(int,input().split())
    # 隣接リスト
    adj = [[] for _ in range(N)]
    for _ in range(N-1):
        a,b = map(int,input().split())
        adj[a-1].append(b-1)
        adj[b-1].append(a-1)
    # 各頂点の深さ
    depth = [-1]*N
    # 各頂点の親
    parent = [-1]*N
    # 各頂点の子
    children = [[] for _ in range(N)]
    # 0 を親とする木を作成
    depth[0] = 0
    parent[0] = 0
    stack = [0]
    while stack:
        v = stack.pop()
        for u in adj[v]:
            if depth[u] != -1:
                continue
            depth[u] = depth[v] + 1
            parent[u] = v
            children[v].append(u)
            stack.append(u)
    # 各頂点の部分木のサイズ
    size = [0]*N
    for v in reversed(range(N)):
        size[v] = 1
        for u in children[v]:
            size[v] += size[u]
    # 各頂点の部分木の根
    root = [0]*N
    for v in range(N):
        if v == 0 or len(children[parent[v]]) == 1:
            root[v] = v
        else:
            root[v] = root[parent[v]]
    # 各頂点の部分木の先頭
    head = [0]*N
    for v in range(N):
        if v == 0 or len(children[parent[v]]) == 1:
            head[v] = v
        else:
            head[v] = head[parent[v]]
    # 各頂点の部分木の先頭の深さ
    head_depth = [0]*N
    for v in range(N):
        if v == 0 or len(children[parent[v]]) == 1:
            head_depth[v] = depth[v]
        else:
            head_depth[v] = head_depth[parent[v]]
    # 各頂点の部分

if __name__ == '__main__':
    main()