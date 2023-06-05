def solve():
    H, W = map(int, input().split())
    A = []
    for i in range(H):
        A.append(list(map(int, input().split())))
    min_A = min([min(a) for a in A])
    ans = 0
    for i in range(H):
        for j in range(W):
            ans += A[i][j] - min_A
    print(ans)
