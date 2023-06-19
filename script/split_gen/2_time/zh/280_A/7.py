def main():
    h,w = map(int,input().split())
    grid = [[c for c in input()] for _ in range(h)]
    count = 0
    for i in range(h):
        for j in range(w):
            if grid[i][j] == '#':
                count += 1
    print(count)
