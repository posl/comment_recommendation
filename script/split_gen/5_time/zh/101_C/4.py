def problems101_c():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(1, n):
        if a[i] > a[i - 1]:
            ans += 1
    print(ans)
problems101_c()
