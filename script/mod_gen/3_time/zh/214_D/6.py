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

if __name__ == '__main__':
    main()