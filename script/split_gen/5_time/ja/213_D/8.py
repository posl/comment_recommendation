def solve():
    N = int(input())
    edges = [[] for _ in range(N)]
    for _ in range(N-1):
        a, b = map(int, input().split())
        edges[a-1].append(b-1)
        edges[b-1].append(a-1)
    # 1からの距離を求める
    dist = [-1] * N
    dist[0] = 0
    stack = [0]
    while stack:
        v = stack.pop()
        for nv in edges[v]:
            if dist[nv] != -1:
                continue
            dist[nv] = dist[v] + 1
            stack.append(nv)
    # 距離が1少ない頂点から順に訪れる
    ans = [1]
    v = 0
    for _ in range(N-1):
        for nv in edges[v]:
            if dist[nv] == dist[v] - 1:
                ans.append(nv+1)
                v = nv
                break
    print(*ans)
