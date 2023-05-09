def main():
    N = int(input())
    edges = []
    for _ in range(N - 1):
        u, v, w = map(int, input().split())
        edges.append((w, u - 1, v - 1))
    edges.sort(reverse = True)
    par = [i for i in range(N)]
    rank = [0 for _ in range(N)]
    def find(x):
        if par[x] == x:
            return x
        else:
            par[x] = find(par[x])
            return par[x]
    def unite(x, y):
        x = find(x)
        y = find(y)
        if x == y:
            return False
        if rank[x] < rank[y]:
            par[x] = y
        else:
            par[y] = x
            if rank[x] == rank[y]:
                rank[x] += 1
        return True
    def same(x, y):
        return find(x) == find(y)
    ans = 0
    for w, u, v in edges:
        ans += (w * (N - 1)) * (N - 1 - (N - 1) // 2)
        ans -= (w * (N - 1)) * (N - 1) // 2
        ans -= (w * (N - 1) * (N - 1)) // 2
        unite(u, v)
    print(ans)

if __name__ == '__main__':
    main()