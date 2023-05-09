def main():
    n, m = map(int, input().split())
    # 1-indexed
    g = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b = map(int, input().split())
        g[a].append(b)
        g[b].append(a)
    def dfs(v, c):
        color[v] = c
        for nv in g[v]:
            if color[nv] == c:
                return False
            if color[nv] == 0 and not dfs(nv, -c):
                return False
        return True
    color = [0] * (n + 1)
    for i in range(1, n + 1):
        if color[i] == 0:
            if not dfs(i, 1):
                print("No")
                return
    print("Yes")

if __name__ == '__main__':
    main()