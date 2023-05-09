def solve():
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]
    s = 0
    for i in range(H):
        for j in range(W):
            s += A[i][j]
    print(s - H * W * min(map(min, A)))
