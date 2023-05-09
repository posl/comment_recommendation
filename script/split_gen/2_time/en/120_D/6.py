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
