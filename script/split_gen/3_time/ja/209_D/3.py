def main():
    N, Q = map(int, input().split())
    ABC = [list(map(int, input().split())) for _ in range(N-1)]
    CD = [list(map(int, input().split())) for _ in range(Q)]
    # 隣接リスト
    G = [[] for _ in range(N+1)]
    for a, b in ABC:
        G[a].append(b)
        G[b].append(a)
    # 木の直径
    # 1 から最も遠い頂点を求める
    dis = [-1]*(N+1)
    dis[1] = 0
    stack = [1]
    while stack:
        v = stack.pop()
        for w in G[v]:
            if dis[w] == -1:
                dis[w] = dis[v] + 1
                stack.append(w)
    # 最も遠い頂点から最も遠い頂点までの距離を求める
    max_dis = max(dis)
    farthest = dis.index(max_dis)
    dis = [-1]*(N+1)
    dis[farthest] = 0
    stack = [farthest]
    while stack:
        v = stack.pop()
        for w in G[v]:
            if dis[w] == -1:
                dis[w] = dis[v] + 1
                stack.append(w)
    D = max(dis)
    # 木の直径の頂点を根とする二分木を作る
    # 木の直径を根とする二分木の深さは D+1 となる
    # 木の直径の頂点を根とする二分木の頂点の深さを求める
    dis = [-1]*(N+1)
    dis[farthest] = 0
    stack = [farthest]
    while stack:
        v = stack.pop()
        for w in G[v]:
            if dis[w] == -1:
                dis[w] = dis[v] + 1
                stack.append(w)
    # 木の直径の頂点を根とする二分木の各頂点の親を求める
