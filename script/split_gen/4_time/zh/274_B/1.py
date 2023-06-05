def main():
    h,w = map(int, input().split())
    grid = [input() for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if grid[i][j] == '#':
                print(j)
                break
        else:
            print(w)
main()
