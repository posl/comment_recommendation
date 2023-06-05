def main():
    h, w = map(int, input().split())
    g = [input() for _ in range(h)]
    visited = [[False] * w for _ in range(h)]
    def dfs(x, y):
        if x < 0 or x >= h or y < 0 or y >= w:
            return (x, y)
        if visited[x][y]:
            return (-1, -1)
        visited[x][y] = True
        if g[x][y] == 'U':
            return dfs(x - 1, y)
        elif g[x][y] == 'D':
            return dfs(x + 1, y)
        elif g[x][y] == 'L':
            return dfs(x, y - 1)
        elif g[x][y] == 'R':
            return dfs(x, y + 1)
        else:
            return (-1, -1)
    print(dfs(0, 0)[0] + 1, dfs(0, 0)[1] + 1)

if __name__ == '__main__':
    main()