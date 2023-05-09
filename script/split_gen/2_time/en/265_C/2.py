def main():
    h, w = map(int, input().split())
    grid = [list(input()) for _ in range(h)]
    visited = [[0] * w for _ in range(h)]
    visited[0][0] = 1
    i = j = 0
    while True:
        if grid[i][j] == 'U':
            i -= 1
        elif grid[i][j] == 'D':
            i += 1
        elif grid[i][j] == 'L':
            j -= 1
        elif grid[i][j] == 'R':
            j += 1
        if i < 0 or i >= h or j < 0 or j >= w:
            print(i+1, j+1)
            return
        if visited[i][j] == 1:
            print(-1)
            return
        visited[i][j] = 1
