def main():
    H, W = map(int, input().split())
    grid = []
    for i in range(H):
        grid.append(input())
    # print(grid)
    visited = [[0]*W for _ in range(H)]
    # print(visited)
    x, y = 0, 0
    while True:
        if grid[x][y] == 'U':
            if x == 0:
                break
            x -= 1
        elif grid[x][y] == 'D':
            if x == H-1:
                break
            x += 1
        elif grid[x][y] == 'L':
            if y == 0:
                break
            y -= 1
        elif grid[x][y] == 'R':
            if y == W-1:
                break
            y += 1
        if visited[x][y] == 1:
            print(-1)
            return
        visited[x][y] = 1
    print(x+1, y+1)
    return
