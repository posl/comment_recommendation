def main():
    H, W = map(int, input().split())
    ch, cw = map(int, input().split())
    dh, dw = map(int, input().split())
    S = [input() for _ in range(H)]
    INF = 10**10
    d = [[INF] * W for _ in range(H)]
    d[ch-1][cw-1] = 0
    q = [(ch-1, cw-1)]
    while q:
        h, w = q.pop(0)
        for nh, nw in [(h-1, w), (h+1, w), (h, w-1), (h, w+1)]:
            if 0 <= nh < H and 0 <= nw < W and S[nh][nw] == '.' and d[nh][nw] == INF:
                d[nh][nw] = d[h][w] + 1
                q.append((nh, nw))
        for nh in range(h-2, h+3):
            for nw in range(w-2, w+3):
                if 0 <= nh < H and 0 <= nw < W and S[nh][nw] == '.' and d[nh][nw] == INF:
                    d[nh][nw] = d[h][w] + 1
                    q.append((nh, nw))
    print(d[dh-1][dw-1] if d[dh-1][dw-1] != INF else -1)
