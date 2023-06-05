def main():
    h, w = map(int, input().split())
    grid = [list(input()) for _ in range(h)]
    x, y = 0, 0
    visited = [[False] * w for _ in range(h)]
    while True:
        if grid[x][y] == 'U' and x != 0:
            x -= 1
        elif grid[x][y] == 'D' and x != h - 1:
            x += 1
        elif grid[x][y] == 'L' and y != 0:
            y -= 1
        elif grid[x][y] == 'R' and y != w - 1:
            y += 1
        else:
            break
        if visited[x][y]:
            print(-1)
            return
        visited[x][y] = True
    print(x + 1, y + 1)

if __name__ == '__main__':
    main()