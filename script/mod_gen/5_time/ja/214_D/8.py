def main():
    n = int(input())
    uvw = [list(map(int, input().split())) for _ in range(n - 1)]
    g = [[] for _ in range(n)]
    for u, v, w in uvw:
        g[u - 1].append((v - 1, w))
        g[v - 1].append((u - 1, w))
    def dfs(u, p = -1):
        res = 0
        for v, w in g[u]:
            if v == p:
                continue
            res = max(res, dfs(v, u) + w)
        return res
    ans = 0
    for u in range(n):
        ans = max(ans, dfs(u))
    print(ans * 2)

if __name__ == '__main__':
    main()