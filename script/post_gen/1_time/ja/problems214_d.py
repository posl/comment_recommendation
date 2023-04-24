Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    edges = []
    for _ in range(N - 1):
        u, v, w = map(int, input().split())
        edges.append((u, v, w))
    edges.sort(key=lambda x: x[2])
    ans = 0
    for i in range(N - 1):
        for j in range(i + 1, N):
            ans += edges[i][2] * edges[j][2]
    print(ans)

=======
Suggestion 2

def main():
    N = int(input())
    edges = []
    for _ in range(N - 1):
        u, v, w = map(int, input().split())
        edges.append((u, v, w))
    edges.sort(key=lambda x: x[2], reverse=True)
    uf = UnionFind(N + 1)
    ans = 0
    for u, v, w in edges:
        ans += uf.size(u) * uf.size(v) * w
        uf.union(u, v)
    print(ans)

=======
Suggestion 3

def main():
    n = int(input())
    edges = []
    for _ in range(n - 1):
        u, v, w = map(int, input().split())
        edges.append((w, u, v))
    edges.sort()
    tree = UnionFind(n)
    ans = 0
    for w, u, v in edges:
        size_u = tree.size(u)
        size_v = tree.size(v)
        ans += w * size_u * size_v
        tree.unite(u, v)
    print(ans)

=======
Suggestion 4

def main():
    n = int(input())
    edges = []
    for _ in range(n-1):
        u, v, w = map(int, input().split())
        edges.append((w, u, v))
    edges.sort()
    ans = 0
    uf = UnionFind(n)
    for w, u, v in edges:
        ans += w * uf.size(u) * uf.size(v)
        uf.union(u, v)
    print(ans)

=======
Suggestion 5

def dfs(v, p):
    for u, w in G[v]:
        if u == p:
            continue
        dist[u] = dist[v] + w
        dfs(u, v)

N = int(input())
G = [[] for _ in range(N)]
for _ in range(N - 1):
    u, v, w = map(int, input().split())
    u -= 1
    v -= 1
    G[u].append((v, w))
    G[v].append((u, w))

dist = [0] * N
dfs(0, -1)

ans = 0
for i in range(N):
    ans += dist[i]

for i in range(N):
    dist[i] = -dist[i]

dist.sort()
ans += dist[0] + dist[1]
print(ans)

=======
Suggestion 6

def main():
    N = int(input())
    edge = []
    for i in range(N-1):
        u,v,w = map(int,input().split())
        edge.append([u,v,w])
    edge.sort(key=lambda x:x[2])
    ans = 0
    for i in range(N-1):
        ans += (N-i-1)*edge[i][2]
    print(ans)

=======
Suggestion 7

def dfs(v, p, d):
    for u, w in graph[v]:
        if u == p: continue
        d[u] = d[v] + w
        dfs(u, v, d)

n = int(input())
graph = [[] for _ in range(n)]
for _ in range(n - 1):
    a, b, w = map(int, input().split())
    graph[a - 1].append((b - 1, w))
    graph[b - 1].append((a - 1, w))

d = [0] * n
dfs(0, -1, d)

ans = 0
for i in range(n):
    ans += d[i]
print(ans)

=======
Suggestion 8

def get_max_weight(n, edges):
    max_weight = 0
    for i in range(n):
        for j in range(i+1, n):
            max_weight = max(max_weight, edges[i][j])
    return max_weight

=======
Suggestion 9

def main():
    n = int(input())
    edges = []
    for i in range(n-1):
        edges.append(list(map(int, input().split())))

    edges.sort(key=lambda x:x[2])

    # Union-Find木
    class UnionFind:
        def __init__(self, n):
            self.n = n
            self.parents = [-1] * n

        def find(self, x):
            if self.parents[x] < 0:
                return x
            else:
                self.parents[x] = self.find(self.parents[x])
                return self.parents[x]

        def union(self, x, y):
            x = self.find(x)
            y = self.find(y)

            if x == y:
                return

            if self.parents[x] > self.parents[y]:
                x, y = y, x

            self.parents[x] += self.parents[y]
            self.parents[y] = x

        def size(self, x):
            return -self.parents[self.find(x)]

        def same(self, x, y):
            return self.find(x) == self.find(y)

        def members(self, x):
            root = self.find(x)
            return [i for i in range(self.n) if self.find(i) == root]

        def roots(self):
            return [i for i, x in enumerate(self.parents) if x < 0]

        def group_count(self):
            return len(self.roots())

        def all_group_members(self):
            return {r: self.members(r) for r in self.roots()}

        def __str__(self):
            return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())

    uf = UnionFind(n)
    result = 0
    for i in range(n-1):
        u, v, w = edges[i]
        u -= 1
        v -= 1
        result += uf.size(u) * uf.size(v) * w
        uf.union(u, v)

    print(result)

=======
Suggestion 10

def calc_f(n, edges):
    # 頂点iから頂点jまでの最短パスに含まれる辺の重みの最大値
    f = [[0] * n for _ in range(n)]
    for s, t, w in edges:
        f[s - 1][t - 1] = w
        f[t - 1][s - 1] = w
    # ワーシャルフロイド法
    for k in range(n):
        for i in range(n):
            for j in range(n):
                f[i][j] = max(f[i][j], f[i][k] + f[k][j])
    return f
