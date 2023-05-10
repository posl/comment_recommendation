def main():
    H, W = map(int, input().split())
    C_h, C_w = map(int, input().split())
    D_h, D_w = map(int, input().split())
    S = [input() for _ in range(H)]
    C_h -= 1
    C_w -= 1
    D_h -= 1
    D_w -= 1
    INF = 10 ** 18
    dist = [[INF] * W for _ in range(H)]
    dist[C_h][C_w] = 0
    que = [(C_h, C_w)]
    while que:
        h, w = que.pop(0)
        for dh, dw in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nh, nw = h + dh, w + dw
            if not (0 <= nh < H and 0 <= nw < W):
                continue
            if S[nh][nw] == "#":
                continue
            if dist[nh][nw] <= dist[h][w]:
                continue
            dist[nh][nw] = dist[h][w]
            que.append((nh, nw))
        for dh in range(-2, 3):
            for dw in range(-2, 3):
                nh, nw = h + dh, w + dw
                if not (0 <= nh < H and 0 <= nw < W):
                    continue
                if S[nh][nw] == "#":
                    continue
                if dist[nh][nw] <= dist[h][w] + 1:
                    continue
                dist[nh][nw] = dist[h][w] + 1
                que.append((nh, nw))
    ans = dist[D_h][D_w]
    if ans == INF:
        ans = -1
    print(ans)
main()

if __name__ == '__main__':
    main()