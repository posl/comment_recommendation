Synthesizing 10/10 solutions

=======
Suggestion 1

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
    # 1-indexed array
    a = [0] + a
    b = [0] + b
    p = [0] + p
    x = [0] + x
    # adjacency list
    adj = [[] for _ in range(N + 1)]
    for i in range(1, N):
        adj[a[i]].append(b[i])
        adj[b[i]].append(a[i])
    # dfs
    visited = [False] * (N + 1)
    parent = [0] * (N + 1)
    depth = [0] * (N + 1)
    first = [0] * (N + 1)
    last = [0] * (N + 1)
    order = []
    def dfs(v, d):
        visited[v] = True
        depth[v] = d
        first[v] = len(order)
        order.append(v)
        for u in adj[v]:
            if visited[u]:
                continue
            parent[u] = v
            dfs(u, d + 1)
            order.append(v)
        last[v] = len(order) - 1
    dfs(1, 0)
    # segment tree
    st = [0] * (2 * N)
    def update(i, x):
        i += N
        st[i] += x
        while i > 1:
            i >>= 1
            st[i] = st[2 * i] + st[2 * i + 1]
    def query(l, r):
        l += N
        r += N
        s = 0
        while l < r:
            if l & 1:
                s += st[l]
                l += 1
            if r & 1:
                r -= 1
                s += st[r]
            l >>= 1

=======
Suggestion 2

def main():
    N, Q = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(N - 1)]
    queries = [list(map(int, input().split())) for _ in range(Q)]
    #print(N, Q)
    #print(edges)
    #print(queries)
    #print()
    graph = [[] for _ in range(N)]
    for a, b in edges:
        graph[a - 1].append(b - 1)
        graph[b - 1].append(a - 1)
    #print(graph)
    #print()

    # DFS
    #https://atcoder.jp/contests/abc138/submissions/20751130
    #https://atcoder.jp/contests/abc138/submissions/20751320
    #https://atcoder.jp/contests/abc138/submissions/20751372
    #https://atcoder.jp/contests/abc138/submissions/20751489
    #https://atcoder.jp/contests/abc138/submissions/20751544
    #https://atcoder.jp/contests/abc138/submissions/20751691
    #https://atcoder.jp/contests/abc138/submissions/20751731
    #https://atcoder.jp/contests/abc138/submissions/20751844
    #https://atcoder.jp/contests/abc138/submissions/20751938
    #https://atcoder.jp/contests/abc138/submissions/20752042
    #https://atcoder.jp/contests/abc138/submissions/20752163
    #https://atcoder.jp/contests/abc138/submissions/20752260
    #https://atcoder.jp/contests/abc138/submissions/20752301
    #https://atcoder.jp/contests/abc138/submissions/20752354
    #https://atcoder.jp/contests/abc138/submissions/20752408
    #https://atcoder.jp/contests/abc138/submissions/20752449
    #https://atcoder.jp/contests/abc138/submissions/20752592
    #https://atcoder.jp/contests/abc138/submissions/20752644
    #https://atcoder.jp/

=======
Suggestion 3

def main():
    N, Q = map(int, input().split())
    E = [[] for _ in range(N)]
    for _ in range(N-1):
        a, b = map(int, input().split())
        E[a-1].append(b-1)
        E[b-1].append(a-1)
    P, X = [], []
    for _ in range(Q):
        p, x = map(int, input().split())
        P.append(p-1)
        X.append(x)
    A = [0] * N
    for p, x in zip(P, X):
        A[p] += x
    Q = [0]
    V = [0] * N
    while Q:
        v = Q.pop()
        for u in E[v]:
            if V[u]:
                continue
            V[u] = 1
            A[u] += A[v]
            Q.append(u)
    print(*A)

=======
Suggestion 4

def main():
    N, Q = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(N - 1)]
    operations = [list(map(int, input().split())) for _ in range(Q)]
    print(*solve(N, Q, edges, operations))

=======
Suggestion 5

def main():
    N, Q = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(N - 1)]
    operations = [list(map(int, input().split())) for _ in range(Q)]

    # グラフの構築
    graph = [[] for _ in range(N)]
    for a, b in edges:
        graph[a - 1].append(b - 1)
        graph[b - 1].append(a - 1)

    # グラフの構築
    # graph = [[] for _ in range(N)]
    # for a, b in edges:
    #     graph[a - 1].append(b - 1)
    #     graph[b - 1].append(a - 1)

    # 木の根から各頂点への距離を計算
    dist = [0] * N
    stack = [0]
    while stack:
        v = stack.pop()
        for u in graph[v]:
            if dist[u] == 0:
                dist[u] = dist[v] + 1
                stack.append(u)

    # 頂点ごとの操作回数を計算
    cnt = [0] * N
    for p, x in operations:
        cnt[p - 1] += x

    # 頂点ごとの操作回数を計算
    # cnt = [0] * N
    # for p, x in operations:
    #     cnt[p - 1] += x

    # 木の根から順に操作回数を加算
    stack = [0]
    while stack:
        v = stack.pop()
        for u in graph[v]:
            if dist[u] > dist[v]:
                cnt[u] += cnt[v]
                stack.append(u)

    # 木の根から順に操作回数を加算
    # stack = [0]
    # while stack:
    #     v = stack.pop()
    #     for u in graph[v]:
    #         if dist[u] > dist[v]:
    #             cnt[u] += cnt[v]
    #             stack.append(u)

    print(*cnt)

