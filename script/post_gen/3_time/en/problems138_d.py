Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, Q = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N - 1)]
    PQX = [list(map(int, input().split())) for _ in range(Q)]
    #print(N, Q)
    #print(AB)
    #print(PQX)
    #print('-----')

    # [i] = [i] + [i - 1]
    # [i] = [i] + [i + 1]
    # [i] = [i] + [i - 1] + [i + 1]
    # [i] = [i] + [i - 2] + [i - 1] + [i + 1]
    # [i] = [i] + [i - 3] + [i - 2] + [i - 1] + [i + 1]
    # [i] = [i] + [i - 4] + [i - 3] + [i - 2] + [i - 1] + [i + 1]
    # [i] = [i] + [i - 5] + [i - 4] + [i - 3] + [i - 2] + [i - 1] + [i + 1]
    # [i] = [i] + [i - 6] + [i - 5] + [i - 4] + [i - 3] + [i - 2] + [i - 1] + [i + 1]
    # [i] = [i] + [i - 7] + [i - 6] + [i - 5] + [i - 4] + [i - 3] + [i - 2] + [i - 1] + [i + 1]
    # [i] = [i] + [i - 8] + [i - 7] + [i - 6] + [i - 5] + [i - 4] + [i - 3] + [i - 2] + [i - 1] + [i + 1]
    # [i] = [i

=======
Suggestion 2

def main():
    N, Q = map(int, input().split())
    a = [0] * (N - 1)
    b = [0] * (N - 1)
    for i in range(N - 1):
        a[i], b[i] = map(int, input().split())
    p = [0] * Q
    x = [0] * Q
    for i in range(Q):
        p[i], x[i] = map(int, input().split())
    G = [[] for _ in range(N + 1)]
    for i in range(N - 1):
        G[a[i]].append(b[i])
        G[b[i]].append(a[i])
    #print(G)
    #print(p)
    #print(x)
    counter = [0] * (N + 1)
    for i in range(Q):
        counter[p[i]] += x[i]
    #print(counter)
    stack = [1]
    visited = [0] * (N + 1)
    visited[1] = 1
    while stack:
        v = stack.pop()
        for w in G[v]:
            if visited[w] == 0:
                visited[w] = 1
                stack.append(w)
                counter[w] += counter[v]
    print(*counter[1:])

=======
Suggestion 3

def main():
    N, Q = map(int, input().split())
    tree = [[] for _ in range(N)]
    for _ in range(N - 1):
        a, b = map(int, input().split())
        tree[a - 1].append(b - 1)
        tree[b - 1].append(a - 1)
    counter = [0] * N
    for _ in range(Q):
        p, x = map(int, input().split())
        counter[p - 1] += x
    stack = [0]
    visited = [False] * N
    while stack:
        v = stack.pop()
        visited[v] = True
        for u in tree[v]:
            if not visited[u]:
                counter[u] += counter[v]
                stack.append(u)
    print(*counter)

=======
Suggestion 4

def main():
    N, Q = map(int, input().split())
    edge = [[] for _ in range(N)]
    for _ in range(N - 1):
        a, b = map(int, input().split())
        edge[a - 1].append(b - 1)
        edge[b - 1].append(a - 1)
    
    add = [0] * N
    for _ in range(Q):
        p, x = map(int, input().split())
        add[p - 1] += x
    
    ans = [0] * N
    que = [0]
    while que:
        now = que.pop()
        for nxt in edge[now]:
            if ans[nxt] == 0:
                ans[nxt] = ans[now] + add[nxt]
                que.append(nxt)
    
    for i in range(N):
        if ans[i] == 0:
            ans[i] = add[i]
    
    print(*ans)

=======
Suggestion 5

def main():
    n, q = map(int, input().split())
    tree = [[] for _ in range(n)]
    for _ in range(n - 1):
        a, b = map(int, input().split())
        tree[a - 1].append(b - 1)
        tree[b - 1].append(a - 1)
    counter = [0] * n
    for _ in range(q):
        p, x = map(int, input().split())
        counter[p - 1] += x
    ans = [0] * n
    def dfs(v, p):
        ans[v] += counter[v]
        if p != -1:
            ans[v] += ans[p]
        for u in tree[v]:
            if u == p:
                continue
            dfs(u, v)
    dfs(0, -1)
    print(*ans)

=======
Suggestion 6

def main():
    N, Q = map(int, input().split())
    graph = [[] for _ in range(N)]
    for _ in range(N - 1):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        graph[a].append(b)
        graph[b].append(a)
    counter = [0] * N
    for _ in range(Q):
        p, x = map(int, input().split())
        p -= 1
        counter[p] += x
    stack = [(0, 0)]
    while stack:
        v, p = stack.pop()
        counter[v] += counter[p]
        for u in graph[v]:
            if u == p:
                continue
            stack.append((u, counter[v]))
    print(*counter)

=======
Suggestion 7

