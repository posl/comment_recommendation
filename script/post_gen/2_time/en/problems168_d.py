Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    A = []
    B = []
    for _ in range(M):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)

    # 1からの距離を求める
    dist = [0] * (N+1)
    dist[1] = 1
    q = [1]
    while len(q) > 0:
        p = q.pop()
        for i in range(M):
            if A[i] == p and dist[B[i]] == 0:
                dist[B[i]] = dist[p] + 1
                q.append(B[i])
            if B[i] == p and dist[A[i]] == 0:
                dist[A[i]] = dist[p] + 1
                q.append(A[i])

    # 1から最も遠いところを求める
    d = 0
    for i in range(2, N+1):
        d = max(d, dist[i])

    # 1から最も遠いところの候補を求める
    cands = []
    for i in range(2, N+1):
        if dist[i] == d:
            cands.append(i)

    # 候補から選ぶ
    q = cands
    for _ in range(d-1):
        q2 = []
        for p in q:
            for i in range(M):
                if A[i] == p and dist[B[i]] == d-1:
                    q2.append(B[i])
                if B[i] == p and dist[A[i]] == d-1:
                    q2.append(A[i])
        q = q2
        d -= 1

    # 答えを求める
    ans = [''] * (N+1)
    for i in range(len(q)):
        ans[q[i]] = cands[i]

    print('Yes')
    for a in ans[2:]:
        print(a)

main()

=======
Suggestion 2

def main():
    n, m = map(int, input().split())
    g = [[] for _ in range(n)]
    for _ in range(m):
        a, b = map(int, input().split())
        g[a - 1].append(b - 1)
        g[b - 1].append(a - 1)
    ans = [-1] * n
    ans[0] = 0
    q = [0]
    while q:
        v = q.pop()
        for nv in g[v]:
            if ans[nv] == -1:
                ans[nv] = v
                q.append(nv)
    print('Yes')
    for a in ans[1:]:
        print(a + 1)

main()

=======
Suggestion 3

def main():
    N, M = map(int, input().split())
    graph = [[] for _ in range(N + 1)]
    for _ in range(M):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    # BFS
    from collections import deque
    que = deque()
    que.append(1)
    dist = [-1] * (N + 1)
    dist[1] = 0
    while que:
        p = que.popleft()
        for q in graph[p]:
            if dist[q] != -1:
                continue
            dist[q] = dist[p] + 1
            que.append(q)

    # 1 からの距離が偶数の時は 1 に向かう
    # 奇数の時は 1 に向かわない
    ans = []
    for i in range(2, N + 1):
        if dist[i] % 2 == 0:
            ans.append(1)
        else:
            ans.append(i)

    print("Yes")
    print(*ans, sep="

")

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    edges = [[] for _ in range(N)]
    for _ in range(M):
        a, b = map(int, input().split())
        edges[a - 1].append(b - 1)
        edges[b - 1].append(a - 1)
    ans = [0] * N
    ans[0] = -1
    q = [0]
    while q:
        v = q.pop()
        for u in edges[v]:
            if ans[u] == 0:
                ans[u] = v + 1
                q.append(u)
    if 0 in ans:
        print("No")
    else:
        print("Yes")
        print(*ans[1:], sep="

")

=======
Suggestion 5

def main():
    N, M = map(int, input().split())
    adj = [[] for _ in range(N)]
    for _ in range(M):
        a, b = map(int, input().split())
        adj[a-1].append(b-1)
        adj[b-1].append(a-1)
    if N == 2:
        print('Yes')
        print(1)
        return
    if any(len(adj[i]) == 1 for i in range(1, N)):
        print('No')
        return
    print('Yes')
    for i in range(1, N):
        for j in adj[i]:
            if j != 0 and len(adj[j]) > 1:
                print(j+1)
                break

=======
Suggestion 6

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
Suggestion 7

def main():
    N, M = map(int, input().split())
    rooms = [[] for i in range(N)]
    for i in range(M):
        a, b = map(int, input().split())
        rooms[a-1].append(b-1)
        rooms[b-1].append(a-1)
    visited = [False] * N
    visited[0] = True
    stack = [0]
    while stack:
        r = stack.pop()
        for i in rooms[r]:
            if not visited[i]:
                visited[i] = True
                stack.append(i)
    if not all(visited):
        print('No')
        return
    print('Yes')
    visited = [False] * N
    visited[0] = True
    stack = [0]
    while stack:
        r = stack.pop()
        for i in rooms[r]:
            if not visited[i]:
                visited[i] = True
                stack.append(i)
                print(r+1)
                break

=======
Suggestion 8

def main():
    N, M = map(int, input().split())
    ab = [list(map(int, input().split())) for _ in range(M)]
    ab = [[a - 1, b - 1] for a, b in ab]
    graph = [[] for _ in range(N)]
    for a, b in ab:
        graph[a].append(b)
        graph[b].append(a)
    dist = [-1] * N
    dist[0] = 0
    stack = [0]
    while stack:
        v = stack.pop()
        for nv in graph[v]:
            if dist[nv] == -1:
                dist[nv] = dist[v] + 1
                stack.append(nv)
    if -1 in dist[1:]:
        print("No")
        return
    ans = [-1] * N
    for i, d in enumerate(dist):
        if d == 1:
            ans[i] = 0
    stack = [0]
    while stack:
        v = stack.pop()
        for nv in graph[v]:
            if ans[nv] == -1:
                ans[nv] = v
                stack.append(nv)
    print("Yes")
    for a in ans[1:]:
        print(a + 1)

main()

=======
Suggestion 9

def main():
    N, M = map(int, input().split())
    # 1-indexed
    g = [[] for _ in range(N + 1)]
    for _ in range(M):
        a, b = map(int, input().split())
        g[a].append(b)
        g[b].append(a)
    # 1-indexed
    ans = [-1] * (N + 1)
    ans[1] = 1
    que = [1]
    while que:
        n = que.pop()
        for e in g[n]:
            if ans[e] == -1:
                ans[e] = n
                que.append(e)
    if -1 in ans[2:]:
        print('No')
    else:
        print('Yes')
        for a in ans[2:]:
            print(a)

=======
Suggestion 10

def dfs(v, p, d):
    global dist
    global parent
    global depth
    parent[v] = p
    depth[v] = d
    dist[v] = d
    for u in graph[v]:
        if u == p:
            continue
        dfs(u, v, d + 1)
        dist[v] = min(dist[v], dist[u])
