Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, Q = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(N-1)]
    queries = [list(map(int, input().split())) for _ in range(Q)]
    graph = [[] for _ in range(N)]
    for a, b in edges:
        graph[a-1].append(b-1)
        graph[b-1].append(a-1)
    # print(graph)
    # print(queries)

    # 1. 前処理
    # 1-1. 木の親子関係を構築
    # 1-2. 木の深さを構築
    # 1-3. Euler Tourを構築
    # 1-4. Euler Tourの各頂点の始点と終点を構築
    # 1-5. Euler Tourの各頂点の始点と終点を構築
    # 1-6. Euler Tourの各頂点の始点と終点を構築

    # 1-1. 木の親子関係を構築
    parent = [-1] * N
    parent[0] = 0
    stack = [0]
    while stack:
        v = stack.pop()
        for nv in graph[v]:
            if parent[nv] == -1:
                parent[nv] = v
                stack.append(nv)
    # print(parent)

    # 1-2. 木の深さを構築
    depth = [0] * N
    depth[0] = 0
    stack = [0]
    while stack:
        v = stack.pop()
        for nv in graph[v]:
            if depth[nv] == 0:
                depth[nv] = depth[v] + 1
                stack.append(nv)
    # print(depth)

    # 1-3. Euler Tourを構築
    euler = []
    stack = [0]
    while stack:
        v = stack.pop()
        euler.append(v)
        for nv in graph[v]:
            if depth

=======
Suggestion 2

def main():
    N, Q = map(int, input().split())
    edges = [[] for i in range(N)]
    for i in range(N - 1):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        edges[a].append(b)
        edges[b].append(a)
    children = [[] for i in range(N)]
    parent = [-1 for i in range(N)]
    parent[0] = 0
    stack = [0]
    while stack:
        v = stack.pop()
        for u in edges[v]:
            if parent[u] == -1:
                parent[u] = v
                children[v].append(u)
                stack.append(u)
    counter = [0 for i in range(N)]
    for i in range(Q):
        p, x = map(int, input().split())
        p -= 1
        counter[p] += x
    stack = [0]
    while stack:
        v = stack.pop()
        for u in children[v]:
            counter[u] += counter[v]
            stack.append(u)
    print(*counter)

=======
Suggestion 3

def main():
    N, Q = list(map(int, input().split()))
    edges = []
    for i in range(N-1):
        edges.append(list(map(int, input().split())))
    ops = []
    for i in range(Q):
        ops.append(list(map(int, input().split())))

    #print(edges)
    #print(ops)

    #build tree
    tree = {}
    for i in range(N):
        tree[i+1] = []
    for e in edges:
        tree[e[0]].append(e[1])
        tree[e[1]].append(e[0])
    #print(tree)

    #dfs
    visited = [False] * (N+1)
    stack = [1]
    visited[1] = True
    order = []
    while len(stack) > 0:
        v = stack.pop()
        order.append(v)
        for c in tree[v]:
            if not visited[c]:
                visited[c] = True
                stack.append(c)
    #print(order)

    #calculate range of subtree
    ranges = {}
    for i in range(N):
        ranges[order[i]] = [i, i]
    for i in range(N-1, -1, -1):
        v = order[i]
        for c in tree[v]:
            if ranges[v][0] > ranges[c][0]:
                ranges[v][0] = ranges[c][0]
            if ranges[v][1] < ranges[c][1]:
                ranges[v][1] = ranges[c][1]
    #print(ranges)

    #calculate result
    result = [0] * N
    for op in ops:
        p = op[0]
        x = op[1]
        result[ranges[p][0]] += x
        if ranges[p][1] < N-1:
            result[ranges[p][1]+1] -= x
    #print(result)

    #print result
    for i in range(1, N):
        result[i] += result[i-1]
    print(' '.join(list(map(str, result))))

=======
Suggestion 4

def main():
    N, Q = map(int, input().split())
    #print(N, Q)
    graph = [[] for _ in range(N)]
    for _ in range(N-1):
        a, b = map(int, input().split())
        graph[a-1].append(b-1)
        graph[b-1].append(a-1)
    #print(graph)
    #print("

")
    q = []
    for _ in range(Q):
        p, x = map(int, input().split())
        q.append((p-1, x))
    #print(q

=======
Suggestion 5

def main():
    n, q = map(int, input().split())
    # 1-indexed
    g = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        a, b = map(int, input().split())
        g[a].append(b)
        g[b].append(a)
    # 1-indexed
    p = [0] * (n + 1)
    x = [0] * (n + 1)
    for _ in range(q):
        p_, x_ = map(int, input().split())
        p[p_] += x_
        x[p_] += x_
    ans = [0] * (n + 1)
    stack = [1]
    while stack:
        v = stack.pop()
        for w in g[v]:
            if ans[w] == 0:
                ans[w] = ans[v] + x[w]
                stack.append(w)
    print(*ans[1:])

=======
Suggestion 6

