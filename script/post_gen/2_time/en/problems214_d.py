Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    G = [[] for _ in range(N)]
    for _ in range(N - 1):
        u, v, w = map(int, input().split())
        G[u - 1].append((v - 1, w))
        G[v - 1].append((u - 1, w))

    d = [0] * N
    q = [0]
    while q:
        v = q.pop()
        for u, w in G[v]:
            if d[u] == 0:
                d[u] = d[v] + w
                q.append(u)

    print(sum(d))

=======
Suggestion 2

def main():
    import sys
    input = sys.stdin.readline

    N = int(input())
    G = [[] for _ in range(N)]
    for _ in range(N-1):
        u,v,w = map(int,input().split())
        G[u-1].append((v-1,w))
        G[v-1].append((u-1,w))

    def dfs(v,p=-1):
        for nv,w in G[v]:
            if nv==p:
                continue
            dfs(nv,v)
            G[v].append((nv,G[nv][0][1]+w))

    dfs(0)

    ans = 0
    for v in range(N):
        for nv,w in G[v]:
            ans += w
    print(ans)

=======
Suggestion 3

def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10**6)
    N = int(input())
    G = [[] for _ in range(N)]
    for _ in range(N - 1):
        u, v, w = map(int, input().split())
        G[u - 1].append((v - 1, w))
        G[v - 1].append((u - 1, w))
    def dfs(v, p):
        for u, w in G[v]:
            if u == p:
                continue
            dfs(u, v)
            s[v] += s[u] + w * s[u]
    s = [0] * N
    dfs(0, -1)
    def dfs2(v, p):
        for u, w in G[v]:
            if u == p:
                continue
            s[u] = s[v] + (N - 2 * s[u] - 1) * w
            dfs2(u, v)
    dfs2(0, -1)
    print(sum(s))

main()

=======
Suggestion 4

def main():
    n = int(input())
    edges = [list(map(int, input().split())) for _ in range(n - 1)]
    edges.sort(key=lambda x: x[2])
    parent = [i for i in range(n + 1)]
    rank = [0 for _ in range(n + 1)]
    ans = 0
    for edge in edges:
        u, v, w = edge
        if find(u, parent) != find(v, parent):
            ans += w * (size(u, parent) * size(v, parent))
            unite(u, v, parent, rank)
    print(ans)

=======
Suggestion 5

def main():
    N = int(input())
    edges = [tuple(map(int, input().split())) for _ in range(N - 1)]
    print(solve(N, edges))

=======
Suggestion 6

def main():
    N = int(input())
    edges = [list(map(int, input().split())) for _ in range(N - 1)]
    edges.sort(key=lambda x: x[2], reverse=True)
    parent = [i for i in range(N + 1)]
    rank = [0 for _ in range(N + 1)]

    def find(x):
        if parent[x] == x:
            return x
        else:
            parent[x] = find(parent[x])
            return parent[x]

    def union(x, y):
        x = find(x)
        y = find(y)
        if x == y:
            return
        if rank[x] < rank[y]:
            parent[x] = y
        else:
            parent[y] = x
            if rank[x] == rank[y]:
                rank[x] += 1

    ans = 0
    for u, v, w in edges:
        ans += w * (find(u) != find(v)) * (rank[find(u)] + rank[find(v)] + 1)
        union(u, v)
    print(ans)

=======
Suggestion 7

def main():
    import sys
    from collections import deque
    N = int(sys.stdin.readline())
    edges = [list(map(int, sys.stdin.readline().split())) for _ in range(N - 1)]
    graph = [[] for _ in range(N + 1)]
    for u, v, w in edges:
        graph[u].append((v, w))
        graph[v].append((u, w))
    #print(graph)
    q = deque([1])
    dist = [0] * (N + 1)
    visited = [False] * (N + 1)
    visited[1] = True
    while q:
        u = q.popleft()
        for v, w in graph[u]:
            if not visited[v]:
                visited[v] = True
                dist[v] = dist[u] + w
                q.append(v)
    #print(dist)
    ans = 0
    for u, v, w in edges:
        ans += w * (dist[u] + dist[v] + w)
    print(ans)

=======
Suggestion 8

def main():
    N = int(input())
    E = [list(map(int, input().split())) for _ in range(N-1)]
    E.sort(key=lambda x: x[2])
    G = [[] for _ in range(N)]
    for u, v, w in E:
        G[u-1].append(v-1)
        G[v-1].append(u-1)
    dp = [0] * N
    def dfs(x, p):
        for y in G[x]:
            if y != p:
                dp[y] = dp[x] + 1
                dfs(y, x)
    dfs(0, -1)
    ans = 0
    for i in range(N):
        ans += dp[i] * (N - dp[i] - 1)
    print(ans)

=======
Suggestion 9

def main():
    import sys
    from collections import deque
    from heapq import heappush, heappop
    input = sys.stdin.readline
    N = int(input())
    G = [[] for _ in range(N + 1)]
    for _ in range(N - 1):
        u, v, w = map(int, input().split())
        G[u].append((v, w))
        G[v].append((u, w))
    q = deque()
    q.append(1)
    visited = [False] * (N + 1)
    visited[1] = True
    parent = [0] * (N + 1)
    while q:
        v = q.popleft()
        for u, w in G[v]:
            if visited[u]:
                continue
            parent[u] = v
            visited[u] = True
            q.append(u)
    dist = [0] * (N + 1)
    for i in range(2, N + 1):
        dist[i] = dist[parent[i]] + G[parent[i]][i]
    ans = 0
    for i in range(2, N + 1):
        ans += dist[i] * (N - dist[i])
    print(ans)

=======
Suggestion 10

def main():
    import sys
    from collections import deque
    from heapq import heappush, heappop
    sys.setrecursionlimit(10**6)
    input = sys.stdin.readline

    N = int(input())
    G = [[] for _ in range(N)]
    for _ in range(N-1):
        u, v, w = map(int, input().split())
        u -= 1
        v -= 1
        G[u].append((v, w))
        G[v].append((u, w))

    # 1. 木の直径を求める
    def bfs(s):
        dist = [-1]*N
        que = deque([s])
        dist[s] = 0
        while que:
            v = que.popleft()
            for nv, w in G[v]:
                if dist[nv] != -1:
                    continue
                dist[nv] = dist[v] + w
                que.append(nv)
        return dist
    dist = bfs(0)
    max_v = max(range(N), key=lambda v: dist[v])
    dist = bfs(max_v)
    max_dist = max(dist)
    # 2. 木の直径の端点からの距離を求める
    dist = bfs(max_v)
    # 3. 木の直径の端点からの距離の和を求める
    ans = sum(dist)
    # 4. 木の直径の端点からの距離の和に、各辺の重みを足す
    for v in range(N):
        for nv, w in G[v]:
            if v > nv:
                continue
            ans += w*(dist[v] + dist[nv] - max_dist)
    print(ans)
