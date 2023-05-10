def main():
    H, W = map(int, input().split())
    C_h, C_w = map(int, input().split())
    D_h, D_w = map(int, input().split())
    S = [list(input()) for i in range(H)]
    C_h -= 1
    C_w -= 1
    D_h -= 1
    D_w -= 1
    from collections import deque
    q = deque()
    q.append((C_h, C_w))
    dist = [[-1] * W for i in range(H)]
    dist[C_h][C_w] = 0
    while q:
        h, w = q.popleft()
        for dh, dw in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nh = h + dh
            nw = w + dw
            if not (0 <= nh < H and 0 <= nw < W):
                continue
            if S[nh][nw] == "#":
                continue
            if dist[nh][nw] == -1:
                dist[nh][nw] = dist[h][w]
                q.appendleft((nh, nw))
    ans = dist[D_h][D_w]
    print(ans)
