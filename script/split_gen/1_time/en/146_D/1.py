def main():
    N = int(input())
    G = [[] for _ in range(N)]
    for _ in range(N-1):
        a, b = map(int, input().split())
        G[a-1].append(b-1)
        G[b-1].append(a-1)
    # 木の直径を求める
    # 0番目の頂点から最も遠い頂点を求める
    def dfs(v, p):
        res = 0
        for nv in G[v]:
            if nv == p:
                continue
            res = max(res, dfs(nv, v)+1)
        return res
    v = 0
    maxd = 0
    for i in range(N):
        d = dfs(i, -1)
        if d > maxd:
            maxd = d
            v = i
    # 0番目の頂点から最も遠い頂点を求める
    def dfs(v, p):
        res = 0
        for nv in G[v]:
            if nv == p:
                continue
            res = max(res, dfs(nv, v)+1)
        return res
    maxd = dfs(v, -1)
    # 木の直径の中心から最も遠い頂点を求める
    def dfs(v, p):
        res = 0
        for nv in G[v]:
            if nv == p:
                continue
            res = max(res, dfs(nv, v)+1)
        return res
    maxd //= 2
    for _ in range(maxd):
        for i in range(N):
            if len(G[i]) == 1:
                G[G[i][0]].remove(i)
                G[i] = []
                break
    # 木の直径の中心から最も遠い頂点を求める
    def dfs(v, p):
        res = 0
        for nv in G[v]:
            if nv == p:
                continue
            res = max(res, dfs(nv, v)+1)
        return res
    maxd = dfs(v, -1)
    # 木の直径の中心から最も遠い頂点を求める
