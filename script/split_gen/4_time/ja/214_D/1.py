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
