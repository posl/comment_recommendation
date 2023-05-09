def main():
    h, w = map(int, input().split())
    grid = [list(input()) for _ in range(h)]
    for i in range(h):
        for j in range(w):
            grid[i][j] = [i, j]
    i, j = 0, 0
    visited = [[False for _ in range(w)] for _ in range(h)]
    while True:
        if visited[i][j]:
            print(-1)
            return
        visited[i][j] = True
        if grid[i][j] == "U":
            if i == 0:
                print(*grid[i][j])
                return
            i -= 1
        elif grid[i][j] == "D":
            if i == h - 1:
                print(*grid[i][j])
                return
            i += 1
        elif grid[i][j] == "L":
            if j == 0:
                print(*grid[i][j])
                return
            j -= 1
        elif grid[i][j] == "R":
            if j == w - 1:
                print(*grid[i][j])
                return
            j += 1
        else:
            print("error")
            return
