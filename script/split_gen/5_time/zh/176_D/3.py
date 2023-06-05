def main():
    # 读入数据
    H, W = map(int, input().split())
    C_h, C_w = map(int, input().split())
    D_h, D_w = map(int, input().split())
    S = [list(input()) for _ in range(H)]
    # 求解
    # 从(C_h, C_w)到(D_h, D_w)的最短距离
    dist = [[-1] * W for _ in range(H)]
    dist[C_h - 1][C_w - 1] = 0
    queue = [(C_h - 1, C_w - 1)]
    while queue:
        i, j = queue.pop(0)
        for i2, j2 in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
            if not (0 <= i2 < H and 0 <= j2 < W):
                continue
            if S[i2][j2] == '#':
                continue
            if dist[i2][j2] != -1:
                continue
            dist[i2][j2] = dist[i][j] + 1
            queue.append((i2, j2))
    # 从(D_h, D_w)到(C_h, C_w)的最短距离
    dist2 = [[-1] * W for _ in range(H)]
    dist2[D_h - 1][D_w - 1] = 0
    queue = [(D_h - 1, D_w - 1)]
    while queue:
        i, j = queue.pop(0)
        for i2, j2 in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
            if not (0 <= i2 < H and 0 <= j2 < W):
                continue
            if S[i2][j2] == '#':
                continue
            if dist2[i2][j2] != -1:
                continue
            dist2[i2][j2] = dist2[i][j] + 1
            queue.append((i2, j2))
    # 从
