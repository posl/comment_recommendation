def main():
    H, W, K = map(int, input().split())
    C = [input() for _ in range(H)]
    ans = 0
    for h in range(2**H):
        for w in range(2**W):
            black = 0
            for i in range(H):
                for j in range(W):
                    if (h>>i)&1 or (w>>j)&1:
                        continue
                    if C[i][j] == "#":
                        black += 1
            if black == K:
                ans += 1
    print(ans)

if __name__ == '__main__':
    main()