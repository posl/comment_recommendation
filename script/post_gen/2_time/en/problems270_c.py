Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, X, Y = map(int, input().split())
    X -= 1
    Y -= 1
    G = [[] for _ in range(N)]
    for _ in range(N-1):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        G[u].append(v)
        G[v].append(u)
    print(*dfs(X, Y, G))

=======
Suggestion 2

def main():
    N, X, Y = map(int, input().split())
    X -= 1
    Y -= 1
    graph = [[] for _ in range(N)]
    for _ in range(N-1):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        graph[u].append(v)
        graph[v].append(u)
    dist = [-1] * N
    dist[X] = 0
    stack = [X]
    while stack:
        v = stack.pop()
        for w in graph[v]:
            if dist[w] != -1:
                continue
            dist[w] = dist[v] + 1
            stack.append(w)
    print(*dist)

=======
Suggestion 3

def main():
    N, X, Y = map(int, input().split())
    X -= 1
    Y -= 1
    edges = [[] for _ in range(N)]
    for _ in range(N - 1):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        edges[u].append(v)
        edges[v].append(u)
    dist = [-1] * N
    dist[X] = 0
    q = [X]
    while q:
        v = q.pop()
        for nv in edges[v]:
            if dist[nv] != -1:
                continue
            dist[nv] = dist[v] + 1
            q.append(nv)
    ans = [0] * N
    for i in range(N):
        if i == X:
            continue
        ans[dist[i]] += 1
    for i in range(1, N):
        print(ans[i])

=======
Suggestion 4

def main():
    N, X, Y = map(int, input().split())
    X -= 1
    Y -= 1
    edges = [[] for _ in range(N)]
    for _ in range(N - 1):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        edges[u].append(v)
        edges[v].append(u)

    # BFS
    visited = [False] * N
    visited[X] = True
    queue = [(X, 0)]
    while queue:
        v, d = queue.pop(0)
        if v == Y:
            print(d // 2)
            return
        for nv in edges[v]:
            if not visited[nv]:
                visited[nv] = True
                queue.append((nv, d + 1))

main()

=======
Suggestion 5

def main():
    N, X, Y = map(int, input().split())
    X -= 1
    Y -= 1
    edges = [list(map(int, input().split())) for _ in range(N - 1)]
    path = [[] for _ in range(N)]
    for u, v in edges:
        u -= 1
        v -= 1
        path[u].append(v)
        path[v].append(u)
    ans = [0] * N
    for i in range(N):
        if i == X or i == Y:
            continue
        d = [0] * N
        q = [i]
        while q:
            x = q.pop()
            for y in path[x]:
                if d[y] == 0:
                    d[y] = d[x] + 1
                    q.append(y)
        ans[d[Y]] += 1
    for i in range(1, N):
        print(ans[i])

=======
Suggestion 6

def main():
    N, X, Y = map(int, input().split())
    X -= 1
    Y -= 1
    G = [[] for _ in range(N)]
    for i in range(N - 1):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        G[u].append(v)
        G[v].append(u)
    ans = [0] * N
    for i in range(N):
        if i == X:
            continue
        d = [0] * N
        q = [i]
        while q:
            v = q.pop()
            for nv in G[v]:
                if d[nv] == 0:
                    d[nv] = d[v] + 1
                    q.append(nv)
        if d[Y] != 0:
            ans[d[Y]] += 1
    for i in range(1, N):
        if ans[i] == 0:
            break
        print(ans[i])

=======
Suggestion 7

def main():
    N, X, Y = map(int, input().split())
    X -= 1
    Y -= 1
    edge = [[] for i in range(N)]
    for i in range(N-1):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        edge[u].append(v)
        edge[v].append(u)
    dist = [-1] * N
    dist[X] = 0
    que = [X]
    while que:
        v = que.pop()
        for u in edge[v]:
            if dist[u] != -1:
                continue
            dist[u] = dist[v] + 1
            que.append(u)
    ans = [0] * N
    for i in range(N):
        if i == X:
            continue
        ans[dist[i]] += 1
    for i in range(1, N):
        if ans[i] == 0:
            continue
        print(ans[i])

=======
Suggestion 8

def main():
    N, X, Y = map(int, input().split())
    X -= 1
    Y -= 1
    edges = [[] for _ in range(N)]
    for _ in range(N - 1):
        U, V = map(int, input().split())
        U -= 1
        V -= 1
        edges[U].append(V)
        edges[V].append(U)
    dist = [-1] * N
    dist[X] = 0
    queue = [X]
    while queue:
        v = queue.pop(0)
        for u in edges[v]:
            if dist[u] == -1:
                dist[u] = dist[v] + 1
                queue.append(u)
    ans = [0] * N
    for i in range(N):
        if i == X or i == Y:
            continue
        ans[dist[i]] += 1
    for i in range(1, N):
        if ans[i] == 0:
            continue
        print(i, ans[i])

=======
Suggestion 9

def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10**6)
    N, X, Y = map(int, input().split())
    X, Y = X-1, Y-1
    graph = [[] for _ in range(N)]
    for _ in range(N-1):
        a, b = map(int, input().split())
        a, b = a-1, b-1
        graph[a].append(b)
        graph[b].append(a)
    dist = [-1]*N
    dist[X] = 0
    def dfs(v):
        for u in graph[v]:
            if dist[u] == -1:
                dist[u] = dist[v] + 1
                dfs(u)
    dfs(X)
    for i in range(N):
        if i == X:
            continue
        print(dist[i])

=======
Suggestion 10

def main():
    N, X, Y = map(int, input().split())
    #print(N, X, Y)
    X -= 1
    Y -= 1
    #print(X, Y)
    edges = []
    for i in range(N-1):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        edges.append((u, v))
    #print(edges)
    #print(edges)
    dist = [[-1 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        dist[i][i] = 0
    for u, v in edges:
        dist[u][v] = 1
        dist[v][u] = 1
    #print(dist)
    for i in range(N):
        for j in range(N):
            for k in range(N):
                if dist[j][i] != -1 and dist[i][k] != -1:
                    if dist[j][k] == -1 or dist[j][k] > dist[j][i] + dist[i][k]:
                        dist[j][k] = dist[j][i] + dist[i][k]
    #print(dist)
    ans = [0] * N
    for i in range(N):
        for j in range(N):
            if dist[i][j] == -1:
                continue
            ans[dist[i][j]] += 1
    for i in range(1, N):
        print(ans[i]//2)
