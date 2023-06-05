def solve():
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]
    total = sum(map(sum, A))
    ave = total // (H * W)
    ans = 0
    for i in range(H):
        for j in range(W):
            ans += abs(A[i][j] - ave)
    print(ans // 2)
