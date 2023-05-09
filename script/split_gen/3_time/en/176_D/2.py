def main():
    H, W = map(int, input().split())
    Ch, Cw = map(int, input().split())
    Dh, Dw = map(int, input().split())
    S = [list(input()) for _ in range(H)]
    INF = 10**10
    dist = [[INF] * W for _ in range(H)]
    dist[Ch-1][Cw-1] = 0
    def bfs():
        from collections import deque
        q = deque()
        q.append((Ch-1, Cw-1))
        while q:
            h, w = q.popleft()
            if h == Dh-1 and w == Dw-1:
                return dist[h][w]
            for dh, dw in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nh, nw = h + dh, w + dw
                if 0 <= nh < H and 0 <= nw < W and S[nh][nw] == '.' and dist[nh][nw] == INF:
                    dist[nh][nw] = dist[h][w]
                    q.appendleft((nh, nw))
            for dh in range(-2, 3):
                for dw in range(-2, 3):
                    nh, nw = h + dh, w + dw
                    if 0 <= nh < H and 0 <= nw < W and S[nh][nw] == '.' and dist[nh][nw] == INF:
                        dist[nh][nw] = dist[h][w] + 1
                        q.append((nh, nw))
        return -1
    print(bfs())
main()
