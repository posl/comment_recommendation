def main():
    H, W, K = map(int, input().split())
    c = []
    for i in range(H):
        c.append(list(input()))
    ans = 0
    for i in range(2 ** H):
        for j in range(2 ** W):
            cnt = 0
            for h in range(H):
                for w in range(W):
                    if (i >> h) & 1 == 0 and (j >> w) & 1 == 0 and c[h][w] == '#':
                        cnt += 1
            if cnt == K:
                ans += 1
    print(ans)
