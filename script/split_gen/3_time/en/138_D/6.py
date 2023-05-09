def main():
    N, Q = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(N - 1)]
    queries = [list(map(int, input().split())) for _ in range(Q)]
    # 木を構成する
    tree = [[] for _ in range(N + 1)]
    for a, b in edges:
        tree[a].append(b)
        tree[b].append(a)
    # 頂点ごとの親を取得する
    parent = [0 for _ in range(N + 1)]
    stack = [1]
    while stack:
        v = stack.pop()
        for w in tree[v]:
            if w == parent[v]:
                continue
            parent[w] = v
            stack.append(w)
    # クエリに対応する頂点を取得する
    query_vertex = [[] for _ in range(N + 1)]
    for p, x in queries:
        query_vertex[p].append(x)
    # クエリに対応する頂点の値を取得する
    value = [0 for _ in range(N + 1)]
    stack = [1]
    while stack:
        v = stack.pop()
        for w in tree[v]:
            if w == parent[v]:
                continue
            stack.append(w)
        for x in query_vertex[v]:
            value[v] += x
    # 頂点ごとの値を取得する
    stack = [1]
    while stack:
        v = stack.pop()
        for w in tree[v]:
            if w == parent[v]:
                continue
            value[w] += value[v]
            stack.append(w)
    # 答えを出力する
    print(*value[1:])
