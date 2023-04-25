Synthesizing 10/10 solutions

=======
Suggestion 1

def find_path(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    if not graph.has_key(start):
        return None
    for node in graph[start]:
        if node not in path:
            newpath = find_path(graph, node, end, path)
            if newpath: return newpath
    return None

=======
Suggestion 2

def main():
    N, X, Y = map(int, input().split())
    X, Y = X - 1, Y - 1
    graph = [[] for _ in range(N)]
    for _ in range(N - 1):
        a, b = map(int, input().split())
        a, b = a - 1, b - 1
        graph[a].append(b)
        graph[b].append(a)
    
    ans = [0] * N
    for i in range(N):
        if i != X:
            q = [i]
            visited = [False] * N
            visited[i] = True
            while q:
                v = q.pop()
                if v == X:
                    ans[i] = len(q) + 1
                    break
                for nv in graph[v]:
                    if not visited[nv]:
                        visited[nv] = True
                        q.append(nv)
    for i in range(N):
        if i != Y:
            q = [i]
            visited = [False] * N
            visited[i] = True
            while q:
                v = q.pop()
                if v == Y:
                    ans[i] = len(q) + 1
                    break
                for nv in graph[v]:
                    if not visited[nv]:
                        visited[nv] = True
                        q.append(nv)
    for i in range(N):
        if i != X and i != Y:
            print(ans[i])

=======
Suggestion 3

def main():
    n, x, y = map(int, input().split())
    x -= 1
    y -= 1
    edges = [[] for _ in range(n)]
    for _ in range(n - 1):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        edges[u].append(v)
        edges[v].append(u)
    dist = [0] * n
    dist[x] = 0
    q = [x]
    while q:
        v = q.pop()
        for to in edges[v]:
            if dist[to] == 0:
                dist[to] = dist[v] + 1
                q.append(to)
    for i in range(n):
        if i == x or i == y:
            continue
        if dist[i] > dist[y]:
            print(i + 1, end=' ')
    print(y + 1)

=======
Suggestion 4

def main():
    N, X, Y = map(int, input().split())
    X -= 1
    Y -= 1
    graph = [[] for _ in range(N)]
    for _ in range(N - 1):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        graph[u].append(v)
        graph[v].append(u)
    ans = [0] * N
    for i in range(N):
        if i == X or i == Y:
            continue
        dist = [-1] * N
        dist[i] = 0
        que = [i]
        while que:
            v = que.pop()
            for nv in graph[v]:
                if dist[nv] != -1:
                    continue
                dist[nv] = dist[v] + 1
                que.append(nv)
        ans[dist[X] + dist[Y] + 1] += 1
    print(*ans[1:])

=======
Suggestion 5

def main():
    N, X, Y = map(int, input().split())
    X -= 1
    Y -= 1
    edges = [[] for _ in range(N)]
    for _ in range(N-1):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        edges[u].append(v)
        edges[v].append(u)
    dist = [-1] * N
    dist[X] = 0
    stack = [X]
    while stack:
        v = stack.pop()
        for nv in edges[v]:
            if dist[nv] != -1:
                continue
            dist[nv] = dist[v] + 1
            stack.append(nv)
    ans = [0] * N
    for i in range(N):
        ans[dist[i]] += 1
    print(*ans[1:])

=======
Suggestion 6

def main():
    N, X, Y = map(int, input().split())
    X -= 1
    Y -= 1
    adj = [[] for _ in range(N)]
    for _ in range(N-1):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        adj[u].append(v)
        adj[v].append(u)
    dist = [-1] * N
    dist[X] = 0
    q = [X]
    while q:
        u = q.pop(0)
        for v in adj[u]:
            if dist[v] == -1:
                dist[v] = dist[u] + 1
                q.append(v)
    ans = [0] * N
    for i in range(N):
        ans[dist[i]] += 1
    for i in range(1, N):
        print(ans[i] // 2)

=======
Suggestion 7

def main():
    N,X,Y=map(int,input().split())
    X-=1
    Y-=1
    G=[[] for _ in range(N)]
    for _ in range(N-1):
        u,v=map(int,input().split())
        u-=1
        v-=1
        G[u].append(v)
        G[v].append(u)
    d=[-1]*N
    d[X]=0
    q=[X]
    while q:
        v=q.pop()
        for w in G[v]:
            if d[w]!=-1:continue
            d[w]=d[v]+1
            q.append(w)
    for i in range(N):
        if i==X:continue
        if d[i]==d[Y]//2:
            print(i+1)
            return
    print(Y+1)
main()

=======
Suggestion 8

def main():
    N, X, Y = map(int, input().split())
    X -= 1
    Y -= 1
    edges = [list(map(int, input().split())) for _ in range(N-1)]
    graph = [[] for _ in range(N)]
    for u, v in edges:
        u -= 1
        v -= 1
        graph[u].append(v)
        graph[v].append(u)
    dist = [-1]*N
    dist[X] = 0
    stack = [X]
    while stack:
        v = stack.pop()
        for w in graph[v]:
            if dist[w] == -1:
                dist[w] = dist[v]+1
                stack.append(w)
    ans = [0]*N
    for i in range(N):
        if i == X or i == Y:
            continue
        if dist[i] == -1:
            continue
        ans[dist[i]] += 1
    for i in range(1, N):
        if ans[i] > 0:
            print(i, ans[i])

main()

=======
Suggestion 9

def main():
    n, x, y = map(int, input().split())
    x -= 1
    y -= 1
    #print(n, x, y)
    graph = [[] for _ in range(n)]
    for _ in range(n-1):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        graph[u].append(v)
        graph[v].append(u)
    #print(graph)
    dist = [0]*n
    dist[x] = 0
    queue = [x]
    while queue:
        v = queue.pop(0)
        for u in graph[v]:
            if dist[u] != 0:
                continue
            dist[u] = dist[v] + 1
            queue.append(u)
    #print(dist)
    ans = [0]*n
    for i in range(n):
        ans[dist[i]] += 1
    for i in range(1, n):
        print(ans[i])

=======
Suggestion 10

def main():
  # Input
  N,X,Y = map(int, input().split())
  # 全ての頂点についての隣接リスト
  adj = [[] for _ in range(N)]
  for _ in range(N-1):
    u,v = map(int, input().split())
    adj[u-1].append(v-1)
    adj[v-1].append(u-1)
  # BFS
  dist = [-1] * N
  dist[X-1] = 0
  q = [X-1]
  while q:
    v = q.pop()
    for w in adj[v]:
      if dist[w] == -1:
        dist[w] = dist[v] + 1
        q.append(w)
  # Output
  for i in range(N):
    if i != X-1:
      print(dist[i])
