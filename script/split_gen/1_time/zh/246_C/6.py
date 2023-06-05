def problems246_c():
    n, k, x = map(int, input().split())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        if a[i] > k:
            ans += (a[i] - k) * x
            k = 0
        else:
            k -= a[i]
    print(ans)
