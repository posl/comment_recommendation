def main():
    h, w = map(int, input().split())
    #print(h, w)
    grid = []
    for i in range(h):
        grid.append(input())
    #print(grid)
    for i in range(w):
        count = 0
        for j in range(h):
            #print(grid[j][i])
            if grid[j][i] == "#":
                count += 1
        print(count)
