Synthesizing 9/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    A = [0] * M
    B = [0] * M
    for i in range(M):
        A[i], B[i] = map(int, input().split())
    G = [set() for _ in range(N + 1)]
    for i in range(M):
        G[A[i]].add(B[i])
        G[B[i]].add(A[i])
    ans = [0] * M
    ans[M - 1] = N * (N - 1) // 2
    for i in range(M - 1, 0, -1):
        ans[i - 1] = ans[i]
        if len(G[A[i]]) > len(G[B[i]]):
            A[i], B[i] = B[i], A[i]
        for j in G[A[i]]:
            if j < A[i]:
                ans[i - 1] -= 1
            G[j].remove(A[i])
            G[j].add(B[i])
        G[B[i]].update(G[A[i]])
        G[A[i]] = set()
    print('
'.join(map(str, ans)))

=======
Suggestion 2

def find(x):
    if par[x] == x:
        return x
    else:
        par[x] = find(par[x])
        return par[x]

=======
Suggestion 3

def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    AB.reverse()
    ans = [0] * M
    ans[0] = N * (N - 1) // 2
    parent = [i for i in range(N + 1)]
    size = [1] * (N + 1)
    for i in range(1, M):
        a, b = AB[i]
        if find(a, parent) != find(b, parent):
            ans[i] = ans[i - 1] - size[find(a, parent)] * size[find(b, parent)]
            unite(a, b, parent, size)
        else:
            ans[i] = ans[i - 1]
    ans.reverse()
    print(*ans, sep='
')

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    AB.reverse()
    ans = [0] * M
    ans[0] = N * (N - 1) // 2
    c = [1] * (N + 1)
    for i in range(1, M):
        a, b = AB[i]
        if c[a] < c[b]:
            a, b = b, a
        ans[i] = ans[i - 1] - c[a] * c[b]
        c[a] += c[b]
    print(*ans[::-1], sep='

')

=======
Suggestion 5

def main():
    N, M = map(int, input().split())
    bridges = [list(map(int, input().split())) for _ in range(M)]
    bridges.reverse()
    ans = [0] * M
    ans[0] = (N - 1) * N // 2
    parent = list(range(N + 1))
    size = [1] * (N + 1)
    for i in range(M - 1):
        a, b = bridges[i]
        pa = root(a, parent)
        pb = root(b, parent)
        if pa != pb:
            ans[i + 1] = ans[i] - (size[pa] * size[pb])
            union(pa, pb, parent, size)
        else:
            ans[i + 1] = ans[i]
    ans.reverse()
    for i in ans:
        print(i)

=======
Suggestion 6

def main():
    n, m = map(int, input().split())
    bridge = [list(map(int, input().split())) for _ in range(m)]
    bridge.reverse()
    ans = [0] * m
    ans[0] = n * (n - 1) // 2
    uf = UnionFind(n)
    for i, (a, b) in enumerate(bridge):
        a -= 1
        b -= 1
        if uf.same(a, b):
            ans[i + 1] = ans[i]
        else:
            ans[i + 1] = ans[i] - uf.size(a) * uf.size(b)
            uf.union(a, b)
    ans.reverse()
    for a in ans:
        print(a)

=======
Suggestion 7

def main():
    N, M = map(int, input().split())
    AB = [tuple(map(int, input().split())) for _ in range(M)]

    # Union-Find
    class UnionFind:
        def __init__(self, N):
            self.parent = [i for i in range(N)]
            self.rank = [0] * N
            self.size = [1] * N

        def find(self, x):
            if self.parent[x] == x:
                return x
            else:
                self.parent[x] = self.find(self.parent[x])
                return self.parent[x]

        def unite(self, x, y):
            x = self.find(x)
            y = self.find(y)
            if x == y:
                return
            if self.rank[x] < self.rank[y]:
                self.parent[x] = y
                self.size[y] += self.size[x]
            else:
                self.parent[y] = x
                self.size[x] += self.size[y]
                if self.rank[x] == self.rank[y]:
                    self.rank[x] += 1

        def same(self, x, y):
            return self.find(x) == self.find(y)

        def get_size(self, x):
            return self.size[self.find(x)]

    # 連結成分の数
    uf = UnionFind(N)
    for a, b in AB:
        uf.unite(a - 1, b - 1)
    size = [uf.get_size(i) for i in range(N)]

    # 答えを求める
    ans = [0] * M
    ans[-1] = N * (N - 1) // 2
    for i in range(M - 1, 0, -1):
        a, b = AB[i]
        a -= 1
        b -= 1
        if not uf.same(a, b):
            ans[i - 1] = ans[i] - size[a] * size[b]
            uf.unite(a, b)
            size[uf.find(a)] += size[uf.find(b)]
        else:
            ans[i - 1] = ans[i]

    for a in ans:
        print(a)

=======
Suggestion 8

def main():
    N, M = map(int, input().split())
    bridges = [tuple(map(int, input().split())) for _ in range(M)]

    # 1-indexed
    par = list(range(N + 1))
    rank = [0] * (N + 1)
    size = [1] * (N + 1)

    def find(x):
        if par[x] == x:
            return x
        par[x] = find(par[x])
        return par[x]

    def unite(x, y):
        x = find(x)
        y = find(y)
        if x == y:
            return
        if rank[x] < rank[y]:
            x, y = y, x
        if rank[x] == rank[y]:
            rank[x] += 1
        par[y] = x
        size[x] += size[y]

    def same(x, y):
        return find(x) == find(y)

    def get_size(x):
        return size[find(x)]

    ans = [0] * M
    ans[-1] = N * (N - 1) // 2
    for i in range(M - 1, 0, -1):
        a, b = bridges[i]
        if same(a, b):
            ans[i - 1] = ans[i]
        else:
            ans[i - 1] = ans[i] - get_size(a) * get_size(b)
            unite(a, b)

    for i in range(M):
        print(ans[i])

=======
Suggestion 9

def main():
    n, m = map(int, input().split())
    ab = [list(map(int, input().split())) for _ in range(m)]

    # Union-Find木
    #
