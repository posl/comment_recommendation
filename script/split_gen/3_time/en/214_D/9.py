def main():
    import sys
    import numpy as np
    from collections import deque
    N = int(input())
    G = [[] for _ in range(N)]
    for _ in range(N-1):
        u, v, w = map(int, sys.stdin.readline().split())
        G[u-1].append([v-1, w])
        G[v-1].append([u-1, w])
    depth = [-1]*N
    depth[0] = 0
    q = deque()
    q.append(0)
    while q:
        v = q.popleft()
        for nv, w in G[v]:
            if depth[nv] != -1:
                continue
            depth[nv] = depth[v] + 1
            q.append(nv)
    dp = np.zeros((N, 20), dtype=np.int64)
    for i in range(N):
        dp[i][0] = i
    for i in range(1, 20):
        for j in range(N):
            dp[j][i] = dp[dp[j][i-1]][i-1]
    def lca(x, y):
        if depth[x] < depth[y]:
            x, y = y, x
        for i in range(19, -1, -1):
            if depth[x] - depth[y] >= 2**i:
                x = dp[x][i]
        if x == y:
            return x
        for i in range(19, -1, -1):
            if dp[x][i] != dp[y][i]:
                x = dp[x][i]
                y = dp[y][i]
        return dp[x][0]
    def dist(x, y):
        return depth[x] + depth[y] - 2*depth[lca(x, y)]
    def f(x, y):
        return depth[x] + depth[y] - 2*depth[lca(x, y)]
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            ans += f(i, j)
    print(ans)
