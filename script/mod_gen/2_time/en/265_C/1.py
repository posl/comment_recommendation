def main():
    H, W = map(int, input().split())
    grid = [input() for _ in range(H)]
    visited = [[False] * W for _ in range(H)]
    i, j = 0, 0
    while True:
        if visited[i][j]:
            print(-1)
            return
        visited[i][j] = True
        if grid[i][j] == 'U':
            i -= 1
        elif grid[i][j] == 'D':
            i += 1
        elif grid[i][j] == 'L':
            j -= 1
        elif grid[i][j] == 'R':
            j += 1
        if i < 0 or i >= H or j < 0 or j >= W:
            print(i + 1, j + 1)
            return

if __name__ == '__main__':
    main()