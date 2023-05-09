def main():
    H, W = map(int, input().split())
    Ch, Cw = map(int, input().split())
    Dh, Dw = map(int, input().split())
    S = []
    for h in range(H):
        S.append(list(input()))
    dist = [[-1] * W for _ in range(H)]
    dist[Ch - 1][Cw - 1] = 0
    q = [(Ch - 1, Cw - 1)]
    while q:
        h, w = q.pop(0)
        for dh, dw in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nh, nw = h + dh, w + dw
            if 0 <= nh < H and 0 <= nw < W and S[nh][nw] == "." and dist[nh][nw] == -1:
                dist[nh][nw] = dist[h][w]
                q.append((nh, nw))
        for dh in range(-2, 3):
            for dw in range(-2, 3):
                nh, nw = h + dh, w + dw
                if 0 <= nh < H and 0 <= nw < W and S[nh][nw] == "." and dist[nh][nw] == -1:
                    dist[nh][nw] = dist[h][w] + 1
                    q.append((nh, nw))
    print(dist[Dh - 1][Dw - 1])
