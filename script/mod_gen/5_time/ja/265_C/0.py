def move(i, j, H, W):
    if i == H and j == W:
        return i, j
    if G[i][j] == "U" and i > 1:
        return move(i-1, j, H, W)
    if G[i][j] == "D" and i < H:
        return move(i+1, j, H, W)
    if G[i][j] == "L" and j > 1:
        return move(i, j-1, H, W)
    if G[i][j] == "R" and j < W:
        return move(i, j+1, H, W)
    return -1, -1
H, W = map(int, input().split())
G = [input() for _ in range(H)]
i, j = move(1, 1, H, W)
print(i, j)

if __name__ == '__main__':
    move()