def main():
    N, Q = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(N - 1)]
    queries = [list(map(int, input().split())) for _ in range(Q)]

    # 木を構成する
    tree = [[] for _ in range(N + 1)]
    for a, b in edges:
        tree[a].append(b)
        tree[b].append(a)

    # 頂点ごとの親を取得する
    parent = [0 for _ in range(N + 1)]
    stack = [1]
    while stack:
        v = stack.pop()
        for w in tree[v]:
            if w == parent[v]:
                continue
            parent[w] = v
            stack.append(w)

    # クエリに対応する頂点を取得する
    query_vertex = [[] for _ in range(N + 1)]
    for p, x in queries:
        query_vertex[p].append(x)

    # クエリに対応する頂点の値を取得する
    value = [0 for _ in range(N + 1)]
    stack = [1]
    while stack:
        v = stack.pop()
        for w in tree[v]:
            if w == parent[v]:
                continue
            stack.append(w)
        for x in query_vertex[v]:
            value[v] += x

    # 頂点ごとの値を取得する
    stack = [1]
    while stack:
        v = stack.pop()
        for w in tree[v]:
            if w == parent[v]:
                continue
            value[w] += value[v]
            stack.append(w)

    # 答えを出力する
    print(*value[1:])

=======
Suggestion 8

def main():
    N, Q = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(N-1)]
    ops = [list(map(int, input().split())) for _ in range(Q)]
    edges.sort(key=lambda x: x[1])
    tree = [[] for _ in range(N+1)]
    for edge in edges:
        tree[edge[0]].append(edge[1])
    scores = [0] * (N+1)
    for op in ops:
        scores[op[0]] += op[1]
    for i in range(1, N+1):
        for j in tree[i]:
            scores[j] += scores[i]
    print(*scores[1:])

=======
Suggestion 9

def main():
    N, Q = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(N-1)]
    operations = [list(map(int, input().split())) for _ in range(Q)]
    # make adjacency list
    adj_list = [[] for _ in range(N)]
    for e in edges:
        adj_list[e[0]-1].append(e[1]-1)
        adj_list[e[1]-1].append(e[0]-1)
    # make tree
    tree = [0 for _ in range(N)]
    # make parent list
    parent = [-1 for _ in range(N)]
    # make child list
    child = [[] for _ in range(N)]
    # make depth list
    depth = [0 for _ in range(N)]
    # make size list
    size = [0 for _ in range(N)]
    # make depth first search list
    dfs = []
    # make stack
    stack = [0]
    while stack:
        v = stack.pop()
        dfs.append(v)
        for c in adj_list[v]:
            if c == parent[v]:
                continue
            parent[c] = v
            child[v].append(c)
            depth[c] = depth[v] + 1
            stack.append(c)
    # make size list
    for v in reversed(dfs):
        size[v] = 1
        for c in child[v]:
            size[v] += size[c]
    # make tree
    for o in operations:
        tree[o[0]-1] += o[1]
        if o[0] < N:
            tree[o[0]] -= o[1]
    for v in range(1, N):
        tree[v] += tree[parent[v]]
    print(' '.join(map(str, tree)))

=======
Suggestion 10

def main():
    import sys
    from collections import deque
    input = sys.stdin.readline
    N, Q = map(int, input().split())
    edges = [[] for _ in range(N)]
    for _ in range(N-1):
        a, b = map(int, input().split())
        edges[a-1].append(b-1)
        edges[b-1].append(a-1)
    #print(edges)
    #print(edges[0])
    #print(edges[1])
    #print(edges[2])
    #print(edges[3])
    #print(edges[4])
    #print(edges[5])
    #print(edges[6])
    #print(edges[7])
    #print(edges[8])
    #print(edges[9])
    #print(edges[10])
    #print(edges[11])
    #print(edges[12])
    #print(edges[13])
    #print(edges[14])
    #print(edges[15])
    #print(edges[16])
    #print(edges[17])
    #print(edges[18])
    #print(edges[19])
    #print(edges[20])
    #print(edges[21])
    #print(edges[22])
    #print(edges[23])
    #print(edges[24])
    #print(edges[25])
    #print(edges[26])
    #print(edges[27])
    #print(edges[28])
    #print(edges[29])
    #print(edges[30])
    #print(edges[31])
    #print(edges[32])
    #print(edges[33])
    #print(edges[34])
    #print(edges[35])
    #print(edges[36])
    #print(edges[37])
    #print(edges[38])
    #print(edges[39])
    #print(edges[40])
    #print(edges[41])
    #print(edges[42])
    #print(edges[43])
    #print(edges[44])
    #print(edges[45])
    #print(edges[46])
    #print(edges[47])
    #print(edges[48])
    #print(edges[49])
    #print(edges[50])
    #print(edges[51])
    #print(edges[52])
    #print(edges[53])
    #print(edges[54])
    #print(edges[55])
    #print(edges[56])
    #print(edges[57])
    #print(edges[
