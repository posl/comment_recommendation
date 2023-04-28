Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    graph = [[] for _ in range(N)]
    for _ in range(N-1):
        u, v, w = map(int, input().split())
        graph[u-1].append((v-1, w))
        graph[v-1].append((u-1, w))
    #print(graph)

    # 1からの距離を求める
    from collections import deque
    dist = [float('inf')]*N
    dist[0] = 0
    q = deque([0])
    while q:
        u = q.popleft()
        for v, w in graph[u]:
            if dist[v] > dist[u] + w:
                dist[v] = dist[u] + w
                q.append(v)
    #print(dist)

    # 木の直径を求める
    dist2 = [float('inf')]*N
    dist2[0] = 0
    q = deque([0])
    while q:
        u = q.popleft()
        for v, w in graph[u]:
            if dist2[v] > dist2[u] + w:
                dist2[v] = dist2[u] + w
                q.append(v)
    #print(dist2)

    # 木の直径を求める
    dist3 = [float('inf')]*N
    dist3[0] = 0
    q = deque([0])
    while q:
        u = q.popleft()
        for v, w in graph[u]:
            if dist3[v] > dist3[u] + w:
                dist3[v] = dist3[u] + w
                q.append(v)
    #print(dist3)

    #print(sum(dist2))
    #print(sum(dist3))

    print(sum(dist2)+sum(dist3)-max(dist2))

=======
Suggestion 2

def main():
    N = int(input())
    edges = []
    for i in range(N-1):
        u, v, w = map(int, input().split())
        edges.append((u, v, w))
    edges.sort(key=lambda x: x[2])
    parents = [i for i in range(N+1)]
    sizes = [1 for i in range(N+1)]
    def root(x):
        if parents[x] == x:
            return x
        else:
            parents[x] = root(parents[x])
            return parents[x]
    def unite(x, y):
        x = root(x)
        y = root(y)
        if x == y:
            return
        if sizes[x] < sizes[y]:
            x, y = y, x
        parents[y] = x
        sizes[x] += sizes[y]
    def same(x, y):
        return root(x) == root(y)
    ans = 0
    for u, v, w in edges:
        ans += sizes[root(u)] * sizes[root(v)] * w
        unite(u, v)
    print(ans)
main()

=======
Suggestion 3

def main():
    N = int(input())
    u, v, w = [], [], []
    for i in range(N-1):
        a, b, c = map(int, input().split())
        u.append(a)
        v.append(b)
        w.append(c)
    #print(u)
    #print(v)
    #print(w)
    #print(N)
    #print(len(u))
    #print(len(v))
    #print(len(w))

    ans = 0
    for i in range(N-1):
        for j in range(i+1, N):
            #print(i, j)
            #print(u[i], v[i], w[i])
            #print(u[j], v[j], w[j])
            #print()
            if u[i] == u[j]:
                ans += w[i]
            elif u[i] == v[j]:
                ans += w[i]
            elif v[i] == u[j]:
                ans += w[i]
            elif v[i] == v[j]:
                ans += w[i]
    print(ans)

=======
Suggestion 4

def main():
    n = int(input())
    edge = []
    for _ in range(n-1):
        u, v, w = map(int, input().split())
        edge.append((w, u, v))
    edge.sort()
    ans = 0
    for i in range(n-1):
        ans += edge[i][0] * (i+1) * (n-i-1)
    print(ans)

=======
Suggestion 5

def find(x):
    if par[x] == x:
        return x
    else:
        par[x] = find(par[x])
        return par[x]

=======
Suggestion 6

def solve():
    N = int(input())
    edges = [tuple(map(int, input().split())) for _ in range(N - 1)]
    edges.sort(key=lambda x: x[2])
    uf = UnionFind(N)
    ans = 0
    for u, v, w in edges:
        ans += uf.size(u) * uf.size(v) * w
        uf.union(u, v)
    print(ans)

=======
Suggestion 7

def main():
    N = int(input())
    edges = []
    for i in range(N-1):
        edges.append(list(map(int,input().split())))
    edges.sort(key=lambda x:x[2])
    #print(edges)
    ans = 0
    for i in range(N-1):
        ans += edges[i][2]*(i+1)*(N-i-1)
    print(ans)

=======
Suggestion 8

def main():
    # 入力受け取り
    N = int(input())
    uvws = []
    for i in range(N-1):
        uvws.append(list(map(int, input().split())))

    # 隣接リスト作成
    adj_list = [[] for _ in range(N)]
    for u, v, w in uvws:
        adj_list[u-1].append((v-1, w))
        adj_list[v-1].append((u-1, w))

    # dfs
    # https://atcoder.jp/contests/abc214/submissions/25019438
    ans = 0
    stack = [(0, 0, 0)]
    while stack:
        v, p, d = stack.pop()
        ans += d
        for nv, w in adj_list[v]:
            if nv == p:
                continue
            stack.append((nv, v, max(d, w)))

    print(ans)

=======
Suggestion 9

def main():
    n = int(input())
    data = [list(map(int, input().split())) for _ in range(n-1)]

    # print(data)

    # まずは頂点の最大値を求める
    max_v = 0
    for d in data:
        max_v = max(max_v, d[0], d[1])

    # print(max_v)

    # 隣接リストを作成する
    adj_list = [[] for _ in range(max_v)]
    for d in data:
        adj_list[d[0]-1].append([d[1]-1, d[2]])
        adj_list[d[1]-1].append([d[0]-1, d[2]])

    # print(adj_list)

    # ダイクストラ法で最短距離を求める
    # ここで、最短距離の値が最大となるものを求める
    # その最大値がf(i,j)となる
    import heapq
    INF = 10**18
    def dijkstra(s):
        dist = [INF] * max_v
        dist[s] = 0
        hq = [(0, s)] # (dist, vertex)
        heapq.heapify(hq)
        while hq:
            p = heapq.heappop(hq)
            v = p[1]
            if dist[v] < p[0]:
                continue
            for e in adj_list[v]:
                if dist[e[0]] > dist[v] + e[1]:
                    dist[e[0]] = dist[v] + e[1]
                    heapq.heappush(hq, (dist[e[0]], e[0]))
        return dist

    max_dist = 0
    for i in range(max_v):
        dist = dijkstra(i)
        for j in range(i+1, max_v):
            max_dist = max(max_dist, dist[j])

    print(max_dist * (n-1))

=======
Suggestion 10

def solve():
    return
