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
    q = deque()
    q.append((C_h, C_w, 0))
    visited = set()
    visited.add((C_h, C_w))
    while q:
        h, w, cnt = q.popleft()
        if h == D_h and w == D_w:
            print(cnt)
            return
        for dh, dw in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nh, nw = h + dh, w + dw
            if 0 <= nh < H and 0 <= nw < W and S[nh][nw] == "." and (nh, nw) not in visited:
                visited.add((nh, nw))
                q.append((nh, nw, cnt))
        for dh in range(-2, 3):
            for dw in range(-2, 3):
                nh, nw = h + dh, w + dw
                if 0 <= nh < H and 0 <= nw < W and S[nh][nw] == "." and (nh, nw) not in visited:
                    visited.add((nh, nw))
                    q.append((nh, nw, cnt + 1))
    print(-1)
