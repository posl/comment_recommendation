def main():
    h, w = map(int, input().split())
    ch, cw = map(int, input().split())
    dh, dw = map(int, input().split())
    s = [list(input()) for _ in range(h)]
    dist = [[-1]*w for _ in range(h)]
    dist[ch-1][cw-1] = 0
    q = [(ch-1, cw-1)]
    while q:
        nh, nw = q.pop(0)
        for dh, dw in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            nh2, nw2 = nh+dh, nw+dw
            if 0 <= nh2 < h and 0 <= nw2 < w and s[nh2][nw2] == "." and dist[nh2][nw2] == -1:
                dist[nh2][nw2] = dist[nh][nw]
                q.append((nh2, nw2))
        for dh in range(-2, 3):
            for dw in range(-2, 3):
                nh2, nw2 = nh+dh, nw+dw
                if 0 <= nh2 < h and 0 <= nw2 < w and s[nh2][nw2] == "." and dist[nh2][nw2] == -1:
                    dist[nh2][nw2] = dist[nh][nw] + 1
                    q.append((nh2, nw2))
    print(dist[dh-1][dw-1])
