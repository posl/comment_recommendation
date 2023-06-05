def main():
    h, w = map(int, input().split())
    c_h, c_w = map(int, input().split())
    d_h, d_w = map(int, input().split())
    s = [input() for _ in range(h)]
    c_h -= 1
    c_w -= 1
    d_h -= 1
    d_w -= 1
    inf = 10**9
    dist = [[inf for _ in range(w)] for _ in range(h)]
    dist[c_h][c_w] = 0
    que = []
    que.append((c_h, c_w))
    while len(que) > 0:
        now_h, now_w = que.pop(0)
        for i in range(-2, 3):
            for j in range(-2, 3):
                next_h = now_h + i
                next_w = now_w + j
                if next_h < 0 or next_h >= h or next_w < 0 or next_w >= w:
                    continue
                if s[next_h][next_w] == '#':
                    continue
                if dist[next_h][next_w] <= dist[now_h][now_w]:
                    continue
                dist[next_h][next_w] = dist[now_h][now_w]
                que.append((next_h, next_w))
        for i in range(-1, 2):
            for j in range(-1, 2):
                next_h = now_h + i
                next_w = now_w + j
                if next_h < 0 or next_h >= h or next_w < 0 or next_w >= w:
                    continue
                if dist[next_h][next_w] <= dist[now_h][now_w] + 1:
                    continue
                dist[next_h][next_w] = dist[now_h][now_w] + 1
                que.append((next_h, next_w))
    if dist[d_h][d_w] == inf:
        print(-1)
    else:
        print(dist[d_h][d_w])
