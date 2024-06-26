def main():
    # H, W, K = map(int, input().split())
    # C = [input() for _ in range(H)]
    H, W, K = 6, 6, 8
    C = ['..##..', '.#..#.', '##....#', '#######', '##....#', '##....#']
    ans = 0
    for i in range(2 ** H):
        for j in range(2 ** W):
            cnt = 0
            for k in range(H):
                for l in range(W):
                    if ((i >> k) & 1) == 0 and ((j >> l) & 1) == 0 and C[k][l] == '#':
                        cnt += 1
            if cnt == K:
                ans += 1
    print(ans)
