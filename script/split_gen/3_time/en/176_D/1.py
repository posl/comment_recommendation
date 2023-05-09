def main():
    H, W = map(int, input().split())
    C_h, C_w = map(int, input().split())
    D_h, D_w = map(int, input().split())
    S = [list(input()) for i in range(H)]
    C_h -= 1
    C_w -= 1
    D_h -= 1
    D_w -= 1
    INF = 10 ** 9
    dist = [[INF for i in range(W)] for j in range(H)]
    dist[C_h][C_w] = 0
    q = []
    q.append([C_h, C_w])
    while len(q) > 0:
        h, w = q.pop(0)
        if h == D_h and w == D_w:
            break
        if h > 0 and S[h - 1][w] == '.' and dist[h - 1][w] > dist[h][w]:
            dist[h - 1][w] = dist[h][w]
            q.append([h - 1, w])
        if h < H - 1 and S[h + 1][w] == '.' and dist[h + 1][w] > dist[h][w]:
            dist[h + 1][w] = dist[h][w]
            q.append([h + 1, w])
        if w > 0 and S[h][w - 1] == '.' and dist[h][w - 1] > dist[h][w]:
            dist[h][w - 1] = dist[h][w]
            q.append([h, w - 1])
        if w < W - 1 and S[h][w + 1] == '.' and dist[h][w + 1] > dist[h][w]:
            dist[h][w + 1] = dist[h][w]
            q.append([h, w + 1])
        for i in range(-2, 3):
            for j in range(-2, 3):
                if h + i < 0 or h + i >= H or w + j < 0 or w + j >= W:
                    continue
                if S[h + i][w + j] == '#' or dist[h + i][w + j] <= dist[h][w] + 1:
                    continue
                dist[h + i][
