def solve():
    h, w = map(int, input().split())
    a = []
    for _ in range(h):
        a.append(list(map(int, input().split())))
    min_num = 100
    for i in range(h):
        for j in range(w):
            if a[i][j] < min_num:
                min_num = a[i][j]
    ans = 0
    for i in range(h):
        for j in range(w):
            ans += a[i][j] - min_num
    print(ans)
solve()
