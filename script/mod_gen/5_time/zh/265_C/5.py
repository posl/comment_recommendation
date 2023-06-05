def main():
    H, W = map(int, input().split())
    grid = [input() for _ in range(H)]
    x, y = 0, 0
    visited = [[0 for _ in range(W)] for _ in range(H)]
    while True:
        if grid[x][y] == 'U':
            if x == 0:
                break
            else:
                x -= 1
        elif grid[x][y] == 'D':
            if x == H - 1:
                break
            else:
                x += 1
        elif grid[x][y] == 'L':
            if y == 0:
                break
            else:
                y -= 1
        elif grid[x][y] == 'R':
            if y == W - 1:
                break
            else:
                y += 1
        if visited[x][y] == 1:
            print(-1)
            return
        else:
            visited[x][y] = 1
    print(x + 1, y + 1)
    return
main()
