def main():
    h,w = map(int, input().split())
    grid = []
    for _ in range(h):
        grid.append(input())
    for i in range(w):
        count = 0
        for j in range(h):
            if grid[j][i] == '#':
                count += 1
        print(count)
