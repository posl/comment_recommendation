def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10**6)
    N = int(input())
    graph = [[] for _ in range(N)]
    for _ in range(N-1):
        u, v, w = map(int, input().split())
        graph[u-1].append((v-1, w))
        graph[v-1].append((u-1, w))
    def dfs(node, parent):
        for child, w in graph[node]:
            if child == parent:
                continue
            dfs(child, node)
            dp[node][0] += dp[child][0] + w * dp[child][1]
            dp[node][1] += dp[child][1]
    dp = [[0, 0] for _ in range(N)]
    dfs(0, -1)
    def dfs2(node, parent):
        for child, w in graph[node]:
            if child == parent:
                continue
            dp[child][0] = dp[node][0] - dp[child][0] - w * dp[child][1] + (dp[node][1] - dp[child][1]) * w
            dp[child][1] = dp[node][1] - dp[child][1]
            dfs2(child, node)
    dfs2(0, -1)
    ans = 0
    for i in range(N):
        ans += dp[i][0]
    print(ans)
