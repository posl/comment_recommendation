def main():
    H, W, K = map(int, input().split())
    c = [input() for _ in range(H)]
    ans = 0
    for h in range(2 ** H):
        for w in range(2 ** W):
            cnt = 0
            for i in range(H):
                if (h >> i) & 1:
                    continue
                for j in range(W):
                    if (w >> j) & 1:
                        continue
                    if c[i][j] == '#':
                        cnt += 1
            if cnt == K:
                ans += 1
    print(ans)
