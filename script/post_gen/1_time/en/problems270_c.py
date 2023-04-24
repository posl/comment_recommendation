Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, X, Y = map(int, input().split())
    G = [[] for _ in range(N)]
    for _ in range(N-1):
        a, b = map(int, input().split())
        G[a-1].append(b-1)
        G[b-1].append(a-1)
    ans = [0] * N
    for i in range(N):
        visited = [False] * N
        queue = [i]
        dist = 0
        while queue:
            dist += 1
            next_queue = []
            for j in queue:
                visited[j] = True
                for k in G[j]:
                    if not visited[k]:
                        next_queue.append(k)
                        ans[k] += dist
            queue = next_queue
    for i in range(N):
        if i == X-1 or i == Y-1:
            continue
        print(ans[i])

main()

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
    queue = [X]
    while queue:
        v = queue.pop(0)
        for nv in graph[v]:
            if dist[nv] == -1:
                dist[nv] = dist[v] + 1
                queue.append(nv)
    for i in range(N):
        if dist[i] == -1:
            continue
        for j in range(i+1, N):
            if dist[j] == -1:
                continue
            if dist[i] + dist[j] + 1 == dist[Y]:
                print(i+1, j+1)

main()

=======
Suggestion 3

def main():
    N, X, Y = map(int, input().split())
    X -= 1
    Y -= 1
    G = [[] for _ in range(N)]
    for _ in range(N-1):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        G[a].append(b)
        G[b].append(a)
    ans = [0]*N
    for i in range(N):
        if i == X:
            continue
        elif i == Y:
            continue
        else:
            dist = [float('inf')]*N
            dist[i] = 0
            Q = [i]
            while Q:
                v = Q.pop()
                for w in G[v]:
                    if dist[w] == float('inf'):
                        dist[w] = dist[v] + 1
                        Q.append(w)
            ans[dist[X] + dist[Y] + 1] += 1
    print(' '.join(map(str, ans[1:])))

=======
Suggestion 4

def main():
    N, X, Y = map(int, input().split())
    X -= 1
    Y -= 1
    edge = [[] for _ in range(N)]
    for _ in range(N-1):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        edge[u].append(v)
        edge[v].append(u)
    dist = [-1] * N
    dist[X] = 0
    q = [X]
    while q:
        v = q.pop()
        for to in edge[v]:
            if dist[to] != -1:
                continue
            dist[to] = dist[v] + 1
            q.append(to)
    for i in range(N):
        if i == X:
            continue
        if dist[i] == -1:
            continue
        print(dist[i]//2 + 1, end=" ")
    print()

=======
Suggestion 5

def main():
    N, X, Y = map(int, input().split())
    X -= 1
    Y -= 1
    paths = [[] for _ in range(N)]
    for _ in range(N - 1):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        paths[u].append(v)
        paths[v].append(u)
    path = [None] * N
    path[X] = 0
    stack = [X]
    while stack:
        x = stack.pop()
        for y in paths[x]:
            if path[y] is None:
                path[y] = path[x] + 1
                stack.append(y)
    ans = [0] * N
    for i in range(N):
        if i != X:
            ans[path[i]] += 1
    print(' '.join(map(str, ans)))

=======
Suggestion 6

def main():
    import sys
    from collections import deque
    N, X, Y = map(int, sys.stdin.readline().split())
    X -= 1
    Y -= 1
    graph = [[] for i in range(N)]
    for i in range(N-1):
        U, V = map(int, sys.stdin.readline().split())
        U -= 1
        V -= 1
        graph[U].append(V)
        graph[V].append(U)
    #print(graph)
    #print(X, Y)
    #print(graph[X])
    #print(graph[Y])
    #print(graph)
    dist = [-1]*N
    dist[X] = 0
    q = deque([X])
    while q:
        now = q.popleft()
        for next in graph[now]:
            if dist[next] == -1:
                dist[next] = dist[now] + 1
                q.append(next)
    #print(dist)
    ans = [0]*N
    for i in range(N):
        ans[dist[i]] += 1
    ans[0] = -1
    print(*ans[1:])

=======
Suggestion 7

def main():
    N, X, Y = map(int, input().split())
    X -= 1
    Y -= 1
    if X > Y:
        X, Y = Y, X
    edges = []
    for _ in range(N-1):
        a, b = map(int, input().split())
        edges.append((a-1, b-1))
    #print(edges)
    #print(X, Y)
    #print(N, X, Y)
    #print(edges)
    #print(X, Y)
    #print(N, X, Y)
    #print(edges)
    #print(X, Y)
    #print(N, X, Y)
    #print(edges)
    #print(X, Y)
    #print(N, X, Y)
    #print(edges)
    #print(X, Y)
    #print(N, X, Y)
    #print(edges)
    #print(X, Y)
    #print(N, X, Y)
    #print(edges)
    #print(X, Y)
    #print(N, X, Y)

    #print(edges)
    #print(X, Y)
    #print(N, X, Y)
    #print(edges)
    #print(X, Y)
    #print(N, X, Y)
    #print(edges)
    #print(X, Y)
    #print(N, X, Y)
    #print(edges)
    #print(X, Y)
    #print(N, X, Y)
    #print(edges)
    #print(X, Y)
    #print(N, X, Y)
    #print(edges)
    #print(X, Y)
    #print(N, X, Y)
    #print(edges)
    #print(X, Y)
    #print(N, X, Y)
    #print(edges)
    #print(X, Y)
    #print(N, X, Y)
    #print(edges)
    #print(X, Y)
    #print(N, X, Y)
    #print(edges)
    #print(X, Y)
    #print(N, X, Y)
    #print(edges)
    #print(X, Y)
    #print(N, X, Y)
    #print(edges)
    #print(X, Y)
    #print(N, X, Y)
    #print(edges)
    #print(X, Y)
    #print(N, X, Y)

=======
Suggestion 8

def main():
    N, X, Y = map(int, input().split())
    #print(N, X, Y)
    #X -= 1
    #Y -= 1
    adj = [[] for _ in range(N)]
    for _ in range(N-1):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        adj[u].append(v)
        adj[v].append(u)
    #print(adj)
    dist = [-1] * N
    dist[X-1] = 0
    que = [X-1]
    while que:
        v = que.pop(0)
        for u in adj[v]:
            if dist[u] == -1:
                dist[u] = dist[v] + 1
                que.append(u)
    #print(dist)
    ans = [0] * N
    for i in range(N):
        if dist[i] != -1:
            ans[dist[i]] += 1
    for i in range(1, N):
        print(ans[i])

=======
Suggestion 9

def get_path(start, end, parent):
    path = [start]
    while path[-1] != end:
        path.append(parent[path[-1]])
    return path

=======
Suggestion 10

def readInts() :
    return list(map(int, input().split()))
