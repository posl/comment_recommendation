def main():
    H, W, A, B = map(int, input().split())
    ans = 0
    for i in range(1 << (H * W)):
        cnt = 0
        for j in range(H * W):
            if i >> j & 1:
                cnt += 1
        if cnt == A:
            cnt = 0
            for j in range(H):
                for k in range(W):
                    if i >> (j * W + k) & 1 and i >> (j * W + k + 1) & 1:
                        cnt += 1
            if cnt == B:
                ans += 1
    print(ans)
