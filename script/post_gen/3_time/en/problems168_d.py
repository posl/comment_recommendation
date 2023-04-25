Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    A = [0] * M
    B = [0] * M
    for i in range(M):
        A[i], B[i] = map(int, input().split())
    # 1から各頂点への最短距離を求める
    dist = [float('inf')] * N
    dist[0] = 0
    for i in range(M):
        if A[i] == 1:
            dist[B[i]-1] = 1
        elif B[i] == 1:
            dist[A[i]-1] = 1
    # 1から各頂点への最短経路の次の頂点を求める
    next = [-1] * N
    for i in range(M):
        if dist[A[i]-1] == dist[B[i]-1] - 1:
            next[B[i]-1] = A[i]
        elif dist[B[i]-1] == dist[A[i]-1] - 1:
            next[A[i]-1] = B[i]
    # 1から各頂点への最短経路を求める
    path = [-1] * N
    path[0] = 1
    for i in range(1, N):
        if path[i] == -1:
            path[i] = next[i]
            while path[i] != 1:
                path[i] = next[path[i]-1]
    # 出力
    print('Yes')
    for i in range(1, N):
        print(path[i])

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    A = []
    B = []
    for i in range(M):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)

    # 始点となる1以外の部屋について、
    # 1にたどり着くために必要な最短経路をBFSで求める
    # その際の各部屋の親を記録しておく
    # そして、親の部屋番号を出力すればよい
    from collections import deque
    adj = [[] for _ in range(N+1)]
    for i in range(M):
        adj[A[i]].append(B[i])
        adj[B[i]].append(A[i])
    q = deque()
    q.append(1)
    parent = [-1] * (N+1)
    parent[1] = 0
    while q:
        v = q.popleft()
        for nv in adj[v]:
            if parent[nv] == -1:
                parent[nv] = v
                q.append(nv)
    if -1 in parent[2:]:
        print("No")
    else:
        print("Yes")
        for i in range(2, N+1):
            print(parent[i])

=======
Suggestion 3

def main():
    N, M = map(int, input().split())
    G = [[] for _ in range(N)]
    for _ in range(M):
        a, b = map(int, input().split())
        G[a - 1].append(b - 1)
        G[b - 1].append(a - 1)
    ans = [-1] * N
    ans[0] = 0
    que = [0]
    while que:
        v = que.pop()
        for u in G[v]:
            if ans[u] == -1:
                ans[u] = v
                que.append(u)
    if -1 in ans[1:]:
        print('No')
    else:
        print('Yes')
        for i in ans[1:]:
            print(i + 1)

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    graph = [[] for _ in range(N)]
    for _ in range(M):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        graph[a].append(b)
        graph[b].append(a)
    ans = [-1] * N
    ans[0] = 0
    stack = [(0, 0)]
    while stack:
        v, par = stack.pop()
        for nv in graph[v]:
            if ans[nv] != -1:
                continue
            ans[nv] = v
            stack.append((nv, v))
    if -1 in ans[1:]:
        print('No')
    else:
        print('Yes')
        for a in ans[1:]:
            print(a + 1)

=======
Suggestion 5

def main():
    N, M = map(int, input().split())
    G = [[] for i in range(N)]
    for i in range(M):
        A, B = map(int, input().split())
        G[A-1].append(B-1)
        G[B-1].append(A-1)
    ans = [-1]*N
    ans[0] = 0
    q = [0]
    while q:
        v = q.pop()
        for i in G[v]:
            if ans[i] == -1:
                ans[i] = v
                q.append(i)
    print("Yes")
    for i in range(1, N):
        print(ans[i]+1)
main()

=======
Suggestion 6

def solve():
    N, M = map(int, input().split())
    edge = [[] for _ in range(N)]
    for _ in range(M):
        a, b = map(int, input().split())
        edge[a-1].append(b-1)
        edge[b-1].append(a-1)
    sign = [0]*N
    sign[0] = -1
    que = [0]
    while que:
        v = que.pop()
        for w in edge[v]:
            if sign[w] == 0:
                que.append(w)
                sign[w] = v+1
    if 0 in sign[1:]:
        print("No")
    else:
        print("Yes")
        for s in sign[1:]:
            print(s)

solve()

=======
Suggestion 7

def solve():
    N, M = [int(x) for x in input().split()]
    A = []
    B = []
    for i in range(M):
        a, b = [int(x) for x in input().split()]
        A.append(a)
        B.append(b)
    # 0-indexed
    A = [a - 1 for a in A]
    B = [b - 1 for b in B]
    # 0-indexed
    graph = [[] for i in range(N)]
    for i in range(M):
        graph[A[i]].append(B[i])
        graph[B[i]].append(A[i])
    # 0-indexed
    visited = [False] * N
    # 0-indexed
    parent = [-1] * N
    # 0-indexed
    depth = [-1] * N
    # 0-indexed
    queue = [0]
    visited[0] = True
    depth[0] = 0
    while queue:
        q = queue.pop()
        for n in graph[q]:
            if not visited[n]:
                visited[n] = True
                parent[n] = q
                depth[n] = depth[q] + 1
                queue.append(n)
    # 0-indexed
    signpost = [-1] * N
    for i in range(N):
        if i == 0:
            continue
        signpost[i] = parent[i]
    print("Yes")
    for i in range(N):
        if i == 0:
            continue
        print(signpost[i] + 1)

solve()

=======
Suggestion 8

def main():
    from collections import deque
    N, M = map(int, input().split())
    adj = [[] for _ in range(N)]
    for _ in range(M):
        a, b = map(int, input().split())
        adj[a-1].append(b-1)
        adj[b-1].append(a-1)
    d = [-1]*N
    d[0] = 0
    q = deque([0])
    while q:
        v = q.popleft()
        for u in adj[v]:
            if d[u] != -1:
                continue
            d[u] = v
            q.append(u)
    if -1 in d[1:]:
        print('No')
    else:
        print('Yes')
        for i in d[1:]:
            print(i+1)

=======
Suggestion 9

def dfs ( v , p , d , edges , ans ): for e in edges [ v ]: if e [ 0 ] == p : continue ans [ e [ 0 ]] = v dfs ( e [ 0 ], v , d + 1 , edges , ans )

=======
Suggestion 10

def read_int():
    return int(input())
