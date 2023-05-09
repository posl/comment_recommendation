def main():
    h, w = map(int, input().split())
    grid = []
    for i in range(h):
        grid.append(input())
    visited = [[False for _ in range(w)] for _ in range(h)]
    def dfs(i, j):
        if i < 0 or i >= h or j < 0 or j >= w or grid[i][j] == '#' or visited[i][j]:
            return 0
        visited[i][j] = True
        return 1 + dfs(i, j + 1) + dfs(i + 1, j)
    print(dfs(0, 0))
