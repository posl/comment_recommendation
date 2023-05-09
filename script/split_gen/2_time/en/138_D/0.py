def main():
    N, Q = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(N-1)]
    queries = [list(map(int, input().split())) for _ in range(Q)]
    graph = [[] for _ in range(N)]
    for a, b in edges:
        graph[a-1].append(b-1)
        graph[b-1].append(a-1)
    # print(graph)
    # print(queries)
    # 1. 前処理
    # 1-1. 木の親子関係を構築
    # 1-2. 木の深さを構築
    # 1-3. Euler Tourを構築
    # 1-4. Euler Tourの各頂点の始点と終点を構築
    # 1-5. Euler Tourの各頂点の始点と終点を構築
    # 1-6. Euler Tourの各頂点の始点と終点を構築
    # 1-1. 木の親子関係を構築
    parent = [-1] * N
    parent[0] = 0
    stack = [0]
    while stack:
        v = stack.pop()
        for nv in graph[v]:
            if parent[nv] == -1:
                parent[nv] = v
                stack.append(nv)
    # print(parent)
    # 1-2. 木の深さを構築
    depth = [0] * N
    depth[0] = 0
    stack = [0]
    while stack:
        v = stack.pop()
        for nv in graph[v]:
            if depth[nv] == 0:
                depth[nv] = depth[v] + 1
                stack.append(nv)
    # print(depth)
    # 1-3. Euler Tourを構築
    euler = []
    stack = [0]
    while stack:
        v = stack.pop()
        euler.append(v)
        for nv in graph[v]:
            if depth
