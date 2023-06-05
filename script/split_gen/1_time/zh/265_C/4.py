def main():
    h,w = map(int,input().split())
    grid = []
    for i in range(h):
        grid.append(input())
    x = 0
    y = 0
    visited = [[0 for i in range(w)] for j in range(h)]
    visited[x][y] = 1
    while True:
        if grid[x][y] == 'U':
            x -= 1
        elif grid[x][y] == 'D':
            x += 1
        elif grid[x][y] == 'L':
            y -= 1
        elif grid[x][y] == 'R':
            y += 1
        if x < 0 or x >= h or y < 0 or y >= w:
            print(x+1,y+1)
            return
        if visited[x][y] == 1:
            print(-1)
            return
        visited[x][y] = 1