=======
Suggestion 6

def main():
    N, Q = map(int, input().split())
    a = []
    b = []
    for i in range(N-1):
        a_i, b_i = map(int, input().split())
        a.append(a_i)
        b.append(b_i)
    p = []
    x = []
    for i in range(Q):
        p_i, x_i = map(int, input().split())
        p.append(p_i)
        x.append(x_i)
    #print(N, Q)
    #print(a)
    #print(b)
    #print(p)
    #print(x)
    #print("")

    # initialize the tree
    tree = {}
    for i in range(N):
        tree[i+1] = []

    # link the tree
    for i in range(N-1):
        tree[a[i]].append(b[i])
        tree[b[i]].append(a[i])

    #print(tree)

    # initialize the counter
    counter = [0 for i in range(N)]

    #print(counter)

    # operation
    for i in range(Q):
        counter[p[i]-1] += x[i]

    #print(counter)

    # dfs
    stack = [1]
    visited = []
    while stack:
        v = stack.pop()
        visited.append(v)
        for child in tree[v]:
            if child not in visited:
                stack.append(child)
                counter[child-1] += counter[v-1]

    #print(counter)

    # output
    for i in range(N):
        print(counter[i], end=" ")
    print("")

=======
Suggestion 7

def main():
    n, q = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(n - 1)]
    queries = [list(map(int, input().split())) for _ in range(q)]
    g = [[] for _ in range(n + 1)]
    for a, b in edges:
        g[a].append(b)
        g[b].append(a)
    visited = [False] * (n + 1)
    visited[1] = True
    depth = [0] * (n + 1)
    parent = [0] * (n + 1)
    stack = [1]
    while stack:
        v = stack.pop()
        for u in g[v]:
            if visited[u]:
                continue
            visited[u] = True
            parent[u] = v
            depth[u] = depth[v] + 1
            stack.append(u)
    children = [[] for _ in range(n + 1)]
    for i in range(2, n + 1):
        children[parent[i]].append(i)
    idx = [0] * (n + 1)
    cnt = 0
    stack = [1]
    while stack:
        v = stack.pop()
        cnt += 1
        idx[v] = cnt
        for u in children[v]:
            stack.append(u)
    a = [0] * (n + 1)
    for p, x in queries:
        a[idx[p]] += x
        if idx[p] + len(children[p]) <= n:
            a[idx[p] + len(children[p])] -= x
    for i in range(1, n + 1):
        a[i] += a[i - 1]
    print(*a[1:])

main()

=======
Suggestion 8

def main():
    import sys
    from collections import defaultdict
    input = sys.stdin.readline
    N, Q = map(int, input().split())
    G = defaultdict(list)
    for _ in range(N-1):
        a, b = map(int, input().split())
        G[a].append(b)
        G[b].append(a)
    X = [0] * (N+1)
    for _ in range(Q):
        p, x = map(int, input().split())
        X[p] += x
    ans = [0] * (N+1)
    def dfs(v, p):
        ans[v] += X[v]
        for u in G[v]:
            if u == p: continue
            X[u] += X[v]
            dfs(u, v)
    dfs(1, -1)
    print(*ans[1:])

=======
Suggestion 9

def main():
    N, Q = map(int, input().split())
    # 隣接リストを作る
    adj = [[] for _ in range(N)]
    for _ in range(N - 1):
        a, b = map(int, input().split())
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    # 頂点ごとの加算値を保存する配列
    add = [0] * N
    for _ in range(Q):
        p, x = map(int, input().split())
        add[p - 1] += x
    # 深さ優先探索で頂点ごとの加算値を累積する
    ans = [0] * N
    stack = [0]
    while stack:
        v = stack.pop()
        for u in adj[v]:
            if ans[u] == 0:
                ans[u] = ans[v] + add[u]
                stack.append(u)
    print(*ans)

=======
Suggestion 10

def main():
    N, Q = map(int, input().split())
    # parent[i]: iの親
    parent = [0] * N
    # children[i]: iの子
    children = [[] for _ in range(N)]
    # depth[i]: iの深さ
    depth = [0] * N
    # cnt[i]: iの深さの部分木に含まれる頂点の数
    cnt = [0] * N
    # val[i]: iの深さの部分木に含まれる頂点のカウンターの合計
    val = [0] * N
    for _ in range(N - 1):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        if a > b:
            a, b = b, a
        parent[b] = a
        children[a].append(b)
    stack = [0]
    while stack:
        x = stack.pop()
        for y in children[x]:
            depth[y] = depth[x] + 1
            cnt[y] = 1
            stack.append(y)
    for _ in range(Q):
        p, x = map(int, input().split())
        p -= 1
        val[p] += x
        cnt[p] += 1
    stack = [0]
    while stack:
        x = stack.pop()
        for y in children[x]:
            val[y] += val[x]
            cnt[y] += cnt[x]
            stack.append(y)
    print(*val, sep=' ')
