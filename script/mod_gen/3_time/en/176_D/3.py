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
    from collections import deque
    q = deque()
    q.append((ch, cw))
    while q:
        h, w = q.popleft()
        for dh, dw in ((1, 0), (0, 1), (-1, 0), (0, -1)):
            nh = h + dh
            nw = w + dw
            if 0 <= nh < H and 0 <= nw < W and S[nh][nw] == '.' and dist[nh][nw] == INF:
                dist[nh][nw] = dist[h][w]
                q.appendleft((nh, nw))
        for dh in range(-2, 3):
            for dw in range(-2, 3):
                nh = h + dh
                nw = w + dw
                if 0 <= nh < H and 0 <= nw < W and S[nh][nw] == '.' and dist[nh][nw] == INF:
                    dist[nh][nw] = dist[h][w] + 1
                    q.append((nh, nw))
    if dist[dh][dw] == INF:
        print(-1)
    else:
        print(dist[dh][dw])
main()
