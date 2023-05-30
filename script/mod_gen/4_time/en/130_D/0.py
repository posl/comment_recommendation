def problems130_d():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    s = [0]
    for i in range(n):
        s.append(s[i] + a[i])
    ans = 0
    l = 0
    r = 1
    while l <= n:
        if s[r] - s[l] >= k:
            ans += n - r + 1
            l += 1
        else:
            if r < n:
                r += 1
            else:
                l += 1
    print(ans)
problems130_d()
