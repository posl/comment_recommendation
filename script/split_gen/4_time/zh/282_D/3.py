def solve():
    N, M = map(int, input().split())
    # 1. 读取边
    edges = []
    for i in range(M):
        u, v = map(int, input().split())
        edges.append((u, v))
    # 2. 构建邻接表
    adj = [[] for _ in range(N+1)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    # 3. 构建双线图
    # 黑色：0，白色：1，未涂色：-1
    colors = [-1] * (N+1)
    def dfs(u, color):
        colors[u] = color
        for v in adj[u]:
            if colors[v] == -1:
                dfs(v, 1-color)
    dfs(1, 0)
    # 4. 统计答案
    ans = 0
    for u, v in edges:
        if colors[u] != colors[v]:
            ans += 1
    print(ans)
solve()
