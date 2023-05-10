def main():
    H, W = map(int, input().split())
    S = [list(input()) for _ in range(H)]
    ans = 0
    for h in range(H):
        for w in range(W):
            if S[h][w] == '#':
                continue
            cnt = 0
            for dh, dw in ((1, 0), (0, 1), (-1, 0), (0, -1)):
                nh = h + dh
                nw = w + dw
                while 0 <= nh < H and 0 <= nw < W:
                    if S[nh][nw] == '#':
                        break
                    cnt += 1
                    nh += dh
                    nw += dw
            ans = max(ans, cnt)
    print(ans + 1)
