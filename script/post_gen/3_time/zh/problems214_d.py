Synthesizing 10/10 solutions

=======
Suggestion 1

def get_input():
    n = int(input())
    if n < 2 or n > 100000:
        raise Exception("n out of range")
    edge = []
    for i in range(n - 1):
        u, v, w = input().split()
        edge.append((int(u), int(v), int(w)))
    return n, edge

=======
Suggestion 2

def main():
    n = int(input())
    w = [0] * (n + 1)
    for _ in range(n - 1):
        u, v, w_ = map(int, input().split())
        w[u] += w_
        w[v] += w_
    ans = sum(w[i] * w[j] for i in range(1, n + 1) for j in range(i + 1, n + 1))
    print(ans)

=======
Suggestion 3

def solve():
    pass

=======
Suggestion 4

def main():
    n = int(input())
    edges = []
    for i in range(n-1):
        u, v, w = map(int, input().split())
        edges.append((w, u, v))
    edges.sort()
    parents = [i for i in range(n+1)]
    def find(x):
        if parents[x] != x:
            parents[x] = find(parents[x])
        return parents[x]
    def union(u, v):
        parents[find(u)] = find(v)
    def same(u, v):
        return find(u) == find(v)
    def kruskal():
        res = 0
        for w, u, v in edges:
            if not same(u, v):
                union(u, v)
                res += w
        return res
    res = kruskal()
    print(res*2)

=======
Suggestion 5

def find_root(u):
    if u == root[u]:
        return u
    else:
        root[u] = find_root(root[u])
        return root[u]

=======
Suggestion 6

def main():
    n = int(input())
    u = [0] * (n-1)
    v = [0] * (n-1)
    w = [0] * (n-1)
    for i in range(n-1):
        u[i], v[i], w[i] = map(int, input().split())

    #print(u)
    #print(v)
    #print(w)

    # 构建邻接表
    adj = [[] for _ in range(n+1)]
    for i in range(n-1):
        adj[u[i]].append((v[i], w[i]))
        adj[v[i]].append((u[i], w[i]))

    #print(adj)
    # 构建父节点
    parent = [-1] * (n+1)
    parent[1] = 0
    q = [1]
    while q:
        cur = q.pop(0)
        for next, _ in adj[cur]:
            if parent[next] == -1:
                parent[next] = cur
                q.append(next)

    #print(parent)

    # 计算每个节点的子节点的权重和
    child = [0] * (n+1)
    for i in range(2, n+1):
        child[parent[i]] += child[i] + 1

    #print(child)

    # 计算每个节点的子节点的权重和
    ans = 0
    for i in range(n-1):
        if parent[u[i]] == v[i]:
            ans += w[i] * (n - child[u[i]])
        else:
            ans += w[i] * (n - child[v[i]])

    print(ans)

=======
Suggestion 7

def main():
    N = int(input())
    edges = []
    for i in range(N-1):
        u, v, w = map(int, input().split())
        edges.append((w, u, v))
    edges.sort()
    parent = [i for i in range(N+1)]
    size = [1] * (N+1)
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
        if size[x] > size[y]:
            x, y = y, x
        parent[x] = y
        size[y] += size[x]
    ans = 0
    for w, u, v in edges:
        ans += w * size[find(u)] * size[find(v)]
        union(u, v)
    print(ans)

=======
Suggestion 8

def solve():
    n = int(input())
    edges = []
    for i in range(n - 1):
        u, v, w = map(int, input().split())
        edges.append((u, v, w))
    edges.sort(key=lambda x: x[2])
    parent = [i for i in range(n + 1)]

    def find(x):
        if parent[x] == x:
            return x
        parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        parent[find(x)] = find(y)

    def kruskal():
        res = 0
        for u, v, w in edges:
            if find(u) != find(v):
                union(u, v)
                res += w
        return res

    a = kruskal()
    b = 0
    for u, v, w in edges:
        if find(u) != find(v):
            union(u, v)
            b += w
    print(a + b)


solve()

=======
Suggestion 9

def main():
    n = int(input())
    uvw = []
    for i in range(n-1):
        uvw.append(list(map(int,input().split())))
    print(uvw)
    for i in range(n-1):
        print(i)
        print(uvw[i][0],uvw[i][1])
        print(uvw[i][2])

=======
Suggestion 10

def main():
    pass
