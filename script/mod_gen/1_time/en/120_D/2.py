def main():
    N, M = map(int, input().split())
    bridges = []
    for i in range(M):
        a, b = map(int, input().split())
        bridges.append((a, b))
    bridges.reverse()
    ans = [0] * M
    ans[0] = N * (N - 1) // 2
    #print(ans)
    parent = [i for i in range(N + 1)]
    rank = [0] * (N + 1)
    #print(parent, rank)
    def root(x):
        if parent[x] == x:
            return x
        else:
            parent[x] = root(parent[x])
            return parent[x]
    def unite(x, y):
        x = root(x)
        y = root(y)
        if x == y:
            return
        if rank[x] < rank[y]:
            parent[x] = y
        else:
            parent[y] = x
            if rank[x] == rank[y]:
                rank[x] += 1
    def same(x, y):
        return root(x) == root(y)
    for i in range(M - 1):
        a, b = bridges[i]
        if same(a, b):
            ans[i + 1] = ans[i]
        else:
            ans[i + 1] = ans[i] - (rank[root(a)] + 1) * (rank[root(b)] + 1)
            unite(a, b)
    ans.reverse()
    for i in ans:
        print(i)
main()

if __name__ == '__main__':
    main()