def main():
    # 读入数据
    N, M = map(int, input().split())
    # 建立邻接表
    adj = [[] for _ in range(N)]
    for _ in range(M):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        adj[u].append(v)
        adj[v].append(u)
    # DFS判断是否为路径图
    seen = [False] * N
    def dfs(v):
        seen[v] = True
        if len(adj[v]) == 1:
            return True
        for nv in adj[v]:
            if seen[nv]:
                continue
            if not dfs(nv):
                return False
        return True
    for v in range(N):
        if seen[v]:
            continue
        if not dfs(v):
            print("No")
            return
    print("Yes")
