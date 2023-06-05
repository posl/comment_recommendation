def main():
    H, W = map(int, input().split())
    C_h, C_w = map(int, input().split())
    D_h, D_w = map(int, input().split())
    S = [list(input()) for _ in range(H)]
    C_h, C_w, D_h, D_w = C_h - 1, C_w - 1, D_h - 1, D_w - 1
    from collections import deque
    q = deque([(C_h, C_w)])
    dist = [[-1] * W for _ in range(H)]
    dist[C_h][C_w] = 0
    while q:
        i, j = q.popleft()
        for i2, j2 in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
            if not (0 <= i2 < H and 0 <= j2 < W):
                continue
            if S[i2][j2] == '#':
                continue
            if dist[i2][j2] != -1:
                continue
            dist[i2][j2] = dist[i][j]
            q.appendleft((i2, j2))
        for i2 in range(i - 2, i + 3):
            for j2 in range(j - 2, j + 3):
                if not (0 <= i2 < H and 0 <= j2 < W):
                    continue
                if S[i2][j2] == '#':
                    continue
                if dist[i2][j2] != -1:
                    continue
                dist[i2][j2] = dist[i][j] + 1
                q.append((i2, j2))
    print(dist[D_h][D_w])

if __name__ == '__main__':
    main()