def main():
    H, W, K = map(int, input().split())
    c = [list(input()) for _ in range(H)]
    ans = 0
    for i in range(2**H):
        for j in range(2**W):
            cnt = 0
            for k in range(H):
                for l in range(W):
                    if i & (1 << k) == 0 and j & (1 << l) == 0 and c[k][l] == '#':
                        cnt += 1
            if cnt == K:
                ans += 1
    print(ans)
