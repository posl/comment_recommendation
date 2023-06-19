def main():
    H, W, K = map(int, input().split())
    c = [input() for _ in range(H)]
    ans = 0
    for i in range(2 ** H):
        for j in range(2 ** W):
            cnt = 0
            for x in range(H):
                for y in range(W):
                    if (i >> x) & 1 == 0 and (j >> y) & 1 == 0 and c[x][y] == '#':
                        cnt += 1
            if cnt == K:
                ans += 1
    print(ans)
main()
