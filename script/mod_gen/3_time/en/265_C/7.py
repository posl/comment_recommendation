def main():
    H, W = map(int, input().split())
    grid = []
    for i in range(H):
        grid.append(list(input()))
    visited = [[False for i in range(W)] for j in range(H)]
    i = 0
    j = 0
    while True:
        if i < 0 or i >= H or j < 0 or j >= W:
            print(-1)
            return
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
    print(i+1, j+1)

if __name__ == '__main__':
    main()