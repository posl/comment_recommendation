def main():
    H, W = map(int, input().split())
    ch, cw = map(int, input().split())
    dh, dw = map(int, input().split())
    S = [list(input()) for _ in range(H)]
    ch -= 1
    cw -= 1
    dh -= 1
    dw -= 1
    INF = 10 ** 9
    dist = [[INF] * W for _ in range(H)]
    dist[ch][cw] = 0
    queue = [(ch, cw)]
    while queue:
        h, w = queue.pop(0)
        for dh, dw in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            nh, nw = h + dh, w + dw
            if 0 <= nh < H and 0 <= nw < W and S[nh][nw] == '.' and dist[nh][nw] > dist[h][w]:
                dist[nh][nw] = dist[h][w]
                queue.append((nh, nw))
        for dh in range(-2, 3):
            for dw in range(-2, 3):
                nh, nw = h + dh, w + dw
                if 0 <= nh < H and 0 <= nw < W and S[nh][nw] == '.' and dist[nh][nw] > dist[h][w] + 1:
                    dist[nh][nw] = dist[h][w] + 1
                    queue.append((nh, nw))
    if dist[dh][dw] == INF:
        print(-1)
    else:
        print(dist[dh][dw])

if __name__ == '__main__':
    main()