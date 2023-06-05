def solve():
    n, m, c = map(int, input().split())
    b = list(map(int, input().split()))
    a = [list(map(int, input().split())) for _ in range(n)]
    ans = 0
    for i in range(n):
        tmp = c
        for j in range(m):
            tmp += a[i][j] * b[j]
        if tmp > 0:
            ans += 1
    print(ans)
