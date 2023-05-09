def  main():
    H, W, K = map(int, input().split())
    S = [list(input()) for _ in range(H)]
    ans = 0
    for i in range(2**H):
        for j in range(2**W):
            count = 0
            for h in range(H):
                for w in range(W):
                    if i >> h & 1 or j >> w & 1:
                        continue
                    if S[h][w] == "#":
                        count += 1
            if count == K:
                ans += 1
    print(ans)

if __name__ == '__main__':
    ()