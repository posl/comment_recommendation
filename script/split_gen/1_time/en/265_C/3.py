def main():
    h, w = map(int, input().split())
    grid = [input() for _ in range(h)]
    visited = [[False] * w for _ in range(h)]
    x, y = 0, 0
    while True:
        if x < 0 or x >= h or y < 0 or y >= w:
            print(-1)
            return
        if visited[x][y]:
            print(-1)
            return
        visited[x][y] = True
        if grid[x][y] == 'U':
            x -= 1
        elif grid[x][y] == 'D':
            x += 1
        elif grid[x][y] == 'L':
            y -= 1
        else:
            y += 1
        if x < 0 or x >= h or y < 0 or y >= w:
            print(x + 1, y + 1)
            return
