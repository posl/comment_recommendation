def main():
    h, w = map(int, input().split())
    grid = [list(input()) for _ in range(h)]
    seen = [[0] * w for _ in range(h)]
    i, j = 0, 0
    while True:
        if seen[i][j]:
            print(-1)
            return
        seen[i][j] = 1
        if grid[i][j] == 'U':
            if i == 0:
                print(i+1, j+1)
                return
            i -= 1
        elif grid[i][j] == 'D':
            if i == h-1:
                print(i+1, j+1)
                return
            i += 1
        elif grid[i][j] == 'L':
            if j == 0:
                print(i+1, j+1)
                return
            j -= 1
        else:
            if j == w-1:
                print(i+1, j+1)
                return
            j += 1
