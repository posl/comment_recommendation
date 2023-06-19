def main():
    N, M = map(int, input().split())
    A = [0] * M
    B = [0] * M
    for i in range(M):
        A[i], B[i] = map(int, input().split())
    # 隣接リスト
    G = [[] for _ in range(N+1)]
    for i in range(M):
        G[A[i]].append(B[i])
        G[B[i]].append(A[i])
    # 木の直径
    def bfs(s):
        d = [-1] * (N+1)
        q = [s]
        d[s] = 0
        while q:
            v = q.pop()
            for nv in G[v]:
                if d[nv] == -1:
                    d[nv] = d[v] + 1
                    q.append(nv)
        return d
    d = bfs(1)
    # 頂点1から最も遠い頂点を求める
    farthest = 1
    for i in range(1, N+1):
        if d[i] > d[farthest]:
            farthest = i
    # 頂点farthestから最も遠い頂点を求める
    d = bfs(farthest)
    farthest = 1
    for i in range(1, N+1):
        if d[i] > d[farthest]:
            farthest = i
    # farthestから頂点1への経路を求める
    path = []
    v = farthest
    while v != 1:
        for nv in G[v]:
            if d[nv] + 1 == d[v]:
                path.append(nv)
                v = nv
                break
    # 答えを求める
    ans = [0] * (N+1)
    for i in range(len(path)-1):
        ans[path[i]] = path[i+1]
    ans[path[-1]] = 1
    print('Yes')
    for i in range(2, N+1):
        print(ans[i])
main()
