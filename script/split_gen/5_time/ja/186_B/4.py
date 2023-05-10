def solve():
    H, W = map(int, input().split())
    A = []
    for _ in range(H):
        A.append(list(map(int, input().split())))
    min_A = 100
    for i in range(H):
        for j in range(W):
            min_A = min(min_A, A[i][j])
    ans = 0
    for i in range(H):
        for j in range(W):
            ans += A[i][j] - min_A
    print(ans)
