def main():
    n = int(input())
    edges = [list(map(int, input().split())) for _ in range(n - 1)]
    edges.sort(key=lambda x: x[2])
    parents = [i for i in range(n)]
    rank = [0 for _ in range(n)]
    def find(x):
        if parents[x] == x:
            return x
        else:
            parents[x] = find(parents[x])
            return parents[x]
    def unite(x, y):
        x = find(x)
        y = find(y)
        if x == y:
            return
        if rank[x] < rank[y]:
            parents[x] = y
        else:
            parents[y] = x
            if rank[x] == rank[y]:
                rank[x] += 1
    def same(x, y):
        return find(x) == find(y)
    def weight(x, y):
        return edges[x][2] + edges[y][2]
    def kruskal():
        res = 0
        for i in range(n - 1):
            if not same(edges[i][0] - 1, edges[i][1] - 1):
                unite(edges[i][0] - 1, edges[i][1] - 1)
                res += weight(i, i)
        return res
    print(kruskal())

if __name__ == '__main__':
    main()