def solve(h1,h2,h3,w1,w2,w3):
    grid = [0]*9
    for i in range(3):
        grid[i] = h1//3
        if i < h1%3:
            grid[i] += 1
    for i in range(3):
        grid[i+3] = h2//3
        if i < h2%3:
            grid[i+3] += 1
    for i in range(3):
        grid[i+6] = h3//3
        if i < h3%3:
            grid[i+6] += 1
    for i in range(3):
        grid[i*3] -= w1//3
        if i < w1%3:
            grid[i*3] -= 1
    for i in range(3):
        grid[i*3+1] -= w2//3
        if i < w2%3:
            grid[i*3+1] -= 1
    for i in range(3):
        grid[i*3+2] -= w3//3
        if i < w3%3:
            grid[i*3+2] -= 1
    if grid[0] == grid[1] == grid[2] == grid[3] == grid[4] == grid[5] == grid[6] == grid[7] == grid[8]:
        return 1
    else:
        return 0
h1,h2,h3,w1,w2,w3 = map(int,input().split())
print(solve(h1,h2,h3,w1,w2,w3))
