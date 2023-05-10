def solve():
    n, m = map(int, input().split())
    g = [[] for _ in range(n)]
    for _ in range(m):
        a, b = map(int, input().split())
        g[a-1].append(b-1)
        g[b-1].append(a-1)
    dp = [[0]*(1<<n) for _ in range(n)]
    for i in range(n):
        dp[i][1<<i] = 1
    for s in range(1<<n):
        for v in range(n):
            if not (s>>v)&1:
                continue
            for u in g[v]:
                if (s>>u)&1:
                    dp[v][s] += dp[u][s^(1<<v)]
    print(sum(dp[i][(1<<n)-1] for i in range(n)))
solve()

if __name__ == '__main__':
    solve()