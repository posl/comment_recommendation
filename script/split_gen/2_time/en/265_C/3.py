def main():
    h, w = map(int, input().split())
    grid = [input() for i in range(h)]
    visited = [[False] * w for i in range(h)]
    visited[0][0] = True
    i = 0
    j = 0
    while True:
        if grid[i][j] == 'U' and i != 0:
            i -= 1
        elif grid[i][j] == 'D' and i != h-1:
            i += 1
        elif grid[i][j] == 'L' and j != 0:
            j -= 1
        elif grid[i][j] == 'R' and j != w-1:
            j += 1
        else:
            break
        if visited[i][j]:
            print(-1)
            return
        visited[i][j] = True
    print(i+1, j+1)
