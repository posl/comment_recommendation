def main():
    h, w = map(int, input().split())
    maze = [input() for _ in range(h)]
    ans = 0
    for i in range(h):
        for j in range(w):
            if maze[i][j] == '.':
                ans = max(ans, dfs(i, j, maze))
    print(ans)
