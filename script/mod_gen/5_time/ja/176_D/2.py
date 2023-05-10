def main():
    H, W = map(int, input().split())
    C_h, C_w = map(int, input().split())
    D_h, D_w = map(int, input().split())
    S = [list(input()) for _ in range(H)]
    C_h -= 1
    C_w -= 1
    D_h -= 1
    D_w -= 1
    INF = 10**9
    dist = [[INF] * W for _ in range(H)]
    dist[C_h][C_w] = 0
    queue = [(C_h, C_w)]
    while queue:
        h, w = queue.pop(0)
        for dh, dw in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            if not (0 <= h + dh < H and 0 <= w + dw < W):
                continue
            if S[h + dh][w + dw] == '#':
                continue
            if dist[h][w] + 1 < dist[h + dh][w + dw]:
                dist[h + dh][w + dw] = dist[h][w] + 1
                queue.append((h + dh, w + dw))
    ans = dist[D_h][D_w]
    if ans == INF:
        ans = -1
    print(ans)

if __name__ == '__main__':
    main()