def main():
    h, w = map(int, input().split())
    grid = [input() for _ in range(h)]
    visited = [[False for _ in range(w)] for _ in range(h)]
    i, j = 0, 0
    while True:
        if visited[i][j]:
            print(-1)
            return
        visited[i][j] = True
        if grid[i][j] == 'U':
            if i > 0:
                i -= 1
            else:
                break
        elif grid[i][j] == 'D':
            if i < h - 1:
                i += 1
            else:
                break
        elif grid[i][j] == 'L':
            if j > 0:
                j -= 1
            else:
                break
        elif grid[i][j] == 'R':
            if j < w - 1:
                j += 1
            else:
                break
    print(i + 1, j + 1)
