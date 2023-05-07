def main():
    H, W, K = map(int, input().split())
    C = [input() for _ in range(H)]
    ans = 0
    for i in range(2**H):
        for j in range(2**W):
            cnt = 0
            for x in range(H):
                for y in range(W):
                    if (i >> x) & 1 == 0 and (j >> y) & 1 == 0 and C[x][y] == "#":
                        cnt += 1
            if cnt == K:
                ans += 1
    print(ans)

if __name__ == '__main__':
    main()