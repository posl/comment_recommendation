def solve():
    N,M = map(int,input().split())
    graph = [[] for _ in range(N)]
    for _ in range(M):
        u,v = map(int,input().split())
        u -= 1
        v -= 1
        graph[u].append(v)
        graph[v].append(u)
    color = [None] * N
    def dfs(v,c):
        if color[v] is not None:
            return color[v] == c
        color[v] = c
        for v2 in graph[v]:
            if not dfs(v2,1-c):
                return False
        return True
    ans = 0
    for v in range(N):
        if color[v] is None:
            if dfs(v,0):
                b = color.count(0)
                ans += b * (b-1) // 2
                b = color.count(1)
                ans += b * (b-1) // 2
            else:
                ans += N * (N-1) // 2
                break
    print(ans)
solve()

if __name__ == '__main__':
    solve()