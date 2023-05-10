def main():
    H, W = map(int, input().split())
    C_h, C_w = map(int, input().split())
    D_h, D_w = map(int, input().split())
    S = [input() for _ in range(H)]
    C_h -= 1
    C_w -= 1
    D_h -= 1
    D_w -= 1
    dist = [[float("inf")] * W for _ in range(H)]
    dist[C_h][C_w] = 0
    que = [(C_h, C_w)]
    while que:
        h, w = que.pop(0)
        if h == D_h and w == D_w:
            break
        for dh, dw in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nh, nw = h + dh, w + dw
            if nh < 0 or nh >= H or nw < 0 or nw >= W or S[nh][nw] == "#" or dist[nh][nw] <= dist[h][w]:
                continue
            dist[nh][nw] = dist[h][w]
            que.insert(0, (nh, nw))
        for dh in range(-2, 3):
            for dw in range(-2, 3):
                nh, nw = h + dh, w + dw
                if nh < 0 or nh >= H or nw < 0 or nw >= W or S[nh][nw] == "#" or dist[nh][nw] <= dist[h][w] + 1:
                    continue
                dist[nh][nw] = dist[h][w] + 1
                que.append((nh, nw))
    print(dist[D_h][D_w] if dist[D_h][D_w] < float("inf") else -1)

if __name__ == '__main__':
    main()