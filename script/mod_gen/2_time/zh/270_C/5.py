def main():
    # 读取输入
    n, x, y = map(int, input().split())
    uv = [list(map(int, input().split())) for _ in range(n-1)]
    # 构建邻接表
    adj = [[] for _ in range(n+1)]
    for u, v in uv:
        adj[u].append(v)
        adj[v].append(u)
    # DFS
    def dfs(u, p):
        for v in adj[u]:
            if v == p:
                continue
            if v == y:
                return [v]
            res = dfs(v, u)
            if res:
                return [u] + res
        return []
    res = dfs(x, -1)
    print(*res)

if __name__ == '__main__':
    main()