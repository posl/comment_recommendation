def main():
    H,W,K = map(int,input().split())
    C = [input() for i in range(H)]
    ans = 0
    for i in range(1 << H):
        for j in range(1 << W):
            count = 0
            for h in range(H):
                for w in range(W):
                    if (i >> h) & 1 == 1 and (j >> w) & 1 == 1 and C[h][w] == "#":
                        count += 1
            if count == K:
                ans += 1
    print(ans)
