def main():
    H, W, K = map(int, input().split())
    c = []
    for _ in range(H):
        c.append(input())
    #print(c)
    ans = 0
    for h in range(1 << H):
        for w in range(1 << W):
            cnt = 0
            for i in range(H):
                for j in range(W):
                    if (h >> i & 1) == 0 and (w >> j & 1) == 0 and c[i][j] == '#':
                        cnt += 1
            if cnt == K:
                ans += 1
    print(ans)

if __name__ == '__main__':
    main()