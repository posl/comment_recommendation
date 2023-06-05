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
    q = []
    q.append([C_h, C_w])
    dist[C_h][C_w] = 0
    while len(q) > 0:
        h, w = q.pop(0)
        for dh, dw in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
            nh = h + dh
            nw = w + dw
            if nh < 0 or nw < 0 or nh >= H or nw >= W:
                continue
            if S[nh][nw] == '#':
                continue
            if dist[nh][nw] == -1:
                dist[nh][nw] = dist[h][w]
                q.append([nh, nw])
    print(dist[D_h][D_w])

if __name__ == '__main__':
    main()