def main():
    h, w = map(int, input().split())
    grid = [list(input()) for _ in range(h)]
    sy, sx = 0, 0
    while True:
        if sy == h - 1 and sx == w - 1:
            print(sy + 1, sx + 1)
            return
        if grid[sy][sx] == 'U':
            sy -= 1
        elif grid[sy][sx] == 'D':
            sy += 1
        elif grid[sy][sx] == 'L':
            sx -= 1
        elif grid[sy][sx] == 'R':
            sx += 1
        if sy < 0 or sy >= h or sx < 0 or sx >= w:
            print(-1)
            return
