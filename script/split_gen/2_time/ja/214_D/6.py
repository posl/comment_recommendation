def main():
    import sys
    sys.setrecursionlimit(10**6)
    input = sys.stdin.readline
    N = int(input())
    G = [[] for _ in range(N)]
    for _ in range(N - 1):
        u, v, w = map(int, input().split())
        G[u - 1].append((v - 1, w))
        G[v - 1].append((u - 1, w))
    from collections import deque
    depth = [-1] * N
    depth[0] = 0
    q = deque([0])
    while q:
        v = q.popleft()
        for nv, w in G[v]:
            if depth[nv] == -1:
                depth[nv] = depth[v] + 1
                q.append(nv)
    # dp[v][k] := vの2^k親の頂点
    dp = [[-1] * 20 for _ in range(N)]
    dp[0][0] = 0
    for v in range(N):
        for k in range(19):
            if dp[v][k] == -1:
                break
            dp[v][k + 1] = dp[dp[v][k]][k]
    def lca(u, v):
        if depth[u] < depth[v]:
            u, v = v, u
        for k in range(20):
            if (depth[u] - depth[v]) & (1 << k):
                u = dp[u][k]
        if u == v:
            return u
        for k in range(19, -1, -1):
            if dp[u][k] != dp[v][k]:
                u = dp[u][k]
                v = dp[v][k]
        return dp[u][0]
    def dist(u, v):
        return depth[u] + depth[v] - 2 * depth[lca(u, v)]
    ans = 0
    for v in range(N):
        for nv, w in G[v]:
            if v < nv:
                ans += w * (N - dist(v, nv))
    print(ans)
