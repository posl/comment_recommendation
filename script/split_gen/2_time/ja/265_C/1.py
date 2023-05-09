def main():
    H, W = map(int, input().split())
    grid = [list(input()) for _ in range(H)]
    i, j = 0, 0
    for _ in range(H*W):
        if grid[i][j] == 'U':
            i -= 1
        elif grid[i][j] == 'D':
            i += 1
        elif grid[i][j] == 'L':
            j -= 1
        elif grid[i][j] == 'R':
            j += 1
        if i < 0 or i >= H or j < 0 or j >= W:
            print(i+1, j+1)
            return
    print(-1)
