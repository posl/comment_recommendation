def main():
    H, W, K = map(int, input().split())
    C = [list(input()) for _ in range(H)]
    ans = 0
    for i in range(2 ** H):
        for j in range(2 ** W):
            tmp = 0
            for k in range(H):
                for l in range(W):
                    if (i >> k & 1) == 0 and (j >> l & 1) == 0:
                        if C[k][l] == '#':
                            tmp += 1
            if tmp == K:
                ans += 1
    print(ans)
