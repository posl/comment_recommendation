def main():
    N = int(input())
    E = [list(map(int, input().split())) for _ in range(N-1)]
    E.sort(key=lambda x: x[2])
    G = [[] for _ in range(N)]
    for u, v, w in E:
        G[u-1].append(v-1)
        G[v-1].append(u-1)
    dp = [0] * N
    def dfs(x, p):
        for y in G[x]:
            if y != p:
                dp[y] = dp[x] + 1
                dfs(y, x)
    dfs(0, -1)
    ans = 0
    for i in range(N):
        ans += dp[i] * (N - dp[i] - 1)
    print(ans)
