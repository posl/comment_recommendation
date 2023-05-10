def main():
    # input
    H, W = map(int, input().split())
    C_s = [input() for _ in range(H)]
    # compute
    ans = 0
    for h in range(H):
        for w in range(W):
            for dh, dw in [(1, 0), (0, 1)]:
                if h+dh < H and w+dw < W:
                    if C_s[h][w] == '.' and C_s[h+dh][w+dw] == '.':
                        ans += 1
    # output
    print(ans)

if __name__ == '__main__':
    main()