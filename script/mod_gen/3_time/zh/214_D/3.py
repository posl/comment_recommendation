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

if __name__ == '__main__':
    main()