def main():
    H, W = map(int, input().split())
    C_h, C_w = map(int, input().split())
    D_h, D_w = map(int, input().split())
    S = [list(input()) for _ in range(H)]
    C_h -= 1
    C_w -= 1
    D_h -= 1
    D_w -= 1
    dist = [[-1] * W for _ in range(H)]
    dist[C_h][C_w] = 0
    q = [(C_h, C_w)]
    while q:
        i, j = q.pop()
        for i2, j2 in ((i-1, j), (i+1, j), (i, j-1), (i, j+1)):
            if not (0 <= i2 < H and 0 <= j2 < W):
                continue
            if S[i2][j2] == '#':
                continue
            if dist[i2][j2] != -1:
                continue
            dist[i2][j2] = dist[i][j] + 1
            q.append((i2, j2))
        for i2 in range(max(0, i-2), min(H, i+3)):
            for j2 in range(max(0, j-2), min(W, j+3)):
                if S[i2][j2] == '#':
                    continue
                if dist[i2][j2] != -1:
                    continue
                dist[i2][j2] = dist[i][j] + 1
                q.append((i2, j2))
    print(dist[D_h][D_w])

if __name__ == '__main__':
    main()