def main():
    H, W = map(int, input().split())
    C_h, C_w = map(int, input().split())
    D_h, D_w = map(int, input().split())
    S = [input() for _ in range(H)]
    C_h -= 1
    C_w -= 1
    D_h -= 1
    D_w -= 1
    from collections import deque
    q = deque([(C_h, C_w, 0)])
    dist = [[float('inf')] * W for _ in range(H)]
    dist[C_h][C_w] = 0
    while q:
        h, w, d = q.popleft()
        if h == D_h and w == D_w:
            print(d)
            return
        for dh, dw in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            nh, nw = h + dh, w + dw
            if 0 <= nh < H and 0 <= nw < W and S[nh][nw] == '.':
                if dist[nh][nw] > d:
                    dist[nh][nw] = d
                    q.appendleft((nh, nw, d))
        for dh in range(-2, 3):
            for dw in range(-2, 3):
                nh, nw = h + dh, w + dw
                if 0 <= nh < H and 0 <= nw < W and S[nh][nw] == '.':
                    if dist[nh][nw] > d + 1:
                        dist[nh][nw] = d + 1
                        q.append((nh, nw, d + 1))
    print(-1)
