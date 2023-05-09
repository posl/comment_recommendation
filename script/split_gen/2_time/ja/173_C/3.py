def main():
    H, W, K = map(int, input().split())
    c = [input() for _ in range(H)]
    ans = 0
    for i in range(1 << H):
        for j in range(1 << W):
            cnt = 0
            for k in range(H):
                for l in range(W):
                    if i >> k & 1:
                        continue
                    if j >> l & 1:
                        continue
                    if c[k][l] == '#':
                        cnt += 1
            if cnt == K:
                ans += 1
    print(ans)
