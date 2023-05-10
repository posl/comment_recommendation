def problem130_d():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    ans = 0
    r = 0
    s = 0
    for l in range(n):
        while r < n and s + a[r] < k:
            s += a[r]
            r += 1
        ans += r - l
        if r == l:
            r += 1
        else:
            s -= a[l]
    print(ans)
