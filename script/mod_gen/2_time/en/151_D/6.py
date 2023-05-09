def main():
    H, W = map(int, input().split())
    S = [list(input()) for _ in range(H)]
    INF = 10**5
    dist = [[INF] * W for _ in range(H)]
    dist[0][0] = 0
    for h in range(H):
        for w in range(W):
            if h > 0 and S[h - 1][w] == '.' and S[h][w] == '.':
                dist[h][w] = min(dist[h][w], dist[h - 1][w] + 1)
            if w > 0 and S[h][w - 1] == '.' and S[h][w] == '.':
                dist[h][w] = min(dist[h][w], dist[h][w - 1] + 1)
    for h in range(H - 1, -1, -1):
        for w in range(W - 1, -1, -1):
            if h < H - 1 and S[h + 1][w] == '.' and S[h][w] == '.':
                dist[h][w] = min(dist[h][w], dist[h + 1][w] + 1)
            if w < W - 1 and S[h][w + 1] == '.' and S[h][w] == '.':
                dist[h][w] = min(dist[h][w], dist[h][w + 1] + 1)
    ans = 0
    for h in range(H):
        for w in range(W):
            if S[h][w] == '.':
                ans = max(ans, dist[h][w])
    print(ans)

if __name__ == '__main__':
    main()