def solve():
    H, W = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(H)]
    ans = []
    for i in range(H):
        for j in range(W - 1):
            if a[i][j] % 2 == 1:
                a[i][j] -= 1
                a[i][j + 1] += 1
                ans.append((i + 1, j + 1, i + 1, j + 2))
    for i in range(H - 1):
        if a[i][W - 1] % 2 == 1:
            a[i][W - 1] -= 1
            a[i + 1][W - 1] += 1
            ans.append((i + 1, W, i + 2, W))
    print(len(ans))
    for i in range(len(ans)):
        print(*ans[i])
solve()
