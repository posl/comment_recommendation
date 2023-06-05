def main():
    H, W = map(int, input().split())
    C_h, C_w = map(int, input().split())
    D_h, D_w = map(int, input().split())
    S = [list(input()) for _ in range(H)]
    C_h -= 1
    C_w -= 1
    D_h -= 1
    D_w -= 1
    INF = 10 ** 9
    dist = [[INF] * W for _ in range(H)]
    dist[C_h][C_w] = 0
    queue = []
    queue.append((C_h, C_w))
    while queue:
        i, j = queue.pop(0)
        for i2, j2 in ((i + 1, j), (i - 1, j), (i, j - 1), (i, j + 1)):
            if not (0 <= i2 < H and 0 <= j2 < W):
                continue
            if S[i2][j2] == '#':
                continue
            if dist[i2][j2] != INF:
                continue
            dist[i2][j2] = dist[i][j]
            queue.append((i2, j2))
    for i in range(max(0, D_h - 2), min(H, D_h + 3)):
        for j in range(max(0, D_w - 2), min(W, D_w + 3)):
            if S[i][j] == '#':
                continue
            dist[i][j] += 1
    if dist[D_h][D_w] == INF:
        print(-1)
    else:
        print(dist[D_h][D_w])
