def main():
    n, m = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(m)]
    adj = [[] for _ in range(n)]
    for u, v in edges:
        u -= 1
        v -= 1
        adj[u].append(v)
        adj[v].append(u)
    color = [-1] * n
    def dfs(u, c):
        color[u] = c
        for v in adj[u]:
            if color[v] == c:
                return False
            if color[v] == -1 and not dfs(v, 1 - c):
                return False
        return True
    ans = 0
    for u in range(n):
        if color[u] != -1:
            continue
        if not dfs(u, 0):
            print(0)
            return
        ans += 1
    print(ans * (n - ans) - m)
main()
