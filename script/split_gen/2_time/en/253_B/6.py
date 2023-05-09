def main():
    h, w = map(int, input().split())
    grid = [input() for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if grid[i][j] == 'o':
                x1 = i
                y1 = j
            elif grid[i][j] == 'o':
                x2 = i
                y2 = j
    print(max(abs(x1 - x2), abs(y1 - y2)))
main()
