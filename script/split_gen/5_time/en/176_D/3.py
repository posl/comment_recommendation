def main():
    H, W = map(int, input().split())
    C_h, C_w = map(int, input().split())
    D_h, D_w = map(int, input().split())
    S = [input() for _ in range(H)]
    C_h -= 1
    C_w -= 1
    D_h -= 1
    D_w -= 1
    dist = [[float("inf") for _ in range(W)] for _ in range(H)]
    dist[C_h][C_w] = 0
    que = [(C_h, C_w, 0)]
    while que:
        h, w, d = que.pop(0)
        if h == D_h and w == D_w:
            break
        for i, j in ((h-1, w), (h+1, w), (h, w-1), (h, w+1)):
            if 0 <= i < H and 0 <= j < W and S[i][j] == "." and dist[i][j] > d:
                dist[i][j] = d
                que.append((i, j, d))
        for i in range(h-2, h+3):
            for j in range(w-2, w+3):
                if 0 <= i < H and 0 <= j < W and S[i][j] == "." and dist[i][j] > d+1:
                    dist[i][j] = d+1
                    que.append((i, j, d+1))
    if dist[D_h][D_w] == float("inf"):
        print(-1)
    else:
        print(dist[D_h][D_w])
