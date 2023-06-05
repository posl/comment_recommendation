def problems101_c():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        ans += 1
        if i + k <= n:
            ans += i // (k - 1)
    print(ans)
problems101_c()
