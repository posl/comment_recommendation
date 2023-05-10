def problem258_b():
    n = int(input())
    a = [list(map(int, input())) for _ in range(n)]
    ans = 0
    for i in range(n):
        for j in range(n):
            if i == 0 or j == 0 or i == n - 1 or j == n - 1:
                continue
            ans = max(ans, a[i][j] + a[i - 1][j] + a[i + 1][j] + a[i][j - 1] + a[i][j + 1])
    print(ans)
