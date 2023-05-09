def main():
    N = int(input())
    edges = [list(map(int, input().split())) for _ in range(N - 1)]
    edges.sort(key=lambda x: x[2], reverse=True)
    parent = [i for i in range(N + 1)]
    rank = [0 for _ in range(N + 1)]
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
        if rank[x] < rank[y]:
            parent[x] = y
        else:
            parent[y] = x
            if rank[x] == rank[y]:
                rank[x] += 1
    ans = 0
    for u, v, w in edges:
        ans += w * (find(u) != find(v)) * (rank[find(u)] + rank[find(v)] + 1)
        union(u, v)
    print(ans)

if __name__ == '__main__':
    main()