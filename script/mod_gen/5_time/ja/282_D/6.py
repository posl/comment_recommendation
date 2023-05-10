def main():
    n, m = map(int, input().split())
    g = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v = map(int, input().split())
        g[u].append(v)
        g[v].append(u)
    color = [0] * (n + 1)
    def dfs(v, c):
        color[v] = c
        for to in g[v]:
            if color[to] == c:
                return False
            if color[to] == 0 and not dfs(to, -c):
                return False
        return True
    ans = 0
    for i in range(1, n + 1):
        if color[i] == 0:
            if dfs(i, 1):
                black = color.count(1)
                white = color.count(-1)
                ans += black * white
            else:
                break
    else:
        print(ans)
        return
    print(0)

if __name__ == '__main__':
    main()