def main():
    N, Q = map(int, input().split())
    #N, Q = 6, 2
    #a = [1, 1, 2, 3]
    #b = [2, 3, 4, 6]
    #p = [1, 1]
    #x = [10, 10]
    a = []
    b = []
    for i in range(N-1):
        a_i, b_i = map(int, input().split())
        #a_i, b_i = a[i], b[i]
        a.append(a_i)
        b.append(b_i)
    p = []
    x = []
    for i in range(Q):
        p_i, x_i = map(int, input().split())
        #p_i, x_i = p[i], x[i]
        p.append(p_i)
        x.append(x_i)
    #print(a)
    #print(b)
    #print(p)
    #print(x)
    graph = [[] for i in range(N)]
    for i in range(N-1):
        graph[a[i]-1].append(b[i]-1)
        graph[b[i]-1].append(a[i]-1)
    #print(graph)
    #print('-----')
    from collections import deque
    queue = deque()
    queue.append(0)
    visited = [False for i in range(N)]
    visited[0] = True
    parent = [-1 for i in range(N)]
    while len(queue) > 0:
        q = queue.popleft()
        for i in graph[q]:
            if not visited[i]:
                visited[i] = True
                parent[i] = q
                queue.append(i)
    #print(parent)
    #print('-----')
    count = [0 for i in range(N)]
    for i in range(Q):
        count[p[i]-1] += x[i]
    #print(count)
    #print('-----')
    queue = deque()
    queue.append(0)
    visited = [False for i in range(N)]
    visited[0] = True
    while len(queue) > 0:
        q = queue.popleft()
        for i in graph[q]:
            if not visited[i]:
                visited[i] = True
                count[i] += count[q]
                queue.append(i)
    #print(count)
    #print('

=======
Suggestion 7

def main():
    import sys
    from collections import deque
    input = sys.stdin.readline
    sys.setrecursionlimit(10**8)
    N,Q = map(int,input().split())
    G = [[] for _ in range(N)]
    for _ in range(N-1):
        a,b = map(int,input().split())
        G[a-1].append(b-1)
        G[b-1].append(a-1)
    P = [0]*N
    D = [0]*N
    Q = deque([0])
    while Q:
        v = Q.popleft()
        for u in G[v]:
            if D[u] == 0:
                D[u] = D[v] + 1
                P[u] = v
                Q.append(u)
    A = [0]*N
    for _ in range(Q):
        p,x = map(int,input().split())
        p -= 1
        A[p] += x
        if p != 0:
            A[P[p]] -= x
    Q = deque([0])
    while Q:
        v = Q.popleft()
        for u in G[v]:
            if D[u] > D[v]:
                A[u] += A[v]
                Q.append(u)
    print(*A)

=======
Suggestion 8

def main():
    N, Q = map(int, input().split())
    # N = 6
    # Q = 2
    # a = [1, 1, 2, 3]
    # b = [2, 3, 4, 6]
    # p = [1, 1]
    # x = [10, 10]
    a = [None] * (N - 1)
    b = [None] * (N - 1)
    for i in range(N - 1):
        a[i], b[i] = map(int, input().split())
    p = [None] * Q
    x = [None] * Q
    for i in range(Q):
        p[i], x[i] = map(int, input().split())

    # グラフを作る
    graph = [[] for _ in range(N)]
    for i in range(N - 1):
        graph[a[i] - 1].append(b[i] - 1)
        graph[b[i] - 1].append(a[i] - 1)

    # DFSで頂点の親を求める
    parent = [-1] * N
    stack = [0]
    while stack:
        v = stack.pop()
        for u in graph[v]:
            if parent[u] == -1:
                parent[u] = v
                stack.append(u)

    # DFSで頂点の子孫を求める
    children = [[] for _ in range(N)]
    stack = [0]
    while stack:
        v = stack.pop()
        for u in graph[v]:
            if parent[u] == v:
                children[v].append(u)
                stack.append(u)

    # 頂点の親から子孫への加算値を求める
    dp = [0] * N
    for i in range(Q):
        dp[p[i] - 1] += x[i]

    # 頂点の子孫から親への加算値を求める
    stack = [0]
    while stack:
        v = stack.pop()
        for u in graph[v]:
            if parent[u] == v:
                dp[u] += dp[v]
                stack.append(u)

    # 頂

=======
Suggestion 9

def main():
    # Write your code here
    n,q=map(int,input().split())
    p=[0]*n
    for i in range(n-1):
        a,b=map(int,input().split())
        p[b-1]=a-1
    x=[0]*n
    for i in range(q):
        p_,x_=map(int,input().split())
        x[p_]+=x_
    for i in range(n-1,0,-1):
        x[p[i]]+=x[i]
    print(*x)

main()

=======
Suggestion 10

def get_subtree_size(g, i):
    def _get_subtree_size(g, i, visited):
        visited.add(i)
        size = 1
        for j in g[i]:
            if j not in visited:
                size += _get_subtree_size(g, j, visited)
        return size
    return _get_subtree_size(g, i, set())
