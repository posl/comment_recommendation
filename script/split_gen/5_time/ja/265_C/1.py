def move(i, j):
    if g[i][j] == 'U' and i > 0:
        return i-1, j
    elif g[i][j] == 'D' and i < H-1:
        return i+1, j
    elif g[i][j] == 'L' and j > 0:
        return i, j-1
    elif g[i][j] == 'R' and j < W-1:
        return i, j+1
    else:
        return i, j
H, W = map(int, input().split())
g = [list(input()) for _ in range(H)]
i, j = 0, 0
seen = [[False for _ in range(W)] for _ in range(H)]
while True:
    if seen[i][j]:
        print(-1)
        exit()
    seen[i][j] = True
    i, j = move(i, j)
    if i == H-1 and j == W-1:
        print(i+1, j+1)
        exit()
