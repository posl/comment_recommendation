Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    edge = [[] for _ in range(n)]
    for _ in range(n - 1):
        u, v, w = map(int, input().split())
        edge[u - 1].append((v - 1, w))
        edge[v - 1].append((u - 1, w))
    ans = 0
    for i in range(n):
        for j, w in edge[i]:
            ans += w * (n - 1) * 2
    print(ans)

=======
Suggestion 2

def main():
    N = int(input())
    edges = []
    for i in range(N - 1):
        u, v, w = map(int, input().split())
        edges.append((u - 1, v - 1, w))
    ans = 0
    for u, v, w in edges:
        ans += w * (N - 1)
    print(ans)

=======
Suggestion 3

def main():
    N = int(input())
    edges = []
    for _ in range(N - 1):
        u, v, w = map(int, input().split())
        edges.append((w, u - 1, v - 1))
    edges.sort(reverse = True)
    par = [i for i in range(N)]
    rank = [0 for _ in range(N)]
    def find(x):
        if par[x] == x:
            return x
        else:
            par[x] = find(par[x])
            return par[x]
    def unite(x, y):
        x = find(x)
        y = find(y)
        if x == y:
            return False
        if rank[x] < rank[y]:
            par[x] = y
        else:
            par[y] = x
            if rank[x] == rank[y]:
                rank[x] += 1
        return True
    def same(x, y):
        return find(x) == find(y)
    ans = 0
    for w, u, v in edges:
        ans += (w * (N - 1)) * (N - 1 - (N - 1) // 2)
        ans -= (w * (N - 1)) * (N - 1) // 2
        ans -= (w * (N - 1) * (N - 1)) // 2
        unite(u, v)
    print(ans)

=======
Suggestion 4

def main():
    N = int(input())
    E = [[] for i in range(N)]
    for i in range(N - 1):
        u, v, w = map(int, input().split())
        u -= 1
        v -= 1
        E[u].append((v, w))
        E[v].append((u, w))
    #print(E)
    #print()

    # 1. DFS to find the maximum edge in each subtree
    # 2. DFS to find the maximum edge in each path

    # 1. DFS to find the maximum edge in each subtree
    # 1.1. Initialize
    T = [0] * N
    for i in range(N):
        T[i] = [0, 0]
    # 1.2. DFS
    stack = [0]
    while stack:
        i = stack.pop()
        for j, w in E[i]:
            if T[j][0] == 0:
                T[j][0] = w
                T[j][1] = i
                stack.append(j)
    #print(T)
    #print()

    # 2. DFS to find the maximum edge in each path
    # 2.1. Initialize
    P = [0] * N
    for i in range(N):
        P[i] = [0, 0]
    # 2.2. DFS
    stack = [0]
    while stack:
        i = stack.pop()
        for j, w in E[i]:
            if P[j][0] == 0:
                P[j][0] = max(w, T[i][0])
                P[j][1] = i
                stack.append(j)
    #print(P)
    #print()

    # 3. Calculate the answer
    ans = 0
    for i in range(N):
        ans += P[i][0]
    print(ans)

=======
Suggestion 5

def main():
    n = int(input())
    e = [[] for _ in range(n)]
    for _ in range(n-1):
        u, v, w = map(int, input().split())
        e[u-1].append((v-1, w))
        e[v-1].append((u-1, w))
    def dfs(s):
        q = [s]
        d = [-1]*n
        d[s] = 0
        while q:
            u = q.pop()
            for v, w in e[u]:
                if d[v] == -1:
                    d[v] = d[u] + w
                    q.append(v)
        return d
    d1 = dfs(0)
    d2 = dfs(d1.index(max(d1)))
    print(sum(d2))

=======
Suggestion 6

def main():
    N = int(input())
    E = [tuple(map(int, input().split())) for _ in range(N - 1)]
    G = [[] for _ in range(N)]
    for u, v, w in E:
        G[u - 1].append((v - 1, w))
        G[v - 1].append((u - 1, w))

    # rootからの距離を求める
    dist = [0] * N
    dist[0] = 0
    stack = [0]
    while stack:
        u = stack.pop()
        for v, w in G[u]:
            if dist[v] == 0:
                dist[v] = dist[u] + w
                stack.append(v)

    # distの最大値と最小値を求める
    max_dist = max(dist)
    min_dist = min(dist)
    # distの最大値と最小値の差を求める
    diff = max_dist - min_dist

    # distの最大値と最小値の差を求める
    ans = diff * (N - 1) + sum(dist)
    print(ans)

=======
Suggestion 7

def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10**6)

    N = int(input())
    graph = [[] for _ in range(N)]
    for _ in range(N-1):
        u, v, w = map(int, input().split())
        graph[u-1].append((v-1, w))
        graph[v-1].append((u-1, w))

    def dfs(node, parent):
        for child, w in graph[node]:
            if child == parent:
                continue
            dfs(child, node)
            dp[node][0] += dp[child][0] + w * dp[child][1]
            dp[node][1] += dp[child][1]

    dp = [[0, 0] for _ in range(N)]
    dfs(0, -1)

    def dfs2(node, parent):
        for child, w in graph[node]:
            if child == parent:
                continue
            dp[child][0] = dp[node][0] - dp[child][0] - w * dp[child][1] + (dp[node][1] - dp[child][1]) * w
            dp[child][1] = dp[node][1] - dp[child][1]
            dfs2(child, node)

    dfs2(0, -1)

    ans = 0
    for i in range(N):
        ans += dp[i][0]
    print(ans)

=======
Suggestion 8

def find(x):
    if par[x] == x:
        return x
    else:
        par[x] = find(par[x])
        return par[x]

=======
Suggestion 9

def main():
    N = int(input())
    edges = [list(map(int, input().split())) for _ in range(N - 1)]
    print(solve(N, edges))

=======
Suggestion 10

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
