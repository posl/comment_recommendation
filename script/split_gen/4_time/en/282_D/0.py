def main():
    n, m = map(int, input().split())
    g = [[] for _ in range(n)]
    for _ in range(m):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        g[u].append(v)
        g[v].append(u)
    def dfs(v, c):
        color[v] = c
        for nv in g[v]:
            if color[nv] == c:
                return False
            if color[nv] == 0 and not dfs(nv, -c):
                return False
        return True
    color = [0] * n
    ans = 0
    for i in range(n):
        if color[i] == 0:
            if dfs(i, 1):
                b = sum(c == 1 for c in color)
                ans += b * (b - 1) // 2
                b = sum(c == -1 for c in color)
                ans += b * (b - 1) // 2
            else:
                print(0)
                exit()
    print(ans)
