def move(x,y,grid):
    if grid[x][y] == 'U' and x != 0:
        x -= 1
    elif grid[x][y] == 'D' and x != H - 1:
        x += 1
    elif grid[x][y] == 'L' and y != 0:
        y -= 1
    elif grid[x][y] == 'R' and y != W - 1:
        y += 1
    else:
        return -1
    return x, y
H, W = map(int, input().split())
grid = [input() for _ in range(H)]
x, y = 0, 0
visited = set()
while True:
    if (x, y) in visited:
        print(-1)
        break
    visited.add((x, y))
    res = move(x, y, grid)
    if res == -1:
        print(x + 1, y + 1)
        break
    else:
        x, y = res

if __name__ == '__main__':
    move()