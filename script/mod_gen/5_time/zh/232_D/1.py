def get_max_count(x, y, H, W, C):
    if x == H or y == W:
        return 0
    if C[x][y] == '#':
        return 0
    return max(get_max_count(x+1, y, H, W, C), get_max_count(x, y+1, H, W, C)) + 1
H, W = map(int, input().split())
C = []
for i in range(H):
    C.append(list(input()))
print(get_max_count(0, 0, H, W, C))
