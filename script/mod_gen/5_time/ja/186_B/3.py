def solve():
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]
    min_a = 100
    for i in range(H):
        for j in range(W):
            min_a = min(min_a, A[i][j])
    ans = 0
    for i in range(H):
        for j in range(W):
            ans += A[i][j] - min_a
    print(ans)
solve()
