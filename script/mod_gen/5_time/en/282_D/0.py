def solve():
    N, M = map(int, input().split())
    G = [[] for _ in range(N)]
    for _ in range(M):
        u, v = map(int, input().split())
        G[u-1].append(v-1)
        G[v-1].append(u-1)
    color = [None] * N
    def dfs(v, c):
        if color[v] is not None:
            return color[v] == c
        color[v] = c
        for w in G[v]:
            if not dfs(w, 1-c):
                return False
        return True
    ans = 0
    for v in range(N):
        if color[v] is None:
            if dfs(v, 0):
                cnt0 = color.count(0)
                cnt1 = N - cnt0
                ans += cnt0 * (cnt0-1) // 2 + cnt1 * (cnt1-1) // 2
            else:
                ans += N * (N-1) // 2
    print(ans)
solve()

if __name__ == '__main__':
    solve()