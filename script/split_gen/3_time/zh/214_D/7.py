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
