def main():
    N, Q = map(int, input().split())
    ab = [list(map(int, input().split())) for _ in range(N - 1)]
    cd = [list(map(int, input().split())) for _ in range(Q)]
    #print(N, Q)
    #print(ab)
    #print(cd)
    #print()
    # 隣接リスト
    edges = [[] for _ in range(N + 1)]
    for a, b in ab:
        edges[a].append(b)
        edges[b].append(a)
    #print(edges)
    #print()
    # 頂点1から各頂点への距離
    dist = [-1] * (N + 1)
    dist[1] = 0
    stack = [1]
    while stack:
        v = stack.pop()
        for v2 in edges[v]:
            if dist[v2] != -1:
                continue
            dist[v2] = dist[v] + 1
            stack.append(v2)
    #print(dist)
    #print()
    for c, d in cd:
        # 高橋君と青木君の距離
        dist_cd = abs(dist[c] - dist[d])
        # 高橋君と青木君の距離が偶数なら街で出会う
        if dist_cd % 2 == 0:
            print('Town')
        # 高橋君と青木君の距離が奇数なら道路上で出会う
        else:
            print('Road')
