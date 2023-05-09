def solve():
    N, M = map(int, input().split())
    graph = [[] for _ in range(N)]
    for _ in range(M):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        graph[u].append(v)
        graph[v].append(u)
    
    color = [-1 for _ in range(N)]
    def dfs(x, c):
        color[x] = c
        for y in graph[x]:
            if color[y] == c:
                return False
            if color[y] == -1 and not dfs(y, 1 - c):
                return False
        return True
    
    ans = 0
    for i in range(N):
        if color[i] == -1:
            if dfs(i, 0):
                ans += color.count(0) * color.count(1)
            else:
                ans += N * (N - 1) // 2
                break
    print(ans - M)
