def main():
    H, W, K = map(int, input().split())
    C = [input() for _ in range(H)]
    ans = 0
    for i in range(2**H):
        for j in range(2**W):
            cnt = 0
            for h in range(H):
                for w in range(W):
                    if i >> h & 1 or j >> w & 1:
                        continue
                    if C[h][w] == "#":
                        cnt += 1
            if cnt == K:
                ans += 1
    print(ans)
