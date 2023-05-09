def solve():
    n, m = map(int, input().split())
    g = {i:[] for i in range(1, n + 1)}
    for i in range(m):
        u, v = map(int, input().split())
        g[u].append(v)
        g[v].append(u)
    ans = 0
    for a in range(1, n - 1):
        for b in g[a]:
            if a < b:
                for c in g[b]:
                    if b < c and a in g[c]:
                        ans += 1
    print(ans // 3)

if __name__ == '__main__':
    solve()