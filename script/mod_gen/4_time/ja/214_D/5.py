def solve():
    N = int(input())
    edges = [tuple(map(int, input().split())) for _ in range(N - 1)]
    edges.sort(key=lambda x: x[2])
    uf = UnionFind(N)
    ans = 0
    for u, v, w in edges:
        ans += uf.size(u) * uf.size(v) * w
        uf.union(u, v)
    print(ans)

if __name__ == '__main__':
    solve()