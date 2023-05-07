def main():
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]
    total = sum(sum(a) for a in A)
    if total % (H * W) != 0:
        print(-1)
        return
    n = total // (H * W)
    ans = 0
    for i in range(H):
        for j in range(W):
            if (i + j) % 2 == 0:
                ans += abs(A[i][j] - n)
    print(ans // 2)
