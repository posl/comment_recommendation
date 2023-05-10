def main():
    H, W = map(int, input().split())
    C_h, C_w = map(int, input().split())
    D_h, D_w = map(int, input().split())
    S = [input() for _ in range(H)]
    C_h -= 1
    C_w -= 1
    D_h -= 1
    D_w -= 1
    INF = 10 ** 9
    dist = [[INF] * W for _ in range(H)]
    dist[C_h][C_w] = 0
    q = [(C_h, C_w)]
    while q:
        h, w = q.pop(0)
        for dh, dw in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nh, nw = h + dh, w + dw
            if not (0 <= nh < H and 0 <= nw < W):
                continue
            if S[nh][nw] == "#":
                continue
            if dist[nh][nw] <= dist[h][w]:
                continue
            dist[nh][nw] = dist[h][w]
            q.append((nh, nw))
        for nh in range(max(0, h - 2), min(h + 3, H)):
            for nw in range(max(0, w - 2), min(w + 3, W)):
                if S[nh][nw] == "#":
                    continue
                if dist[nh][nw] <= dist[h][w] + 1:
                    continue
                dist[nh][nw] = dist[h][w] + 1
                q.append((nh, nw))
    print(-1 if dist[D_h][D_w] == INF else dist[D_h][D_w])

if __name__ == '__main__':
    main()